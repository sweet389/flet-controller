import socket
def socket_setup():
    global s
    HOST, PORT = "192.168.0.201", 64000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting")
    global conn, addr
    conn, addr = s.accept()
    print(f"Connected with {addr}")
def socket_recv():
    data=conn.recv(1024)
    data=data.decode()
    if data:
        print(data)
def main():
    socket_setup()
    for x in range(0,11):
        socket_recv()
main()