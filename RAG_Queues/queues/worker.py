# Purpose : Take the user query and perform the retrieval operation here.

from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

openai_client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_to_code_RAG",
    embedding=embedding_model
)

def process_query(query:str):
    print("Searching chunks", query)
    search_results = vector_db.similarity_search(query=query)
    
    context = "\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

    SYSTEM_PROMPT = f"""
    You are a helpful assistant that can answer questions about the query asked by the user based on
    the available context retrieved from a PDF file along with page_content and page_number.

    You should only answer the question based on the available context and should be able to navigate the
    user to the exact page number to know more about the answer.

    Context:
    {context}
    """

    response = openai_client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {'role':'system', 'content': SYSTEM_PROMPT},
            {'role':'user', 'content': query}
        ]
    )
    print(f"🔮: {response.choices[0].message.content}")
    return response.choices[0].message.content

#----------------------------------------------------------------------------
# OTHER TERMINAL

# (venv) PS D:\gen_ai-lab> python -m RAG_Queues.main
# INFO:     Started server process [4144]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
# INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
# INFO:     127.0.0.1:62230 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:64049 - "GET /chat HTTP/1.1" 405 Method Not Allowed
# INFO:     127.0.0.1:51345 - "GET /chat HTTP/1.1" 405 Method Not Allowed
# INFO:     127.0.0.1:64150 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:64150 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:64150 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62325 - "POST /chat?query=What%20are%20common%20mathematical%20functions%20in%20Python HTTP/1.1" 200 OK
# INFO:     127.0.0.1:52876 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:52876 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:56911 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:56911 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     Shutting down
# INFO:     Waiting for application shutdown.
# INFO:     Application shutdown complete.
# INFO:     Finished server process [4144]
# (venv) PS D:\gen_ai-lab> python -m RAG_Queues.main
# INFO:     Started server process [18652]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
# INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
# INFO:     127.0.0.1:62658 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62658 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:58609 - "GET /result?job_id=4ec69f3a-3ffe-44b5-ae06-2bd63c85256f HTTP/1.1" 200 OK
# INFO:     127.0.0.1:54436 - "GET /result?job_id=4ec69f3a-3ffe-44b5-ae06-2bd63c85256f HTTP/1.1" 200 OK
# INFO:     127.0.0.1:61904 - "POST /chat?query=Explain%20me%20operators%20in%20Python HTTP/1.1" 200 OK
# INFO:     127.0.0.1:59926 - "GET /result?job_id=6a88aec3-a811-48fb-a5fa-4b6a02ebcea7 HTTP/1.1" 200 OK
# INFO:     127.0.0.1:56823 - "GET /result?job_id=6a88aec3-a811-48fb-a5fa-4b6a02ebcea7 HTTP/1.1" 200 OK
# INFO:     127.0.0.1:62562 - "GET /result?job_id=6a88aec3-a811-48fb-a5fa-4b6a02ebcea7 HTTP/1.1" 200 OK
# INFO:     127.0.0.1:52878 - "POST /chat?query=Explain%20me%20operators%20in%20Python HTTP/1.1" 200 OK
# INFO:     127.0.0.1:49252 - "GET /result?job_id=c42dcaca-5910-4be6-a7be-9a19f26cf6ba HTTP/1.1" 200 OK
# INFO:     127.0.0.1:60140 - "POST /chat?query=Explain%20me%20operators%20in%20Python HTTP/1.1" 200 OK
# INFO:     127.0.0.1:53645 - "GET /result?job_id=5fc6d103-96f9-43da-a8f9-fae8c06f86da HTTP/1.1" 200 OK
# INFO:     127.0.0.1:63180 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:63180 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:64172 - "GET /result?job_id=5fc6d103-96f9-43da-a8f9-fae8c06f86da HTTP/1.1" 200 OK

# ----------------------------------------------------------------------

### Terminal logs

# (venv) PS D:\gen_ai-lab> rq worker --worker-class rq.worker.SimpleWorker
# 16:33:07 Worker 1d0c96392e294a34be6a234e3f4e8650: started with PID 16752, version 2.6.1
# 16:33:07 Worker 1d0c96392e294a34be6a234e3f4e8650: subscribing to channel rq:pubsub:1d0c96392e294a34be6a234e3f4e8650
# 16:33:07 *** Listening on default...
# 16:33:07 Worker 1d0c96392e294a34be6a234e3f4e8650: cleaning registries for queue: default
# StartedJobRegistry cleanup: 6a88aec3-a811-48fb-a5fa-4b6a02ebcea7 Moved to FailedJobRegistry, due to AbandonedJobError, at 2026-01-28 11:03:07.965787+00:00
# StartedJobRegistry cleanup: c42dcaca-5910-4be6-a7be-9a19f26cf6ba Moved to FailedJobRegistry, due to AbandonedJobError, at 2026-01-28 11:03:07.974356+00:00
# 16:33:23 default: RAG_Queues.queues.worker.process_query('Explain me operators in Python') (5fc6d103-96f9-43da-a8f9-fae8c06f86da)
# Searching chunks Explain me operators in Python
# 🔮: The provided context does not contain specific information about operators in Python. To find detailed explanations about operators in Python, you may want to check the sections following the basics of variables and numbers, which are around pages 38-41 in the document "Python Programming.pdf."

# Typically, in Python, operators include:

# - Arithmetic operators (such as +, -, *, /, %, **, //)
# - Comparison operators (such as ==, !=, >, <, >=, <=)
# - Logical operators (and, or, not)
# - Assignment operators (=, +=, -=, etc.)
# - Bitwise operators (&, |, ^, ~, <<, >>)

# If you would like, I can help locate the exact page or section in your document where operators are discussed, or provide explanations and examples on operators based on general Python knowledge. Would you like me to do that?
# 16:33:42 Successfully completed RAG_Queues.queues.worker.process_query('Explain me operators in Python') job in 0:00:18.765730s on worker 1d0c96392e294a34be6a234e3f4e8650
# 16:33:42 default: Job OK (5fc6d103-96f9-43da-a8f9-fae8c06f86da)
# 16:33:42 Result is kept for 500 seconds
    