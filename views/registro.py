import flet as ft

def registro_main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.title = "Registro"
    # Aquí añades los controles necesarios para el registro de usuario
    register_text = ft.Text("Registro", size=40, weight=ft.FontWeight.BOLD)
    username = ft.TextField(label="Usuario", border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")
    password = ft.TextField(label="Contraseña", password=True, border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")
    register_btn = ft.FilledButton(
        "Registrar",
        width=300,
        height=50,
        style=ft.ButtonStyle(
            color="#f0f0f0",
            bgcolor="#1C2120",
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        on_click=lambda e: print("Usuario registrado")  # Aquí pones la lógica de registro
    )

    page.add(ft.Column(
        controls=[register_text, username, password, register_btn],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    ))
    page.update()
ft.app(target=registro_main)