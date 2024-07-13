import flet as ft

def app_view(page):
    app_content = ft.Column(
        [
            ft.Text("Bienvenido a la aplicación!", size=30),
            # Aquí puedes agregar más contenido para tu aplicación
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return ft.View(
        "/app",
        [app_content],
        bgcolor='white',
    )
