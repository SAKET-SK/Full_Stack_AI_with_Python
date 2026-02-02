from dotenv import load_dotenv

from typing_extensions import TypedDict    # State is defined using TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages   # Append only specific field in state
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",   # or gpt-4o, gpt-4.1-mini
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

# This is a simple node definition
def chatbot(state: State):
    print("Inside chatbot")
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}

graph_builder = StateGraph(State)

# Registering a node
graph_builder.add_node("chatbot", chatbot)   

# Working with edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile the graph
graph = graph_builder.compile()

def compile_graph_with_checkpoint(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)

DB_URI = "localhost:27017"    # mongodb://<username>:<password>@<host>:<port>/<database>
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpoint(checkpointer=checkpointer)

    config = {
        "configurable": {
            "thread_id": "saket"    # Can be anything (text,number,etc.), as per your wish
        }
    }

    # Running the graph -> need to pass the initial state
    for chunk in graph_with_checkpointer.stream(
        State({"messages": ["What is my name?"]}),
                config,
                stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()

# Checkpointer:
# Under (saket) -> "Hello, Good Day!"

# OUTPUT

# (venv) PS D:\gen_ai-lab\LangGraph> python chat_checkpoint.py
# ================================ Human Message =================================

# Hello, Good Day!
# Inside chatbot
# ================================== Ai Message ==================================

# Hello again! Hope you're having a great day! How can I help you today?
# (venv) PS D:\gen_ai-lab\LangGraph> ^C
# (venv) PS D:\gen_ai-lab\LangGraph> python chat_checkpoint.py
# ================================ Human Message =================================

# Hello, Good Day! My name is Saket
# Inside chatbot
# ================================== Ai Message ==================================

# Hello Saket! Good day to you! How can I assist you today?
# (venv) PS D:\gen_ai-lab\LangGraph> python chat_checkpoint.py
# ================================ Human Message =================================

# What is my name?
# Inside chatbot
# ================================== Ai Message ==================================

# Your name is Saket. How can I assist you further today?
# (venv) PS D:\gen_ai-lab\LangGraph> 
