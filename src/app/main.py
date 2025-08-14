import flet as ft
import socket
import time

buttons_sizes = 90
button_bgcolor = ft.CupertinoColors.QUATERNARY_LABEL
page=None
def socket_setup(Host, Port):
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((Host, Port))
        print(f"Connected with {Host}:{Port}")
        last_log.value = f"Connected with {Host}:{Port}"
        page.update()
    except Exception as e:
        print(f"ERRO SOCKET: {e}")
        last_log.value = e
        page.update()
        time.sleep(1)
        
def main(p: ft.Page):
    global page
    page=p
    page.title = "Controle ESP32"
    page.theme_mode = ft.ThemeMode.DARK
    largura_tela = page.width
    altura_tela = page.height
    if altura_tela >= 844:
        slider_height=altura_tela-770
    else:
        slider_height=30
    print(f"{largura_tela}x{altura_tela}")

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
    def socket_submit(e):
        socket_setup(ip_text_box.value, port_text_box.value)
    
    right_arrow = ft.IconButton(ft.Icons.KEYBOARD_ARROW_RIGHT_SHARP, on_click=move_right, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)
    left_arrow = ft.IconButton(ft.Icons.KEYBOARD_ARROW_LEFT_SHARP, on_click=move_left, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)
    down_arrow = ft.IconButton(ft.Icons.ARROW_DOWNWARD, on_click=move_down, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)
    up_arrow = ft.IconButton(ft.Icons.ARROW_UPWARD, on_click=move_up, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)    
    slider = ft.Slider(min=0, max=100, on_change=update_slider, label="{value}%", width=largura_tela - 60)

    ip_text_box=ft.TextField(label="IP:", hint_text="127.0.0.1", multiline=False, filled=True, border=ft.InputBorder.OUTLINE, border_radius=12, border_width=0.5, bgcolor=ft.CupertinoColors.TERTIARY_LABEL)
    port_text_box=ft.TextField(label="Port:", multiline=False, filled=True, border=ft.InputBorder.OUTLINE, border_radius=12, border_width=0.5, bgcolor=ft.CupertinoColors.TERTIARY_LABEL)
    submit_button=ft.FilledButton(text="Submit", bgcolor=ft.CupertinoColors.TERTIARY_LABEL, color=ft.CupertinoColors.WHITE, width=100, on_click=socket_submit)
    
    global last_log
    last_log=ft.Text(value="", size=16)

    page.add(
        ft.Container(
            content=ft.Row([slider], alignment=ft.MainAxisAlignment.CENTER),
            margin=ft.margin.only(top=slider_height)
        ),
        ft.Container(
            content=ft.Row(
                controls=[
                        ft.Column(
                        [
                            ip_text_box,
                            port_text_box,
                            submit_button
                        ],
                        width=140,
                        alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Column(
                            [
                                ft.Text(value=f"STATUS{" "*16}", text_align=ft.TextAlign.START, size=25),                                
                                ft.Container(
                                    width=300,     
                                    expand=True,    
                                    bgcolor=ft.CupertinoColors.TERTIARY_LABEL,
                                    border=ft.border.all(1, ft.Colors.BLACK),
                                    border_radius=8,
                                    padding=10,
                                    content=ft.Column([
                                        ft.Row([ft.Text(f"Connection:", size=16), ft.Icon(name=ft.Icons.WIFI,)]),
                                        ft.Row([ft.Text(f"IP:", size=16), ft.Icon(name=ft.Icons.WIFI)]),
                                        ft.Row([ft.Text(f"Port:", size=16), ft.Icon(name=ft.Icons.WIFI)]),
                                        ft.Row([ft.Text(f"Power:", size=16), ft.Icon(name=ft.Icons.WIFI)]),
                                        ft.Row([ft.Text(value="Last Log:", size=16),last_log]),
                                    ],  
                                    alignment=ft.MainAxisAlignment.START,
                                    scroll=ft.ScrollMode.AUTO
                                    ),
                                    
                                ), 
                            ],
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                        alignment=ft.MainAxisAlignment.START,
                        expand=True,
                        )
                ],
            ),
            border=ft.border.all(1.5, ft.CupertinoColors.SYSTEM_INDIGO,),
            border_radius=5,
            expand=True,
            padding=ft.padding.all(8)
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

def socket_send(dir,power=0):
    try:
        match dir:
            case "forward":
                s.sendall(dir.encode())
                print(f"Sended {dir}")
                last_log.value = dir
                page.update()
            case "backward":
                s.sendall(dir.encode())
                print(f"Sended {dir}")
                last_log.value = dir
                page.update()
            case "left":
                s.sendall(dir.encode())
                print(f"Sended {dir}")
                last_log.value = dir
                page.update()
            case "right":
                s.sendall(dir.encode())
                print(f"Sended {dir}")
                last_log.value = dir
                page.update()
            case "power":
                s.sendall(f"p/{power+100}".encode())
                print(f"Sended {dir}={power+100}")
                last_log.value = f"{dir}={power+100}"
                page.update()
            case _: 
                print("Invalid direction")
    except Exception as e:
        print(f"ERRO SOCKET SEND {e}")
        last_log.value = e
        page.update()
        time.sleep(1)
        

ft.app(target=main)
