# Defining State
from typing_extensions import TypedDict    # State is defined using TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages   # Append only specific field in state
from langgraph.graph import StateGraph, START, END
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

# P.S you will need openai api key for this example to work. I don't have one.
# I tried to use Groq LLM as an alternative but it its failing with an error right now.
# But this boilerplate code should work once you have the OpenAI API key.

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

llm = ChatOpenAI(
    model="gpt-4.1-mini",   # or gpt-4o, gpt-4.1-mini
    temperature=0.7
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def ai_node(state: State):
    """Second node - uses AI to respond"""
    response = llm.invoke(state["messages"])
    return {
        "messages": [response]
    }

def samplenode(state: State):
    """Third node - adds a final message"""
    print("\nInside sample node")
    return {
        "messages": [AIMessage(content="Appended message from sample node. Workflow complete!")]
    }


graph_builder = StateGraph(State)

# Registering nodes
graph_builder.add_node("ai_node", ai_node)  # NEW: AI node
graph_builder.add_node("samplenode", samplenode)

# Working with edges
graph_builder.add_edge(START, "ai_node")
graph_builder.add_edge("ai_node", "samplenode")
graph_builder.add_edge("samplenode", END)

# Compile the graph
graph = graph_builder.compile()

print("\nGraph compiled successfully")
print("\nGraph Structure: START → ai_node → samplenode → END\n")

initial_message = HumanMessage(content="Hello! Can you tell me a fun fact about Python programming?")

updated_state = graph.invoke({
    "messages": [initial_message]
})

print("\nFinal messages:\n")
for msg in updated_state["messages"]:
    print(f"{type(msg).__name__}: {msg.content}")

