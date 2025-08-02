from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np
import re

app = FastAPI()

# Improved storage structure
documents = {}  # Stores document metadata
chunks = {}     # Stores text chunks with embeddings

# Initialize model
model = SentenceTransformer('all-MiniLM-L6-v2')

def split_into_chunks(text, chunk_size=500, overlap=100):
    """Split text into overlapping chunks for better context"""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(400, "Only PDF files are accepted")
    
    try:
        # Read PDF content
        pdf_reader = PdfReader(file.file)
        full_text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text() or ""
            # Clean up text
            page_text = re.sub(r'\s+', ' ', page_text).strip()
            full_text += page_text + "\n"
        
        # Generate document ID
        doc_id = str(len(documents) + 1)
        
        # Store document metadata
        documents[doc_id] = {
            "filename": file.filename,
            "page_count": len(pdf_reader.pages)
        }
        
        # Split and store chunks
        text_chunks = split_into_chunks(full_text)
        chunks[doc_id] = []
        
        for i, chunk in enumerate(text_chunks):
            embedding = model.encode(chunk).tolist()
            chunks[doc_id].append({
                "text": chunk,
                "embedding": embedding,
                "chunk_id": i
            })
        
        return JSONResponse({
            "message": "PDF processed successfully",
            "document_id": doc_id,
            "chunk_count": len(text_chunks)
        })
    except Exception as e:
        raise HTTPException(500, f"Error processing PDF: {str(e)}")

@app.post("/ask/")
async def ask_question(question: str, document_id: str = None):
    try:
        if not documents:
            return {"answer": "No documents available"}
            
        # If no document_id specified, search all documents
        target_docs = [document_id] if document_id else list(documents.keys())
        
        # Find most relevant chunk across documents
        question_embedding = model.encode(question)
        best_match = None
        best_score = -1
        
        for doc_id in target_docs:
            if doc_id not in chunks:
                continue
                
            for chunk in chunks[doc_id]:
                similarity = np.dot(question_embedding, chunk["embedding"]) / (
                    np.linalg.norm(question_embedding) * np.linalg.norm(chunk["embedding"])
                )
                
                if similarity > best_score:
                    best_score = similarity
                    best_match = {
                        "text": chunk["text"],
                        "document_id": doc_id,
                        "document_name": documents[doc_id]["filename"],
                        "chunk_id": chunk["chunk_id"]
                    }
        
        if not best_match:
            return {"answer": "No relevant information found"}
        
        # Return the complete best matching chunk
        return {
            "answer": best_match["text"],
            "source": f"Document: {best_match['document_name']} (Chunk {best_match['chunk_id']})",
            "confidence": float(best_score),
            "document_id": best_match["document_id"]
        }
    except Exception as e:
        raise HTTPException(500, f"Error answering question: {str(e)}")