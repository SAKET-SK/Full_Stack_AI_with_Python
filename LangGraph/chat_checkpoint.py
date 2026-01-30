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
            "thread_id": "saket"
        }
    }

    # Running the graph -> need to pass the initial state
    updated_state = graph_with_checkpointer.invoke(
        State({"messages": ["Hello, Good Day!"]}),
        config,
    )
    
    print("Final State:", updated_state)

# Checkpointer:
# Under (saket) -> "Hello, Good Day!"
