import flet as ft

def main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.title = "Login"
    page.bgcolor = "#ffffff"
    
    # Variables
    fondo_login_link = "https://private-user-images.githubusercontent.com/119741641/348506387-a70b684b-3d23-4c5d-a18b-c784bc880eb6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjA5MTA2OTYsIm5iZiI6MTcyMDkxMDM5NiwicGF0aCI6Ii8xMTk3NDE2NDEvMzQ4NTA2Mzg3LWE3MGI2ODRiLTNkMjMtNGM1ZC1hMThiLWM3ODRiYzg4MGViNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDcxM1QyMjM5NTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lMjI4ZTNlMzdiNWIyYjMxNGVmY2JmMGU0OWJiNmYzYmY2MjJmYWNmYTlkNTgyOWQ5NDI0ZjViNDc1MzVjZjgzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.GJ18-jBUArk-7SMJkkDGhPqPYwslGIFlIYhELgRbT0I"
    login_text = ft.Text("Login", color='black', size=40, weight=ft.FontWeight.BOLD)
    username = ft.TextField(label="Usuario", border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")
    password = ft.TextField(label="Contraseña",password=True, border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")
    
    # Agregar imagen de fondo
    bg_image = ft.Image(src=fondo_login_link, fit=ft.ImageFit.COVER, width=page.window.width, height=page.window.height)
    page.add(bg_image)

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
        padding=10,
    )
    c1_columna = ft.Column(
        [   
            ft.Container(expand=True),
            c1_container,
            c1_username,
            c1_password,
            ft.FilledButton(
                "Login",
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