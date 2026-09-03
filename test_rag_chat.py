from app.rag.rag_service import ask_rag


question = "What is a stack?"

answer = ask_rag(question)

print("\nANSWER:\n")

print(answer)