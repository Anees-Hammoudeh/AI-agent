import os
from google.genai import types

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        # Get absolute paths for both working directory and target file
        abs_working = os.path.abspath(working_directory)
        abs_file = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if file path is inside the working directory
        if not abs_file.startswith(abs_working):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Check if the path points to an existing directory
        if os.path.isdir(abs_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Create any missing parent directories
        os.makedirs(os.path.dirname(abs_file), exist_ok=True)

        # Write content to the file
        with open(abs_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path of the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
