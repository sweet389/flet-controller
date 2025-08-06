import flet as ft
buttons_sizes = 90
button_bgcolor = ft.CupertinoColors.QUATERNARY_LABEL

def main(page: ft.Page):
    page.title = "Controle ESP32"
    page.theme_mode = ft.ThemeMode.DARK
    largura_tela = page.width
    altura_tela = page.height
    print(altura_tela)

    def move_right(e):
        pass
    def update_slider(e):
        print(round(slider.value))

    right_arrow = ft.IconButton(ft.Icons.KEYBOARD_ARROW_RIGHT_SHARP, on_click=move_right, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)
    left_arrow = ft.IconButton(ft.Icons.KEYBOARD_ARROW_LEFT_SHARP, on_click=move_right, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)

    down_arrow = ft.IconButton(ft.Icons.ARROW_DOWNWARD, on_click=move_right, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)
    up_arrow = ft.IconButton(ft.Icons.ARROW_UPWARD, on_click=move_right, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(15), bgcolor=button_bgcolor), icon_size=buttons_sizes)    

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

ft.app(target=main)
