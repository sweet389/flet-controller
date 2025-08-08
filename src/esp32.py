import socket
def socket_setup():
    global s
    HOST, PORT = "127.0.0.1", 64000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    global conn, addr
    conn, addr = s.accept()
    print(f"Connected with {addr}")
def main():
    socket_setup()
    