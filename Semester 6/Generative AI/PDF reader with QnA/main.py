import os

def main():
    pdf_path = "Ch 1 - Management.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return

    from pdf_loader import load_and_split_pdf
    from vectordb import store_chunks_in_chroma, load_chroma
    from qa_chain import create_qa_chain
    from server import start_socket_server

    chunks = load_and_split_pdf(pdf_path)

    # For first time loading PDF
    # vectordb = store_chunks_in_chroma(chunks)
    
    # For loading existing PDF
    # Currently loaded PDF = "Ch 1 - Management.pdf"
    vectordb = load_chroma()
    
    qa_chain = create_qa_chain(vectordb)
    start_socket_server(qa_chain)

if __name__ == "__main__":
    main()