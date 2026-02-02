from dotenv import load_dotenv
from mem0 import Memory
import os
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "gpt-4o-mini"     
        }
    },
    "graph_store": {
      "provider": "neo4j",
        "config": {
            "url": "YOUR_NEO4J_CONNECTION_URL",
            "username": "neo4j",
            "password": "YOUR_NEO4J_AURA_INSTANCE_PASSWORD"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

# Now we need to chat with the model
# We meed to give every chat message to this memory client.
memory_client = Memory.from_config(config)

while True:
    user_query = input("Enter your query:- ")

    search_memory = memory_client.search(query=user_query, user_id="saket")

    memories = [
        f"ID: {mem.get('id')}\nMemory: {mem.get('memory')}"
        for mem in search_memory.get("results")
    ]

    print("Memories Fetched : ", memories)

    SYSTEM_PROMPT = f"""
        I am providing you with the context about the user: {json.dumps(memories)}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    ai_response = response.choices[0].message.content

    print("AI Response : ", ai_response)

    memory_client.add(
        user_id="saket",   # Need to scope it to the user ID; can be any string, number etc.
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )

    print("Memory has been added successfully...")

# OUTPUT:

# (venv) PS D:\gen_ai-lab\Memory_Agents> python memory.py
# Enter your query:- Hello My name is Saket and I am a Software Engineer, how are you?
# Memories Fetched :  ['ID: 45f846f1-7506-425d-8243-88dcb32a696e\nMemory: Name is Saket']
# AI Response :  Hello Saket! I'm doing great, thank you for asking. How can I assist you today?
# Memory has been added successfully...
# Enter your query:- I build chatbots using Oracle Digital Assistant and specialise in JavaScript, AI and Python.
# Memories Fetched :  ['ID: b8e25915-5121-4afe-9f4f-a81773139be6\nMemory: Is a Software Engineer', 'ID: 45f846f1-7506-425d-8243-88dcb32a696e\nMemory: Name is Saket']
# AI Response :  Great to hear that! With your expertise in Oracle Digital Assistant, JavaScript, AI, and Python, you have a strong foundation for building intelligent and interactive chatbots. If you need any help with chatbot design, integrating AI models, scripting in JavaScript or Python, or optimizing Oracle Digital Assistant flows, feel free to ask! How can I assist you today?
# Memory has been added successfully...
# Enter your query:- 
