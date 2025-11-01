import socket

import time

#Membuat socket UDP

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Koneksi ke server

socketClient.connect(("127.0.0.1", 12345))

# Mengirim pesan berulang

for i in range(5):

pesan = "Data ke-" + str(i + 1)

socketClient.send(pesan.encode())

print("Mengirim:", pesan)

time.sleep(1) # jeda 1 detik setiap kirim
