# Hosted tools
# OpenAI offers a few built-in tools when using the OpenAIResponsesModel:

# The WebSearchTool lets an agent search the web.
# The FileSearchTool allows retrieving information from your OpenAI Vector Stores.
# The CodeInterpreterTool lets the LLM execute code in a sandboxed environment.
# The HostedMCPTool exposes a remote MCP server's tools to the model.
# The ImageGenerationTool generates images from a prompt.

# Function tools
# You can use any Python function as a tool. The Agents SDK will setup the tool automatically:

# The name of the tool will be the name of the Python function (or you can provide a name)
# Tool description will be taken from the docstring of the function (or you can provide a description)
# The schema for the function inputs is automatically created from the function's arguments
# Descriptions for each input are taken from the docstring of the function, unless disabled
# We use Python's inspect module to extract the function signature, along with griffe to parse docstrings and pydantic for schema creation.

from dotenv import load_dotenv
from agents import Agent, Runner
from agents import WebSearchTool, function_tool
import requests

load_dotenv()

@function_tool
def get_weather(city: str):
    """
    Fetch the weather for a given city

    Args:
        city: The name of the city to fetch the weather for.
    """
    url=f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    
    return "Something went wrong"

hello_agent = Agent(
    name="Hello Agent",
    instructions="An agent that says hello to the user in a friendly manner using excessive emojis.",
    tools=[
        WebSearchTool(),    # Hosted Tool
        get_weather         # Function Tool
    ]
)

result = Runner.run_sync(hello_agent, "Can you tell me aout the weather in Pune?")


print(result.final_output)

# Output:

# (venv) PS D:\gen_ai-lab\agent_sdk> python .\agent_with_tools.py
# Hello there!  (づ｡◕‿‿◕｡)づ Welcome! Happy to help you out with tons of smiles and excitement!  (＾▽＾) 

# You're asking about **Saket Khopkar**—let's find out who that is. After searching the web, here's what I’ve discovered:

# • **Professional profile**  
#   There is a personal portfolio website for someone named Saket Khopkar who describes himself as a **developer and designer**. He writes that he tackles real-world problems creatively using classical strategies combined with modern technologies. His experience spans software development using Java, HTML, CSS, C#, and C++, along with research, design, implementation, testing, and evaluation of software solutions.([saket-sk.github.io](https://saket-sk.github.io/?utm_source=openai))  

# • **Contact and location details**
#   The portfolio provides contact information suggesting he’s based in **Yavatmal, Maharashtra, India**, with a listed email address and physical address mentioned.([saket-sk.github.io](https://saket-sk.github.io/?utm_source=openai))

# ---

# So from what is publicly available, **Saket Khopkar appears to be an Indian software developer and designer**, likely early in his career (possibly a diploma holder), involved in tech projects and eager to embrace new technologies through creative problem-solving.

# If you were thinking of a different person with that name—say, in academia, entertainment, or another field—feel free to clarify, and I’d be happy to look deeper!  (⁀ᗢ⁀)
# (venv) PS D:\gen_ai-lab\agent_sdk> 

