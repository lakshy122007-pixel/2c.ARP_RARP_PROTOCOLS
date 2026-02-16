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