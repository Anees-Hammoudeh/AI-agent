from collections.abc import Callable
from google.genai import types

from functions.get_files_info import get_files_info,schema_get_files_info
from functions.get_file_content import get_file_content,schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_file import run_python_file,schema_run_python_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)

function_map: dict[str, Callable[..., str]] = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
}


def call_function(function_call: types.FunctionCall, verbose: bool = False) -> types.Content:
    function_name = function_call.name or ""

    # 1. print debug info
    if verbose:
        print(f"Calling function: {function_name}({function_call.args})")
    else:
        print(f" - Calling function: {function_name}")

    # 2. validate function
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    # 3. copy args safely
    args = dict(function_call.args) if function_call.args else {}

    # force working directory (IMPORTANT)
    args["working_directory"] = "./calculator"

    # 4. call the function
    try:
        function_result = function_map[function_name](**args)
    except Exception as e:
        function_result = f"Error: {str(e)}"

    # 5. return tool response
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
