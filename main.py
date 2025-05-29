from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from retrieval import get_qa_chain
import uvicorn

app = FastAPI(title="RAG Question Answering API")

class QuestionInput(BaseModel):
    questions: List[str]

qa_chain = get_qa_chain()  # Load on startup

@app.post("/ask")
def ask_questions(data: QuestionInput):
    try:
        responses = [qa_chain.run(q) for q in data.questions]
        return {"responses": responses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

