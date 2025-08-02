import socket

def start_socket_server(qa_chain, host='localhost', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"[Server started on {host}:{port}]")

        conn, addr = s.accept()
        with conn:
            print(f"[Connected by {addr}]")
            while True:
                question = conn.recv(4096).decode()
                if question.lower() in ['exit', 'quit']:
                    break
                answer = qa_chain.run(question)
                conn.sendall(answer.encode())
