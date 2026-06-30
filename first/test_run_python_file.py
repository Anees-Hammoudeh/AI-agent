from functions.run_python_file import run_python_file

# Should print calculator usage
print(run_python_file("calculator", "main.py"))

# Should run calculator with expression
print(run_python_file("calculator", "main.py", ["3 + 5"]))

# Should run calculator tests
print(run_python_file("calculator", "tests.py"))

# Should return error - outside working directory
print(run_python_file("calculator", "../main.py"))

# Should return error - file doesn't exist
print(run_python_file("calculator", "nonexistent.py"))

# Should return error - not a Python file
print(run_python_file("calculator", "lorem.txt"))
