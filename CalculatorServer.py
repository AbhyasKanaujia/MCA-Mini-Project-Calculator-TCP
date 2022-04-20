import socket
import re


host = socket.gethostname()
port = 5000
print("Server is up and running...")

server = socket.socket()

server.bind((host, port))
server.listen(10)
print("listening to 10 concurrent requests...")


while True:
    conn, addr = server.accept()
    print("Received Request from: ", addr)
    data = conn.recv(1024).decode()
    # print("Request Received: ", data)
    # data = re.sub(r'\b0+(?!\b)', '', data)
    # print("After Sanitization: ", data)

    result = ""
    try:
        if(data != ""):
            result = round(eval(data), 2)
    except Exception as e:
        result = "Invalid Expression!!"
    print("Sending reply: ", result)

    conn.send(str(result).encode())
    conn.close()
    print("Connection Closed")
    print("-----------------------------------")
