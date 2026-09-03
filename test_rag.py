from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents


documents = load_documents()

print("Number of pages loaded:", len(documents))


chunks = split_documents(documents)

print("Number of chunks created:", len(chunks))


for chunk in chunks[:3]:

    print("\n--- CHUNK ---")

    print(chunk.page_content[:500])