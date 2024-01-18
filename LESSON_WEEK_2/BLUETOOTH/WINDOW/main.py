import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("B8:27:EB:0E:F2:0D",1))

try:
    while True:
        msg = input("Enter msg: ")
        client.send(str(msg).encode("utf-8"))
        data = client.recv(1024)
        if not data:
            break
            
        print(f"msg: {data.decode('utf-8')}")

except OSError as e:
    pass

client.close()