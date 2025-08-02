from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

def create_qa_chain(vectordb):
    llm = Ollama(model="deepseek-r1:8b")
    retriever = vectordb.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
