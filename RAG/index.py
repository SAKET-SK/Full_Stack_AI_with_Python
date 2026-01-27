# We will create a RAG system to chat with the user with questions around PDF is same folder.
# Here is a starter code

##### RAG PHASE 1 : INDEXING #####
# In this phase of RAG we upload the douments, chunk them and store their embeddings in Vector Database

# index.py is the file that is responsible for indexing of data.

from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders.pdf import PyPDFLoader      # Step 1 : for loading PDF
from langchain_text_splitters import RecursiveCharacterTextSplitter   # Step 2 : To be used for chunking
from langchain_openai import OpenAIEmbeddings                         # Step 3 : To be used for creating embeddings for our chunks
from langchain_qdrant import QdrantVectorStore                      # Setting up our Qdrant vector store

load_dotenv()

pdf_path = Path(__file__).parent / "Python Programming.pdf"

# Load this file into Python Program
# A loader is a utility function provided by LangChain community which basically loads a PDF file.
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# print(docs[15])  # Page by page reading - Testing successful

# Time to split the document in smaller chunks
# overlap = a basic context or recap of previous chunk; good for maintaining context while splitting
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
chunk = text_splitter.split_documents(documents=docs)   # Chunking done...

# Next Step : Create Vector Embeddings for these chunks
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunk,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_to_code_RAG"
)

print("Indexing of documents done...")


