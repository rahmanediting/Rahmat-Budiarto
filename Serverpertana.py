import socket



myp socket.SOCK_DGRAM

afn socket.AF_INET

socketServer = socket.socket(afn, myp)



socketServer.bind(("127.0.0.1", 12345))

print("Server mendengarkan...")



while True:

    clientData = socketServer.recvfrom(1624)

    addrs clientData[1][8]

    msg clientData[6].decode()

    print(addrs +":"+ msg)
