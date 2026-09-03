
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage


llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

student_assistant_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a helpful AI Student Assistant.

Help students with:
- Academic subjects
- Programming
- Data Science
- Artificial Intelligence
- Machine Learning
- Career preparation
- Placement preparation

Give simple, clear and accurate answers.
"""
    ),
    (
        "human",
        "{question}"
    )
]) 

student_assistant_chain = (
    student_assistant_prompt
    | llm
)

# Store conversation history
chat_histories = {}


def ask_ai(question: str):

    response = student_assistant_chain.invoke({
        "question": question
    })

    return response.content

def chat_with_history(session_id: str, message: str):

    # Create history for a new session
    if session_id not in chat_histories:
        chat_histories[session_id] = []

    history = chat_histories[session_id]

    # Add user's message
    history.append(
        HumanMessage(content=message)
    )

    # Send complete conversation to AI
    response = llm.invoke(history)

    # Add AI response to history
    history.append(
        AIMessage(content=response.content)
    )

    return response.content