# Agents as tools
# In some workflows, you may want a central agent to orchestrate a network of specialized agents, instead of handing off control. You can do this by modeling agents as tools.

from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You translate the user's message to Spanish",
)

french_agent = Agent(
    name="French agent",
    instructions="You translate the user's message to French",
)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish",
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French",
        ),
    ],
)

result = Runner.run_sync(orchestrator_agent, input="Say 'Hello, how are you?' in French.")
print(result.raw_responses)   # You can see all info about tool calls
print(result.final_output)

# Output:
# (venv) PS D:\gen_ai-lab\agent_sdk> python .\agent_as_tool.py
# 'Hello, how are you?' in Spanish is: Hola, ¿cómo estás?
# (venv) PS D:\gen_ai-lab\agent_sdk> python .\agent_as_tool.py
# "Hello, how are you?" in French is: Bonjour, comment ça va ?
# (venv) PS D:\gen_ai-lab\agent_sdk> 
