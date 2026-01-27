##### RAG PHASE 2 : RETRIEVAL #####
# In this phase of RAG, we chat with the RAG System with the questions around the document.
# Here our LLM retrieves the most relevant chunks, taking in context the user query and then generates a response

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

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

# Take user input

user_query = input("Shoot me with your questions: >>   ")

# Do the similarity search - Returns relevant chunks from the vector db
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" 
for result in search_results])

SYSTEM_PROMPT = """
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
        {'role':'user', 'content': user_query}
    ]
)

print(f"🔮: {response.choices[0].message.content}")
