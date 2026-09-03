from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


DOCUMENTS_DIR = Path("documents")


def load_documents():

    documents = []

    for file_path in DOCUMENTS_DIR.glob("*.pdf"):

        loader = PyPDFLoader(
            str(file_path)
        )

        documents.extend(
            loader.load()
        )

    return documents