from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import operator
from typing import SupportsIndex, cast

import numpy as np

from .dependencies import require_umap


@dataclass(frozen=True, slots=True)
class Projection:
    coordinates: np.ndarray
    neighbor_ids: np.ndarray
    neighbor_distances: np.ndarray
    algorithm: str
    options: Mapping[str, object]


def project_vectors(
    vectors: np.ndarray,
    *,
    umap: Mapping[str, object],
) -> Projection:
    """Project vectors and return the neighbor graph used by UMAP."""

    matrix = np.asarray(vectors, dtype=np.float32)
    if matrix.ndim != 2:
        raise ValueError("Vectors must be a two-dimensional matrix.")
    if matrix.shape[1] == 0:
        raise ValueError("Vectors must have at least one dimension.")
    if not np.isfinite(matrix).all():
        raise ValueError("Vectors must contain only finite values.")

    options = _options(umap)
    row_count = matrix.shape[0]
    resolved = dict(options)
    resolved["n_neighbors"] = (
        0
        if row_count == 0
        else row_count
        if row_count < 3
        else min(cast(int, options["n_neighbors"]), row_count - 1)
    )
    resolved["n_components"] = 2
    resolved["n_jobs"] = 1
    if row_count == 0:
        return Projection(
            coordinates=np.empty((0, 2), dtype=np.float32),
            neighbor_ids=np.empty((0, 0), dtype=np.int32),
            neighbor_distances=np.empty((0, 0), dtype=np.float32),
            algorithm="empty",
            options=resolved,
        )

    require_umap()
    from umap.umap_ import nearest_neighbors

    neighbor_count = cast(int, resolved["n_neighbors"])
    ids, distances, search_index = nearest_neighbors(
        matrix,
        n_neighbors=neighbor_count,
        metric=options["metric"],
        metric_kwds=options.get("metric_kwds"),
        angular=False,
        random_state=options["random_state"],
        n_jobs=1,
    )
    ids, distances = _stable_neighbors(ids, distances)

    if row_count < 3:
        return Projection(
            coordinates=np.column_stack(
                (
                    np.arange(row_count, dtype=np.float32),
                    np.zeros(row_count, dtype=np.float32),
                )
            ),
            neighbor_ids=ids,
            neighbor_distances=distances,
            algorithm="linear",
            options=resolved,
        )

    import umap as umap_module

    if row_count == 3:
        resolved["init"] = "random"
    else:
        resolved.setdefault("init", "spectral")
    coordinates = np.asarray(
        umap_module.UMAP(
            **resolved,
            precomputed_knn=(ids.copy(), distances.copy(), search_index),
        ).fit_transform(matrix),
        dtype=np.float32,
    )
    if not np.isfinite(coordinates).all():
        raise ValueError("UMAP projection produced non-finite coordinates.")
    return Projection(
        coordinates=coordinates,
        neighbor_ids=ids,
        neighbor_distances=distances,
        algorithm="umap",
        options=resolved,
    )


def _options(values: Mapping[str, object]) -> dict[str, object]:
    reserved = {"n_components", "n_jobs", "precomputed_knn"} & values.keys()
    if reserved:
        names = ", ".join(sorted(reserved))
        raise ValueError(f"ChartCoach owns these UMAP options: {names}.")

    options: dict[str, object] = {
        "n_neighbors": 15,
        "min_dist": 0.1,
        "metric": "cosine",
        "random_state": 42,
    }
    options.update(values)
    try:
        n_neighbors = operator.index(cast(SupportsIndex, options["n_neighbors"]))
        random_state = operator.index(cast(SupportsIndex, options["random_state"]))
    except TypeError as exc:
        raise ValueError("UMAP n_neighbors and random_state must be integers.") from exc
    if isinstance(options["n_neighbors"], bool) or n_neighbors < 2:
        raise ValueError("UMAP n_neighbors must be an integer of at least 2.")
    if isinstance(options["random_state"], bool):
        raise ValueError("UMAP random_state must be an integer.")
    if not isinstance(options["metric"], str) or not options["metric"]:
        raise ValueError("UMAP metric must be a non-empty string.")
    options["n_neighbors"] = n_neighbors
    options["random_state"] = random_state
    return options


def _stable_neighbors(
    ids: np.ndarray,
    distances: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    stable_ids = np.empty(ids.shape, dtype=np.int32)
    stable_distances = np.empty(distances.shape, dtype=np.float32)
    for row in range(ids.shape[0]):
        neighbors = {
            int(neighbor_id): float(distance)
            for neighbor_id, distance in zip(ids[row], distances[row], strict=True)
            if neighbor_id >= 0 and np.isfinite(distance)
        }
        neighbors.pop(row, None)
        pairs = [
            (row, 0.0),
            *sorted(neighbors.items(), key=lambda pair: (pair[1], pair[0])),
        ]
        if len(pairs) < ids.shape[1]:
            raise ValueError("Nearest-neighbor search returned an incomplete graph.")
        pairs = pairs[: ids.shape[1]]
        stable_ids[row] = [neighbor_id for neighbor_id, _ in pairs]
        stable_distances[row] = [distance for _, distance in pairs]
    return stable_ids, stable_distances


__all__ = ["Projection", "project_vectors"]
