import socket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 12345)
print("=== Client Chat UDP ===")
username = input("Masukkan username: ")
while True:
    pesan = input("Ketik pesan (atau 'stop' untuk keluar): ")
    if pesan.lower() == "stop":
        print("Program dihentikan.")
        break
   full_msg = f"[{username}] {pesan}"
   socketClient.sendto(full_msg.encode(), server_address)
