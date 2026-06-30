import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found.")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

client = genai.Client(api_key=api_key)

messages: list[types.Content] = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
]

if args.verbose:
    print(f"User prompt: {args.user_prompt}")

for _ in range(20):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0,
            tools=[available_functions],
        ),
    )

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if not response.function_calls:
        print("Final response:")
        print(response.text)
        break

    function_responses = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, args.verbose)

        if not function_call_result.parts:
            raise Exception("No parts in function call result")
        if function_call_result.parts[0].function_response is None:
            raise Exception("No function response in result")
        if function_call_result.parts[0].function_response.response is None:
            raise Exception("No response in function response")

        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result.parts[0])

    # أضف نتائج الـ functions للـ messages
    messages.append(types.Content(role="user", parts=function_responses))

else:
    print("Error: max iterations reached without final response")
    exit(1)
