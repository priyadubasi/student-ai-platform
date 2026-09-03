from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents
from app.rag.vector_store import create_vector_store


documents = load_documents()

chunks = split_documents(documents)

print("Creating vector database...")

vector_store = create_vector_store(chunks)

print("Vector database created successfully!")

print("Total chunks stored:", len(chunks))