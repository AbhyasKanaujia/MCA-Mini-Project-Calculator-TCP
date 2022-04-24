import socket


# This function is used to remove leading zeros from the expression eg. 02+006 = 2 + 6
def sanitizeExpression(exp):
    op = "+-*/%"
    opIndex = []
    clean = ''

    for i in range(len(exp)):
        if exp[i] in op:
            opIndex.append(i)
    opIndex.append(len(exp))

    k = 0
    i = 0
    # if 0 present then remove
    while i < len(exp):
        if exp[i] == '0' and i != opIndex[k] - 1:
            i += 1
            continue
        else:
            clean = clean + exp[i:opIndex[k] + 1]
            i = opIndex[k]
            k += 1
        i += 1

    # return clean expression
    return clean


# get the hostname
host = socket.gethostname()
port = 5000

# print sever status
print("Server is up and running...")

# get the instance of socket
server = socket.socket()

# bind the socket to the host and port
server.bind((host, port))

# listen for 10 conncurrent connections
server.listen(10)

# Display status
print("listening to 10 concurrent requests...")
print("-----------------------------------")


while True:
    # wait for connection from client
    conn, addr = server.accept()
    # Dispaly client address
    print("Received Request from: ", addr)
    # get data from client
    data = conn.recv(1024).decode()
    # display client message
    print("Request Received: ", data)
    # sanitize the expression
    data = sanitizeExpression(data)
    # display sanitized expression
    print("After Sanitization: ", data)

    result = ""
    # Attempt evaluation of expression
    try:
        if(data != ""):
            # return result
            result = eval(data)
    except Exception as e:
        # if error then return Invalid
        result = "Invalid Expression!!"
    # send result to client
    print("Sending reply: ", result)

    # encode the data and send to the client
    conn.send(str(result).encode())
    # close connection with client
    conn.close()
    # Display status
    print("Connection Closed")
    print("-----------------------------------")
