# Chain of Thought Prompting:
# In chain-of-thought prompting, we encourage the model to generate intermediate reasoning steps before arriving at a final answer.
# This technique helps the model to break down complex problems into smaller, manageable parts, leading to

from dotenv import load_dotenv
from openai import OpenAI
import json
import requests

load_dotenv()   

client = OpenAI()     # Using the openai key, put $7 credts 🥲; Gemini setup with OpenAI is giving rate limit issues, this setup functions effortlessly as expected.

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)      # Making a GET request to the URL

    if response.status_code == 200:
        return f"The weather in the {city} is {response.text}"
    
    return "Something went wrong. Please try again."

available_tools = {
    "get_weather": get_weather
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

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

while True:
    user_query = input("> ")
    message_history.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            response_format={"type": "json_object"},        
            messages=message_history
        )

        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        result = json.loads(raw_result)

        if result.get("step") == "START":
            print("👉", result.get("content"))    # Emojis for better step by step analysis; depends on your call to include them or not.
            continue

        if result.get("step") == "PLAN":
            print("🧠", result.get("content"))
            continue

        if result.get("step") == "TOOL":
            tool_name = result.get("tool")
            tool_input = result.get("input")
            print(f"{tool_name} : ({tool_input})")

            tool_response = available_tools[tool_name](tool_input)

            message_history.append({"role": "developer", "content": json.dumps(
                {
                    "step": "OUTPUT",
                    "content": tool_response
                }
            )})
            continue

        if result.get("step") == "OUTPUT":
            print(result.get("content"))
            break


