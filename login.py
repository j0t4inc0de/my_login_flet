import flet as ft

def main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.title = "Login"
    
    def iniciar_sesion(e):
        print("\nSe apretó el botón 'Login'")

    def registrar_usuario(e):
        print("\nSe apretó el botón de registro")
        page.views.clear()
        from views.registro import registro_main
        page.go('/registro')

    def contrasena_olvidada(e):
        print("\nSe apretó el botón de 'contraseña olvidada'")

    path_fondo_login = "https://github.com/j0t4inc0de/my_login_flet/releases/download/fondo/fondo_login.png"
    bg_image = ft.Image(src=path_fondo_login, fit=ft.ImageFit.COVER, width=page.window.width, height=page.window.height)
    login_text = ft.Text("Login", color='black', size=40, weight=ft.FontWeight.BOLD)
    username = ft.TextField(label="Usuario", border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")
    password = ft.TextField(label="Contraseña", password=True, border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")

    password_olvidada = ft.TextButton(
        text="¿Se te olvidó la contraseña?",
        on_click=contrasena_olvidada,
        style=ft.ButtonStyle(
            color="#000000",
            bgcolor="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    register_btn = ft.TextButton(
        text="Regístrate",
        on_click=registrar_usuario,
        style=ft.ButtonStyle(
            color="#000000",
            bgcolor="#ffffff",
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    login_btn = ft.FilledButton(
        "Login",
        on_click=iniciar_sesion,
        width=300,
        height=50,
        style=ft.ButtonStyle(
            color="#f0f0f0",
            bgcolor="#1C2120",
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

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
        padding=15,
    )
    c1_columna = ft.Column(
        [
            c1_br,
            c1_container,
            c1_username,
            c1_password,
            login_btn,
            password_olvidada,
            register_btn
        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    stack = ft.Stack(
        [
            bg_image,
            c1_columna
        ],
        width=page.window.width,
        height=page.window.height
    )
    page.add(stack)
    page.update()
ft.app(target=main)