# Defining State
from typing_extensions import TypedDict    # State is defined using TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages   # Append only specific field in state
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

# P.S you will need openai api key for this example to work. I don't have one.
# I tried to use Groq LLM as an alternative but it its failing with an error right now.
# But this boilerplate code should work once you have the OpenAI API key.

import os
from dotenv import load_dotenv

load_dotenv()

# Get the API key
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# if not GROQ_API_KEY:
#     raise ValueError("GROQ_API_KEY not found in .env file!")

# print("Groq API Key loaded successfully")

# Initialize Groq chat model
llm = init_chat_model(
    model="gpt-4.1-mini",
    provider="openai",
)

print("Groq LLM initialized")

class State(TypedDict):
    messages: Annotated[list, add_messages]

def ai_node(state: State):
    """Second node - uses AI to respond"""
    response = llm.invoke(state.get("messages"))

def samplenode(state: State):
    """Third node - adds a final message"""
    print("\nInside sample node")
    return {"messages": ["Appended message from sample node. Workflow complete!"]}

graph_builder = StateGraph(State)

# Registering nodes
graph_builder.add_node("ai_node", ai_node)  # NEW: AI node using Groq
graph_builder.add_node("samplenode", samplenode)

# Working with edges
graph_builder.add_edge(START, "ai_node")
graph_builder.add_edge("ai_node", "samplenode")
graph_builder.add_edge("samplenode", END)

# Compile the graph
graph = graph_builder.compile()

print("\nGraph compiled successfully")
print("\nGraph Structure: START → ai_node → samplenode → END\n")

initial_message = "Hello! Can you tell me a fun fact about Python programming?"
print(f"\nInitial Message: {initial_message}\n")
updated_state = graph.invoke(State({"messages": [initial_message]}))
print("\nFinal State:", updated_state)