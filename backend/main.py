from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    # Simple AI logic (replace with LLM later)
    reply = f"You said: {req.message}"
    return {"reply": reply}
