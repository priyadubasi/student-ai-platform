from langchain_ollama import ChatOllama

from app.rag.retriever import get_retriever


def ask_rag(question):

    retriever = get_retriever()

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    llm = ChatOllama(
        model="llama3.2"
    )

    prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the information
provided in the context below.

If the answer is not available in the context,
say:

"I could not find the answer in the provided document."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content