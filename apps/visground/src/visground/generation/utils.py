from typing import Any, Type

import polars as pl
from slugify import slugify


def pyexecute(
    code: str,
    context: dict[str, Any] | None = None,
    expected_type: Type[Any] | tuple[Type[Any], ...] | None = None,
    result_name: str = "result",
) -> Any:
    namespace = {
        "__builtins__": __builtins__,
        **(context or {}),
    }

    compiled = compile(code, "<dynamic>", "exec")
    exec(compiled, namespace, namespace)

    if result_name not in namespace:
        raise ValueError(f"Code must assign `{result_name}`")

    result = namespace[result_name]

    if expected_type is not None and not isinstance(result, expected_type):
        raise TypeError(f"Expected {expected_type}, got {type(result)}")

    return result


def create_field_sample(
    df: pl.DataFrame,
    field: str,
    n: int,
    max_chars: int,
    list_n: int,
) -> list:
    dtype = df.get_column(field).dtype
    truncate_scalar = pl.col(field).cast(pl.String).str.slice(0, max_chars)
    truncate_list = pl.col(field).list.head(list_n)
    truncate = truncate_list if dtype == pl.List else truncate_scalar

    return (
        df.select(field)
        .drop_nulls()
        .unique(maintain_order=True)
        .head()
        .with_columns(truncate)[field]
        .to_list()
    )


def describe_dataframe(
    df: pl.DataFrame,
    n: int = 6,
    max_chars: int = 100,
    list_n: int = 3,
) -> dict:
    # Ensures deterministic ordering
    ordered_df = df.sort(df.columns)
    return {
        "shape": df.shape,
        "fields": {
            field: {
                "dtype": str(dtype),
                "samples": create_field_sample(
                    ordered_df,
                    field,
                    n=n,
                    max_chars=max_chars,
                    list_n=list_n,
                ),
            }
            for field, dtype in zip(df.columns, df.dtypes)
        },
    }


def _snake_case_df_column_names(df: pl.DataFrame) -> pl.DataFrame:
    return df.rename({col: slugify(col, separator="_") for col in df.columns})


def normalize_df(df: pl.DataFrame) -> pl.DataFrame:
    return _snake_case_df_column_names(df).with_columns(
        pl.col(pl.Decimal).cast(pl.Float64)
    )
