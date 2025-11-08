import socket, threading, time
from datetime import datetime

socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketServer.bind(("0.0.0.0", 12345))
print("Server menunggu pesan dari client...\n")

def func(number):
    data, addr = socketServer.recvfrom (1024)
    pesan = data.decode()
    waktu = datetime.now().strftime("%H:%M:%S")
    print(f"[{waktu}] User-{number} ({addr[0]}): {pesan}")
    time.sleep(1)
    print(f"[{waktu}] Selesai memproses data dari User-{number}\n")

nomer = 0
while True:
    nomer += 1
    t = threading.Thread(target=func, args=(nomer,))
    t.start()
