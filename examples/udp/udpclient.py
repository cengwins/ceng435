import socket
import time

# You have to set the ip address of the server if you do not use docker compose
serverAddressPort   = ("server", 8000)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
i = 0
while (True):
    i = i + 1
    msgFromClient       = "Hello UDP Server" + str(i) 
    bytesToSend         = str.encode(msgFromClient)
# Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    # Note that this is a blocking implementation if server does not echo, you will be blocked
    # Therefore, your client may end up in a deadlock! especially if you add tc commands!
    msg = "{}".format(msgFromServer[0])

    print(msg)
    time.sleep(1)