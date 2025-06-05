import flet as ft
from traducciones import traducciones

class TPolicia:
    def __init__(self, page: ft.Page):
        self.page = page
        self.lang = page.client_locale[:2] #Detecta el idioma segun el sistema
        self.t = traducciones.get(self.lang, traducciones["en"]) #Traduccion inicial
        self.language_dropdown = None
        self.content_area = None

        self.setup_ui() 

    def setup_ui(self):
        self.page.title = "Police Dashboard"
        self.page.bgcolor = "#0e2a47"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.scroll = ft.ScrollMode.AUTO

        #Dropdown para cambiar el idioma manualmente

        self.language_dropdown = ft.Dropdown(
            value= self.lang,
            options= [
                ft.dropdown.Option("es", "Español"),
                ft.dropdown.Option("en", "English")
            ],
            on_change= self.change_language
        )

        def create_button(icon: str, label: str) -> ft.Container:
            return ft.Container(
                content=ft.Column([
                    ft.Icon(name=icon, size=40, color="white"),
                    ft.Text(label, color="white", size=16, weight="bold")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                width=160,
                height=120,
                bgcolor="#1b3b5b",
                border_radius=10,
                alignment=ft.alignment.center,
                ink=True,
                on_click=lambda e: print(f"{label} clicked"),
            )

        buttons = [
            create_button("gamepad", "DISPATCH"),
            create_button("fingerprint", "CITIZEN SEARCH"),
            create_button("description", "REPORTS"),
            create_button("directions_car", "VEHICLES"),
            create_button("gavel", "CRIMINAL CODE"),
            create_button("search", "SEARCH AND CAPTURE"),
            create_button("account_balance_wallet", "DEBTORS"),
            create_button("gavel", "FEDERAL MANAGEMENT"),
            create_button("badge", "AGENT MANAGEMENT"),
            create_button("videocam", "SECURITY CAMERAS"),
        ]

        page.add(
            ft.Text("POLICE ON DUTY", size=24, color="white"),
            ft.GridView(
                runs_count=4,
                max_extent=200,
                child_aspect_ratio=1.3,
                spacing=15,
                controls=buttons
            )
        )

ft.app(target=TPolicia)
