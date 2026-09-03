from app.rag.retriever import get_retriever


retriever = get_retriever()

question = "What is a stack?"

documents = retriever.invoke(question)

print("Relevant documents found:", len(documents))


for i, document in enumerate(documents, start=1):

    print(f"\n--- RESULT {i} ---")

    print(document.page_content[:1000])