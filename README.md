# AI Coding Agent

An autonomous AI coding agent built with Python and Google Gemini. The agent can read, write, and execute files to independently analyze and fix bugs in a codebase — without human intervention.

## How It Works

The agent runs in a loop, continuously calling tools and reasoning about results until it completes the task:

1. User gives a prompt (e.g., "Fix the bug: 3 + 7 * 2 shouldn't be 20")
2. The agent lists and reads relevant files
3. It identifies the root cause of the bug
4. It writes the fix directly to the source file
5. It runs the tests to verify the fix worked
6. It returns a final response to the user

## Features

- List files and directories
- Read file contents
- Write and overwrite files
- Execute Python files with arguments
- Autonomous multi-step reasoning loop
- Verbose mode for debugging

## Setup

1. Clone the repo:
   git clone https://github.com/Anees-Hammoudeh/AI-agent.git
   cd AI-agent

2. Install dependencies:
   uv venv
   source .venv/bin/activate
   uv sync

3. Add your Gemini API key to a `.env` file:
   GEMINI_API_KEY=your_api_key_here

4. Run the agent:
   uv run main.py "your prompt here"

## Usage

Basic usage:
   uv run main.py "How does the calculator render results?"

With verbose output:
   uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20" --verbose

## Project Structure

 AI-agent/
   ├── main.py              # Entry point and agent loop
   ├── call_function.py     # Function dispatcher
   ├── prompts.py           # System prompt
   ├── functions/
   │   ├── get_files_info.py
   │   ├── get_file_content.py
   │   ├── write_file.py
   │   └── run_python_file.py
   └── calculator/          # Sample codebase for the agent to work on

## Warning

This is a learning project. Do not use it in production or give it access to sensitive files. The agent can read, write, and execute arbitrary code within the working directory.

## Built With

- Python
- Google Gemini API (gemini-2.5-flash)
- uv
