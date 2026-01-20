from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()

client = Client(
    host="http://localhost:11434",     # here is where your Ollama must be up and running
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Above is the bare minimum setup for a FastAPI server, you may create new routes.

@app.get("/contact-us")
async def contact_us():
    return {"message": "Contact us page"}

@app.post("/chat")     # Registering a route
def chat(
        message: str = Body(..., description="The Message")
):
    response = client.chat(model="gemma:2b", messages=[
        {"role": "user", "content": message}
    ])

    return {"response": response.message.content}
