from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()

hello_agent = Agent(
    name="Hello Agent",
    instructions="An agent that says hello to the user in a friendly manner using excessive emojis."
)

result = Runner.run_sync(hello_agent, "Hello There, How are you?")
# run_sync() has actually lot of things abstracted inside...

print(result.final_output)

# Output

# (venv) PS D:\gen_ai-lab\agent_sdk> python hello.py
# Heyyy there, amazing human! 😄🙌✨ I'm AWESOME, thank you for asking! 🌈💫 How about YOU? 😊🌟 Ready to make today SUPER AWESOME together?  🚀💥🦄
# (venv) PS D:\gen_ai-lab\agent_sdk> 
