import flet as ft

def main(page: ft.Page):
    page.window.width = 375
    page.window.height = 812
    page.title = "Login"
    # page.bgcolor = "#ffffff"

    # Variables
    # path_logo = "assets/icono.png"
    path_fondo_login = "assets/fondo_login1.png"
    # path_logo = "https://private-user-images.githubusercontent.com/119741641/348514845-f887ae47-b72c-4c27-89c6-50542c1b9007.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjA5MzAzNTIsIm5iZiI6MTcyMDkzMDA1MiwicGF0aCI6Ii8xMTk3NDE2NDEvMzQ4NTE0ODQ1LWY4ODdhZTQ3LWI3MmMtNGMyNy04OWM2LTUwNTQyYzFiOTAwNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzE0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDcxNFQwNDA3MzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iYmQzYTk2ZTk0MTkyMjg0ZGQ0NGQxNzAyZDE5Mzc2MjQ3NmM0NzJlODcxZGFmNTkzNjE3YWQ3ODZhYzMyZTY5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.--nWqpqAVlK3CH0te9L3VKi0o99BRUy0uuRscDR-sTA"
    # path_fondo_login = "https://private-user-images.githubusercontent.com/119741641/348506387-a70b684b-3d23-4c5d-a18b-c784bc880eb6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjA5MTA2OTYsIm5iZiI6MTcyMDkxMDM5NiwicGF0aCI6Ii8xMTk3NDE2NDEvMzQ4NTA2Mzg3LWE3MGI2ODRiLTNkMjMtNGM1ZC1hMThiLWM3ODRiYzg4MGViNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDcxM1QyMjM5NTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lMjI4ZTNlMzdiNWIyYjMxNGVmY2JmMGU0OWJiNmYzYmY2MjJmYWNmYTlkNTgyOWQ5NDI0ZjViNDc1MzVjZjgzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.GJ18-jBUArk-7SMJkkDGhPqPYwslGIFlIYhELgRbT0I"
    login_text = ft.Text("Login", color='black', size=40, weight=ft.FontWeight.BOLD)
    username = ft.TextField(label="Usuario", border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")
    password = ft.TextField(label="Contraseña", password=True, border_radius=15, width=300, filled=True, border_color="transparent", bgcolor="#8F8E8E")
    password_olvidada = ft.TextButton(
        text="¿Se te olvido la contraseña?",
        style=ft.ButtonStyle(
        color="#000000",
        bgcolor="#ffffff",
        shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    register_btn = ft.TextButton(
        text="Registrate",
        style=ft.ButtonStyle(
        color="#000000",
        bgcolor="#ffffff",
        shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    login_btn = ft.FilledButton(
        "Login",
        width=300,
        height=50,
        style=ft.ButtonStyle(
            color="#f0f0f0",
            bgcolor="#1C2120",
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
    bg_image = ft.Image(src=path_fondo_login, fit=ft.ImageFit.COVER, width=page.window.width, height=page.window.height)
    
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
    # Crear el stack y añadir los elementos
    stack = ft.Stack(
        [
            bg_image,  # Imagen de fondo
            c1_columna  # Formulario
        ],
        width=page.window.width,
        height=page.window.height
    )
    page.add(stack)
    page.update()

ft.app(target=main)