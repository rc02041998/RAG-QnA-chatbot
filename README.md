
# 🧠 RAG API with FastAPI, Ollama (LLaMA 2), and FAISS

This project is a Retrieval-Augmented Generation (RAG) API built using FastAPI. It uses:
-  LLaMA 2 via Ollama as the local LLM
-  LangChain for chaining and document retrieval
-  Dockling is used to extract text from pdf 
-  FAISS for vector similarity search
-  FastAPI for serving a question-answering endpoint

---

## 📁 Project Structure

```
.
├── main.py                # FastAPI app
├── retrieval.py           # QA chain with LLaMA 2 + retriever
├── vector_store.py        # Vector DB loader and creator
├── build_vectorstore.py   # One-time script to build vector DB
├── requirements.txt       # Python dependencies
├── .gitignore
├── README.md
└── data/                  # Folder for PDF documents
```

---

##  Getting Started

### 1. Clone the repo and set up your environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Install and run Ollama with LLaMA 2

```bash
ollama pull llama2
ollama run llama2
```

### 3. Add your PDF documents

Put your IFB/IFPQ or any PDF files in the root or `data/` folder.

### 4. Build the FAISS vector store (run once)

```bash
python build_vectorstore.py
```

### 5. Start the API

```bash
uvicorn main:app --reload
```

### 6. Open Swagger docs

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  Example POST request to `/ask`

```json
POST http://localhost:8000/ask
Content-Type: application/json

{
  "questions": [
    "What are the license requirements?"
  ]
}
```

---

##  Features

- One-time vector DB creation
- Efficient PDF document retrieval
- Local inference using LLaMA 2 via Ollama
- FAISS-powered context search
- Simple and extendable API design

---

## To Do

- [ ] Add file upload support
- [ ] Add streaming responses
- [ ] Enable frontend integration
- [ ] Dockerize for deployment

---

