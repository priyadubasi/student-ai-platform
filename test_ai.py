from app.services.ai_service import ask_ai


question = "Explain machine learning in simple words."

answer = ask_ai(question)

print("AI Response:")
print(answer)