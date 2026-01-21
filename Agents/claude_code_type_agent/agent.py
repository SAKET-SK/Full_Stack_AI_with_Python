# Chain of Thought Prompting:
# In chain-of-thought prompting, we encourage the model to generate intermediate reasoning steps before arriving at a final answer.
# This technique helps the model to break down complex problems into smaller, manageable parts, leading to

from dotenv import load_dotenv
from openai import OpenAI
import json
import requests
from pydantic import BaseModel, Field
from typing import Optional
import os

load_dotenv()   

client = OpenAI()

def run_command(command: str):
    result = os.system(command)
    return result

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)      # Making a GET request to the URL

    if response.status_code == 200:
        return f"The weather in the {city} is {response.text}"
    
    return "Something went wrong. Please try again."

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command
}

SYSTEM_PROMPT = """
    You are expert logical reasoner and problem solver and part time trip planner.
    You excel at resolving user problems by breaking them down into clear, manageable steps.
    When presented the question, you will first THINK about the best solution. The THINKING process can be 
    of multiple steps. After you have thought through the problem, you will then provide the final ANSWER.
    If needed, you can also call the tools to help you solve the problem, from the list of given tools.

    You must respond using the following structured format:

    OUTPUT JSON FORMAT:
{
  "step": "START | PLAN | TOOL | OUTPUT",
  "content": "string",
  "tool": "string (only if step = TOOL)",
  "input": "string (only if step = TOOL)"
}

Guidelines:
- START: Briefly restate the user's problem.
- PLAN: Explain your approach at a high level (do NOT reveal private chain-of-thought, keep it concise).
- TOOL: Use this when you want to call a tool.
- OUTPUT: Provide the final answer to the user.

Available tools:
- get_weather(city: str): Returns weather for a city.
- run_command(command: str): Undertands and executes a shell command

Rules:
- Do reveal your steps during chain-of-thought reasoning.
- PLAN should be short and helpful.
- OUTPUT should be clean and user-facing.

Example:

User: What is the weather in Mumbai?

Assistant:
{ "step": "START", "content": "The user is asking for the weather in Mumbai." }
{ "step": "PLAN", "content": "I should use the weather tool to fetch the current weather." }
{ "step": "TOOL", "tool": "get_weather", "input": "Mumbai" }

(After tool runs)

Assistant:
{ "step": "OUTPUT", "content": "The weather in Mumbai is sunny and 30°C." }
"""

print("\n\n\n")

# Writing Output Schema:
# The output schema is a JSON object that defines the structure of the output from the tool.

class MyOutPutFormat(BaseModel):
    step: str = Field(..., description="The step of the output.")
    content: Optional[str] = Field(None, description="The optional content of the output.")
    tool: Optional[str] = Field(None, description="The optional tool name of the output.")
    input: Optional[str] = Field(None, description="The optional input of the output.")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

while True:
    user_query = input("> ")
    message_history.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.parse(
            model="gpt-4.1-mini",
            response_format=MyOutPutFormat,        
            messages=message_history
        )

        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})

        
        parsed_result = response.choices[0].message.parsed

        if parsed_result.step == "START":
            print("👉", parsed_result.content)
            continue

        if parsed_result.step == "PLAN":
            print("🧠", parsed_result.content)
            continue

        if parsed_result.step == "TOOL":
            tool_name = parsed_result.tool
            tool_input = parsed_result.input
            print(f"🛠️ calling {tool_name} : ({tool_input})")

            tool_response = available_tools[tool_name](tool_input)

            message_history.append({"role": "developer", "content": json.dumps(
                {
                    "step": "OUTPUT",
                    "content": tool_response
                }
            )})
            continue

        if parsed_result.step == "OUTPUT":
            print("🔮", parsed_result.content)
            break


