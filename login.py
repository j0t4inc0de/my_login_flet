import flet as ft

def main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.title = "Login"
    
    # Agregar imagen de fondo
    bg_image = ft.Image(src="assets/fondo_login.png", fit=ft.ImageFit.COVER, width=page.window.width, height=page.window.height)
    page.add(bg_image)

    login_text = ft.Text("Login", color='black', size=40, weight=ft.FontWeight.BOLD)
    username = ft.TextField(label="Usuario", border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")
    password = ft.TextField(label="Contrseña",password=True, border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")

    c1_container = ft.Container(
        content=login_text,
        alignment=ft.alignment.bottom_center,
        padding=10,
    )
    c1_username = ft.Container(
        content=username,
        alignment=ft.alignment.bottom_center,
        padding=5,
    )
    c1_password = ft.Container(
        content=password,
        alignment=ft.alignment.bottom_center,
        padding=5,
    )
    c1_br = ft.Container(
        content=ft.Text(" "),
        alignment=ft.alignment.bottom_center,
        padding=10
    )
    c1_columna = ft.Column(
        [   
            ft.Container(expand=True),
            c1_container,
            c1_username,
            c1_password,
            ft.FilledButton(
                "Log in",
                width=300,
                height=40,
                style=ft.ButtonStyle(
                    color="#f0f0f0",
                    bgcolor="#1C2120",
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
            ),
            c1_br
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    # Añadir el formulario encima de la imagen de fondo
    overlay = ft.Container(
        content=c1_columna,
        alignment=ft.alignment.center,
        margin=20
    )
    page.overlay.append(overlay)
    page.update()

ft.app(target=main, assets_dir="assets")