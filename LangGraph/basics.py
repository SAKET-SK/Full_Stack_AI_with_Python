# LangGraph is a python library that allows you to build AI Agent workflows using a graph-based approach.

# Traditional workflows contained while loops, if-else conditions etc. In case if you want
# to add even one node to your flow, this code will get messy and unmanageable.
# LangGraph allows you to build such complex workflows using a graph-based approach.

# Install LangGraph using pip
# pip install -U langgraph

# Important concepts in LangGraph:
# 1. Node: A node represents a single unit of work or operation in the workflow
# 2. Edge: An edge represents the connection between two nodes, indicating the flow of data or control
# 3. Graph: A graph is a collection of nodes and edges that defines the overall workflow
# 4. State: State represents the current status of the graph execution, including the values of variables and the progress of nodes.

# When you run a graph, you will give your state as an input.
# The state will be passed to the first node in the graph.
# Each node will perform its operation and update the state accordingly.
# The state will be passed to the next node in the graph.
# The process repeats until the graph is complete.

# Defining State
from typing_extensions import TypedDict    # State is defined using TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages   # Append only specific field in state
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    messages: Annotated[list, add_messages]

# This is a simple node definition
def node_function(state: State):
    print("Inside node_function")
    return {"messages": ["Hello there Buddy!"]}

def samplenode(state: State):
    print("Inside sample node")
    return {"messages": ["Appended message from sample node."]}

# Basically what add_messages will do is, it will append the new messages to the existing messages in the state.
# This is an in-built functionality provided by LangGraph to handle message appending in a convenient way.

# example usage
# state : {"messages": ["Existing message"]}
# node runs : node_function(state)
# output state : {"messages": ["Existing message", "Hello there Buddy!"]}

graph_builder = StateGraph(State)

# Registering a node
graph_builder.add_node("node_function", node_function)   # good practice to give the node a same name as the function
graph_builder.add_node("samplenode", samplenode)

# Working with edges
graph_builder.add_edge(START, "node_function")
graph_builder.add_edge("node_function", "samplenode")
graph_builder.add_edge("samplenode", END)

# Compile the graph
graph = graph_builder.compile()

# Running the graph -> need to pass the initial state
updated_state = graph.invoke(State({"messages": ["Hello, this is the initial message."]}))
print("Final State:", updated_state)

# Output:
# Inside node_function
# Inside sample node
# Final State: {'messages': [HumanMessage(content='Hello, this is the initial message.', additional_kwargs={}, response_metadata={}, id='abc4ce8d-987a-4ad6-9f0f-d294077ac215'), HumanMessage(content='Hello there Buddy!', additional_kwargs={}, response_metadata={}, id='c581e9fa-6914-44c3-a3ce-b48548f50b9a'), HumanMessage(content='Appended message from sample node.', additional_kwargs={}, response_metadata={}, id='60be98d2-be13-4c2b-bb86-c153bc2653b0')]}

# This shows our execution was successful and the state was updated correctly through the nodes in the graph.
# This is a basic example of how to use LangGraph to create a simple workflow.
# You can create much more complex workflows using conditions, loops, parallel execution, etc.