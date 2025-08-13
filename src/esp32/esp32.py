import socket
import network

def wifi_conf(ssid="", passwd="", hostname=''):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(ssid=ssid, password=passwd)
    network.hostname(hostname)
    return ap.ifconfig()

def socket_setup(ip, port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((str(ip), port))
        s.listen()
        conn, addr=s.accept()
        return conn, addr
    except Exception as e:
        print(f"[*] {e}")
ip=wifi_conf("biloba", "abacaxiba", "Franco Lindao")
socket_setup(ip, 1000)