import flet as ft
from traducciones import traducciones

class TPolicia:
    def __init__(self, page: ft.Page):
        self.page = page
        self.lang = "en" #Detecta el idioma segun el sistema
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

        self.content_area = ft.Column()
        self.page.add(self.language_dropdown, self.content_area)
        self.build_dashboard()

    def change_language(self, e):
        
        self.lang = e.control.value
        self.t = traducciones.get(self.lang, traducciones["en"])
        self.build_dashboard()

    def create_button(icon: str, label_key: str) -> ft.Container:
            return ft.Container(
                content=ft.Column([
                    ft.Icon(name=icon, size=40, color="white"),
                    ft.Text(self.t[label_key], color="white", size=16, weight="bold")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                width=160,
                height=120,
                bgcolor="#1b3b5b",
                border_radius=10,
                alignment=ft.alignment.center,
                ink=True,
                on_click=lambda e: print(f"{self.t[label_key]} clicked"),
            )
    
    def build_dashboard(self):
        #Limpia el contenido actual
        self.content_area.controls.clear()

        buttons = [
            self.create_button("gamepad", "DISPATCH"),
            self.create_button("fingerprint", "CITIZEN SEARCH"),
            self.create_button("description", "REPORTS"),
            self.create_button("directions_car", "VEHICLES"),
            self.create_button("gavel", "CRIMINAL CODE"),
            self.create_button("search", "SEARCH AND CAPTURE"),
            self.create_button("account_balance_wallet", "DEBTORS"),
            self.create_button("gavel", "FEDERAL MANAGEMENT"),
            self.create_button("badge", "AGENT MANAGEMENT"),
            self.create_button("videocam", "SECURITY CAMERAS"),
        ]

        self.content_area.controls.append(
            ft.Text(self.t["on_duty"], size=24, color="white")
        )
        
        self.content_area.controls.append(
             ft.GridView(
                  runs_count=4,
                max_extent=200,
                child_aspect_ratio=1.3,
                spacing=15,
                run_spacing=15,
                controls=buttons
            )
        )

        self.page.update()

ft.app(target=TPolicia)
