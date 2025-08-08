import flet as ft
import socket
import threading as th
buttons_sizes = 90
button_bgcolor = ft.CupertinoColors.QUATERNARY_LABEL

def main(page: ft.Page):
    th1.start()
    page.title = "Controle ESP32"
    page.theme_mode = ft.ThemeMode.DARK
    largura_tela = page.width
    altura_tela = page.height
    print(altura_tela)

    def move_right(e):
        socket_send("right")
    def move_up(e):
        socket_send("forward")
    def move_left(e):
        socket_send("left")
    def move_down(e):
        socket_send("backward")

    def update_slider(e):
        socket_send("power", round(slider.value))
        print(round(slider.value))

    right_arrow = ft.IconButton(ft.Icons.KEYBOARD_ARROW_RIGHT_SHARP, on_click=move_right, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)
    left_arrow = ft.IconButton(ft.Icons.KEYBOARD_ARROW_LEFT_SHARP, on_click=move_left, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)

    down_arrow = ft.IconButton(ft.Icons.ARROW_DOWNWARD, on_click=move_down, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)
    up_arrow = ft.IconButton(ft.Icons.ARROW_UPWARD, on_click=move_up, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)    

    slider = ft.Slider(min=0, max=100, on_change=update_slider, label="{value}%", width=largura_tela - 60)

    page.add(
        ft.Container(
            content=ft.Row([slider], alignment=ft.MainAxisAlignment.CENTER),
            margin=ft.margin.only(top=altura_tela - 770)
        ),
        ft.Container(
            expand=True,
            alignment=ft.alignment.bottom_center,
            border=ft.border.all(0.8, ft.CupertinoColors.QUATERNARY_LABEL)
        ),
        ft.Container(
            expand=False,
            alignment=ft.alignment.bottom_center,
            content=ft.Row([up_arrow], alignment=ft.MainAxisAlignment.CENTER),
        ),
        ft.Container(
            expand=False,
            alignment=ft.alignment.bottom_center,
            margin=ft.margin.only(bottom=20, top=1),
            content=ft.Row([left_arrow, down_arrow, right_arrow], ft.MainAxisAlignment.CENTER),
        )
    )

def socket_setup(Host, Port):
    global s
    try:
        s = socket.socket()
        s.connect((Host, Port))
        print(f"Connected with {Host}:{Port}")
    except Exception as e:
        print(e)

def socket_send(dir,power=0):
    match dir:
        case "forward":
            s.sendall(dir.encode())
            print(f"Sended {dir}")
        case "backward":
            s.sendall(dir.encode())
        case "left":
            s.sendall(dir.encode())
        case "right":
            s.sendall(dir.encode())
        case "power":
            s.sendall(f"{dir}/{power+100}".encode())
        case _:
            print("Invalid direction")

def sockets_func():
    socket_setup("127.0.0.1", 64000)
    
th1=th.Thread(target=sockets_func)
ft.app(target=main)
