# 🎓 Student AI Platform

An AI-powered student management and assistance platform built with **FastAPI, PostgreSQL, SQLAlchemy, LangChain, RAG, JWT Authentication, and a simple HTML/CSS/JavaScript frontend**.

## 🚀 Features

* 🔐 User registration and JWT login
* 👥 Role-based access control
* 👨‍🎓 Student CRUD operations
* 🗄️ PostgreSQL database
* 🧩 SQLAlchemy ORM
* ✅ Pydantic validation
* 🤖 AI-powered question answering
* 📚 Retrieval-Augmented Generation (RAG)
* 🔎 Document-based information retrieval
* 🧠 LangChain integration
* 🦙 Ollama / Llama model integration
* 🌐 FastAPI REST APIs
* 💻 Web frontend
* 🛡️ API authentication and authorization
* ❤️ Health-check endpoint
* ⚠️ Error handling and validation

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │      Frontend       │
                    │ HTML/CSS/JavaScript │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       FastAPI       │
                    │      REST APIs      │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        Authentication    Student APIs       RAG APIs
              │                │                │
              ▼                ▼                ▼
             JWT          PostgreSQL       Vector DB
                                               │
                                               ▼
                                         LangChain
                                               │
                                               ▼
                                         LLM / Ollama
```

## 📁 Project Structure

```text
student-ai-platform/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── student.py
│   │   ├── chat.py
│   │   └── user.py
│   │
│   ├── routers/
│   │   ├── students.py
│   │   ├── ai.py
│   │   ├── rag.py
│   │   └── auth.py
│   │
│   ├── schemas/
│   │   ├── student.py
│   │   └── auth.py
│   │
│   ├── services/
│   │   └── student_service.py
│   │
│   └── rag/
│       ├── retriever.py
│       └── rag_service.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## 🛠️ Technologies

| Technology          | Purpose              |
| ------------------- | -------------------- |
| Python              | Backend programming  |
| FastAPI             | REST API development |
| PostgreSQL          | Database             |
| SQLAlchemy          | ORM                  |
| Pydantic            | Data validation      |
| JWT                 | Authentication       |
| LangChain           | LLM/RAG framework    |
| Ollama              | Local LLM execution  |
| Llama 3.2           | Language model       |
| HTML/CSS/JavaScript | Frontend             |
| Uvicorn             | ASGI server          |

## 🔐 Authentication

The platform uses JWT-based authentication.

Main authentication endpoints:

```text
POST /auth/register
POST /auth/login
GET  /auth/me
GET  /auth/admin-only
```

### Roles

```text
student
admin
```

Students can access student information, while administrative operations require an **admin** role.

## 👨‍🎓 Student APIs

```text
GET     /students/
GET     /students/{student_id}

POST    /students/
PUT     /students/{student_id}
PATCH   /students/{student_id}
DELETE  /students/{student_id}
```

### Permissions

```text
GET       → Authenticated users
POST      → Admin
PUT       → Admin
PATCH     → Admin
DELETE    → Admin
```

## 🤖 RAG AI Assistant

The RAG pipeline follows:

```text
Documents
    ↓
Document Loading
    ↓
Text Splitting
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retriever
    ↓
Relevant Context
    ↓
LLM
    ↓
Final Answer
```

The AI assistant is designed to answer questions using information retrieved from the provided documents.

## 🔗 RAG API

```text
POST /rag/ask
```

Example request:

```json
{
    "question": "What is a stack?"
}
```

Example response:

```json
{
    "question": "What is a stack?",
    "answer": "A stack is a linear data structure..."
}
```

## ▶️ Running the Project

### 1. Create virtual environment

```powershell
python -m venv venv
```

### 2. Activate it

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file containing your local configuration.

**Never upload `.env` to GitHub.**

### 5. Start FastAPI

```powershell
uvicorn app.main:app --reload
```

### 6. Open Swagger

```text
http://127.0.0.1:8000/docs
```

### 7. Start frontend

```powershell
python -m http.server 5500 --directory frontend
```

Open:

```text
http://127.0.0.1:5500
```

## ❤️ Health Check

```text
GET /health
```

Example response:

```json
{
    "status": "healthy",
    "message": "Student AI Platform is running"
}
```

## 🔒 Security

The project uses:

* Password hashing
* JWT authentication
* Role-based authorization
* Environment variables for secrets
* Request validation
* HTTP status codes
* Authentication-protected APIs

Sensitive information such as database passwords, JWT secrets, and API keys should never be committed to source control.

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Python backend development
* REST API development
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Authentication
* Authorization
* JWT
* RAG
* LangChain
* Vector databases
* LLM integration
* Frontend/backend integration
* API testing
* Application architecture

## 📌 Future Improvements

Possible future upgrades:

* Student dashboard with analytics
* Admin dashboard
* File/document upload UI
* Conversation history
* Streaming AI responses
* Better frontend design
* Docker deployment
* Cloud deployment
* Automated testing with Pytest
* CI/CD pipeline
* Production database configuration

## 👩‍💻 Project Goal

The goal of this project is to combine **student management** with **AI-powered assistance** into a single full-stack application.

---

**Student AI Platform — FastAPI + PostgreSQL + RAG + LangChain + JWT**
