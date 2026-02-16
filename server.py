import socket

# IP -> MAC table (ARP table)
arp_table = {
    "192.168.1.1": "AA:BB:CC:DD:EE:01",
    "192.168.1.2": "AA:BB:CC:DD:EE:02",
    "192.168.1.10": "AA:BB:CC:DD:EE:10",
}

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("ARP Server started...")
conn, addr = server.accept()
print("Client connected:", addr)

while True:
    ip = conn.recv(1024).decode().strip()
    if not ip or ip.lower() == "exit":
        break

    mac = arp_table.get(ip, "MAC NOT FOUND")
    conn.send(mac.encode())

conn.close()
server.close()
print("Server stopped.")