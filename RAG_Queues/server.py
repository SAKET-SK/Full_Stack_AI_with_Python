from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queues.worker import process_query   # __init__.py is needed; read about it later

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Server up and running"}

# Defining the chat route
@app.post('/chat')
def chat(
        query: str = Query(..., description="The input query for the chatbot from the user")
):
    job = queue.enqueue(process_query, query)   # Enqueues the process_query as processor function; with query as argument
    # Returns the ID of the job, you basically saying, go in the queue, this is your id
    return {"status" : "Queued", "job_id": job.id}

# OUTPUT:
# {
#   "status": "Queued",
#   "job_id": "4ec69f3a-3ffe-44b5-ae06-2bd63c85256f"
# }

# To check status of job, we will create one more route

@app.get('/result')
def get_result(
        job_id: str = Query(..., description="The ID of the job")
):
        job = queue.fetch_job(job_id=job_id)
        result = job.return_value()
        return {"result": result}
