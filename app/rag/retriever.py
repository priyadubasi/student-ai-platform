from langchain_chroma import Chroma

from app.rag.embeddings import get_embeddings


def get_retriever():

    embeddings = get_embeddings()

    vector_store = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

    return retriever