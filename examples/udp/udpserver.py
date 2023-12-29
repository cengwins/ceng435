import socket

 
# You have to set your own ip address of eth0 if you do not use docker compose
localIP     = "server"
localPort   = 8000
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")


# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "{}".format(message)
    bytesToSend = str.encode(clientMsg)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    # Note that this is a blocking implementation, no messages from client no action
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)