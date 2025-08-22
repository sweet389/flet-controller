import socket
import network
import time
import _thread as th
import machine

pins={
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "pwr": 5
}

def setup():
    global m1,m2,m3,m4,pwr
    try:
        m1=machine.Pin(pins["1"], machine.Pin.OUT)
        m2=machine.Pin(pins["2"], machine.Pin.OUT)
        m3=machine.Pin(pins["3"], machine.Pin.OUT)
        m4=machine.Pin(pins["4"], machine.Pin.OUT)
        pwr=machine.PWM(machine.Pin(pins["pwr"], freq=5000, duty_u16=32768))
        print("AA")
    except Exception as e:
        print(f"[*] {e}")

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
        print("\n[✔]")
        time.sleep(0.5)
        print(f"[*] Connected on: {addr[0]}:{addr[1]}")
        return conn, addr
    except Exception as e:
        print(f"[*] {e}")

def socket_recv(c):
    try:
        data=c.recv(2048).decode()
        if not data:
            print("[*] No data recived")
        print(f'[*] Recived: {data}')
        if data=="forward":
            move(1)
        elif data=="backward":
            move(2)
        elif data=="left":
            move(3)
        elif data=="right":
            move(4)
        elif data.startswith("p/"):
            power(data.split("/")[1])
    except Exception as e:
        print(f"[*] {e}")

def move(dir):
    try:
        if dir=="forward":
            m1.on()
            m2.off()
            m3.on()
            m4.off()
        elif dir=="backward":
            m1.off()
            m2.on()
            m3.off()
            m4.on()
        elif dir=="left":
            m1.off()
            m2.on()
            m3.on()
            m4.off()
        elif dir=="right":
            m1.on()
            m2.off()
            m3.off()
            m4.on()
    except Exception as e:
        print(f"[*] {e}")

def power(p):
    try:
        pwr.duty(map(p,0,1024,0,100))
    except Exception as e:
        print(f"[*] {e}")

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

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
setup()
ip=wifi_conf("birombola", "abacaxiba", "Franco Lindao")
conn,addr=socket_setup(ip, 23)
socket_recv(conn)

