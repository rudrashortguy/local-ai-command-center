import time
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/chat")
async def chat(data: dict):
    msg = data.get("message", "Hello")
    return {"response": f"You said: '{msg}'. I'm running offline with mock responses - connect Ollama for real AI."}

@app.post("/summarize-pdf")
async def summarize_pdf(file: UploadFile = File(...)):
    content = await file.read()
    return {"summary": f"Summarized {file.filename} ({len(content)} bytes). Mock summary - connect Ollama for real summaries."}

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    return {"text": "Mock OCR output. Install Tesseract for real OCR.", "confidence": 0.95}

@app.post("/voice-input")
async def voice_input(data: dict = {}):
    return {"text": "Mock voice transcription. Install SpeechRecognition for real voice input.", "confidence": 0.90}

@app.post("/caption-image")
async def caption_image(file: UploadFile = File(...)):
    return {"caption": "A mock caption of the uploaded image. Install BLIP model for real captioning."}

@app.get("/file-search")
async def file_search(q: str = ""):
    return {"results": [{"file": "notes.txt", "snippet": f"...{q}... found in mock index."}]}

@app.post("/rag-query")
async def rag_query(data: dict):
    q = data.get("query", "")
    return {"answer": f"Mock RAG answer for '{q}'. Install ChromaDB + sentence-transformers for real RAG."}
