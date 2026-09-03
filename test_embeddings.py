from app.rag.embeddings import get_embeddings


embeddings = get_embeddings()

vector = embeddings.embed_query(
    "What is a data structure?"
)

print("Embedding created successfully!")

print("Vector length:", len(vector))

print("First 10 values:", vector[:10])