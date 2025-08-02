import socket

def start_client(host='localhost', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to server. Type 'exit' to quit.")
        while True:
            question = input("Ask: ")
            if question.lower() in ['exit', 'quit']:
                break
            s.sendall(question.encode())
            answer = s.recv(4096).decode()
            print("AI:", answer)

if __name__ == "__main__":
    start_client()