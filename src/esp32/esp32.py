import socket
import network
import time
import _thread as th

def wifi_conf(ssid="", passwd="", hostname=''):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(ssid=ssid, password=passwd)
    network.hostname(hostname)
    print(ap.ifconfig()[0])
    return ap.ifconfig()[0]

def socket_setup(ip, port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global running_spinner
    try:
        s.bind((ip, port))
        th.start_new_thread(spinner,(0.15, f" Waiting on {ip}:{port}"))
        running_spinner=True
        s.listen()
        conn, addr=s.accept()
        running_spinner=False
        time.sleep(0.2)
        print("\n[✔]")
        time.sleep(0.5)
        print(f"[*] Connected on: {addr[0]}:{addr[1]}")
        return conn, addr
    except Exception as e:
        print(f"[*] {e}")

def socket_recv(c):
    data=c.recv(2048).decode()
    if not data:
        print("[*] No data recived")
    print(f'[*] Recived: {data}')

def spinner(_time, msg=""):
    simbols = ['-', '\\', '|', '/']
    i=0
    while running_spinner==True:
        try:    
            print("\r[{1}] {0}".format(msg,simbols[i]), end="")
            i = (i + 1) % len(simbols)
            time.sleep(_time)
        except Exception as e:
            print(f"[*] {e}")

running_spinner=False
ip=wifi_conf("birombola", "abacaxiba", "Franco Lindao")
conn,addr=socket_setup(ip, 23)
socket_recv(conn)

