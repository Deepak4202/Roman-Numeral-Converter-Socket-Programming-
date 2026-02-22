import socket
while True:
    s = socket.socket()
    s.connect(("127.0.0.1",4444))
    a = input("Enter number for converting to Roman Number : ")
    s.send(a.encode())
    data = s.recv(1024).decode()
    print("The Roman number for {} = {} ".format(a,data))