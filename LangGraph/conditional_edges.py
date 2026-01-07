from typing import Annotated
from langgraph.graph.message import add_messages   # Append only specific field in state
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from typing import Optional, Literal
from openai import OpenAI

client = OpenAI()

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
    user_query: str
    llm_output: Optional[str]
    is_good_response: Optional[bool]
    messages: Annotated[list, add_messages]

def ai_node(state: State):
    """Second node - uses AI to respond"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": state.get("user_query")}
        ],
    )
    state["llm_output"] = response.choices[0].message.content
    return state

def evaluation_node(state: State) -> Literal["next_node", "end_node"]:
    """Third node - checks the LLM output quality and decides the next step"""
    if True:
        return "next_node"
    
    return "end_node"

# We can also write a node function with any other model, in case if the user is not satisfied with the response.
    
def end_node(state: State):
    return state

graph_builder = StateGraph(State)

# Registering nodes
graph_builder.add_node("ai_node", ai_node)  # NEW: AI node using Groq
graph_builder.add_node("evaluation_node", evaluation_node)

# Working with edges
graph_builder.add_edge(START, "ai_node")
graph_builder.add_conditional_edge("ai_node", "evaluation_node")   # Addding the conditional edge
graph_builder.add_edge("evaluation_node", END)

# Compile the graph
graph = graph_builder.compile()

print("\nGraph compiled successfully")
print("\nGraph Structure: START → ai_node → samplenode → END\n")

initial_message = "Hello! Can you tell me a fun fact about Python programming?"
print(f"\nInitial Message: {initial_message}\n")
updated_state = graph.invoke(State({"messages": [initial_message]}))
print("\nFinal State:", updated_state)