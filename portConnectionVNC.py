import socket

HOST = "localhost"
PORT = 80

# Creates a new socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try to connect to the given host and port
if sock.connect_ex((HOST, PORT)) == 0:
    print("Port " + str(PORT) + " is in use") # Connected successfully
else:
    print("Port " + str(PORT) + " is not in use") # Failed to connect because port is in use (or bad host)

# Close the connection
sock.close()