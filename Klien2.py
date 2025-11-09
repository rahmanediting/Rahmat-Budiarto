import socket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("localhost", 12345)
print("Client siap mengirimkan data ke server.")
while True:
      angka = input("Masukkan angka (atau ketik 'stop' untuk keluar): ")
      if angka.lower() == "stop":
         print("Program dihentikan.")
         break
      socketClient.sendto(angka.encode(), server_address)
