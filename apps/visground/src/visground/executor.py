from typing import Any, Type


def pyexecute(
    code: str,
    context: dict[str, Any] | None = None,
    expected_type: Type[Any] | tuple[Type[Any], ...] | None = None,
    result_name: str = "result",
) -> Any:
    globals_dict = {"__builtins__": __builtins__}
    locals_dict = dict(context or {})

    compiled = compile(code, "<dynamic>", "exec")
    exec(compiled, globals_dict, locals_dict)

    if result_name not in locals_dict:
        raise ValueError(f"Code must assign `{result_name}`")

    result = locals_dict[result_name]

    if expected_type is not None and not isinstance(result, expected_type):
        raise TypeError(f"Expected {expected_type}, got {type(result)}")

    return result
