import socket

#Basic TCP Client
proto = input("1 for TCP, 2 for UDP")

target_host = "www.google.com"
target_port = 80

def tcpinit():
#create a socket obj
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the client
    client.connect((target_host,target_port))

#Data -> 
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# <- Data
    response = client.recv(4096)

    print(response.decode())
    client.close()

def udpinit():
#create a socket obj
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Data -> 
    client.sendto(b"DAATAAA",(target_host,target_port))
# <- Data
    data, addr = client.recvfrom(4096)

    print(data.decode())
    client.close()

    

if proto == "1":
    tcpinit()
elif proto == "2":
    udpinit()
else:
    exit()




