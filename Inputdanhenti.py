#Input IP dan Port server secara dinamis

ip_server = input("Masukkan IP Server: ")

port_server = int(input("Masukkan Port Server: "))

#Membuat socket UDP

socketClient socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Koneksi ke server

socketClient.connect((ip_server, port_server))

#Pengiriman pesan berulang dan penghentian otomatis

count = 1

while True:

pesan f"Data ke-{count}"

socketClient.send(pesan.encode())

print("Mengirim:", pesan)

time.sleep(1)

count += 1

#Memeriksa perintah berhenti

stop input("Ketik 'stop' untuk menghentikan pengiriman: ")

if stop.lower() == "stop":

print("Pengiriman dihentikan oleh pengguna.")

break
