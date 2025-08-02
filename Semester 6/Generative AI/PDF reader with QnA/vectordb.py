from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

def store_chunks_in_chroma(chunks, persist_directory="./chroma_db"):
    embeddings = OllamaEmbeddings(model="deepseek-r1:8b")
    vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=persist_directory)
    vectordb.persist()
    return vectordb

def load_chroma(persist_directory="./chroma_db"):
    embeddings = OllamaEmbeddings(model="deepseek-r1:8b")
    return Chroma(persist_directory=persist_directory, embedding_function=embeddings)
