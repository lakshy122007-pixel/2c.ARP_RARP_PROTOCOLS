# 2c.SIMULATING ARP /RARP PROTOCOLS
## AIM
To write a python program for simulating ARP protocols using TCP.
## ALGORITHM:
## Client:
1. Start the program
2. Using socket connection is established between client and server.
3. Get the IP address to be converted into MAC address.
4. Send this IP address to server.
5. Server returns the MAC address to client.
## Server:
1. Start the program
2. Accept the socket which is created by the client.
3. Server maintains the table in which IP and corresponding MAC addresses are
stored.
4. Read the IP address which is send by the client.
5. Map the IP address with its MAC address and return the MAC address to client.
## PROGRAM - ARP
```
import socket
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
```
## OUPUT - ARP
![alt text](<Screenshot (51).png>)
## PROGRAM - RARP
```
import socket

client = socket.socket()
client.connect(("localhost", 5000))

print("Connected to ARP Server")
ip = input("Enter IP address to get MAC: ")

client.send(ip.encode())
mac = client.recv(1024).decode()

print("MAC Address:", mac)

client.send("exit".encode())
client.close()
```
## OUPUT -RARP
![alt text](<Screenshot (52).png>)
## RESULT
Thus, the python program for simulating ARP protocols using TCP was successfully 
executed.
