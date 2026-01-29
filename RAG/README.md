To run the docker compose:

```
PS D:\gen_ai-lab\RAG> docker compose up -d
time="2026-01-27T22:30:35+05:30" level=warning msg="No services to build"
PS D:\gen_ai-lab\RAG>
```

Make sure you have docker desktop up and running on your system.

Information about the code files:
- The file "index.py" implements the Indexing Phase of RAG whereas the file "chat.py" implements the Retrieval Pahse of RAG.
- Indexing phase consists of users uploading the documents, chunk them and store them into Vector Databases. Retrieval phase kicks off when user tries to chat with the Chatbot around the uploaded documents.
- We are going to use Qdrant as a Vector Database. Simple andeasy to setup via Docker as instructed. You may view the logs in Docker Desktop and visit the UI of Qdrant to view the collection once created by executing "index.py". Later run "chat_py". Collection plays a vital role in here.
- Run this server before running code from "RAG_Queues" folder.
