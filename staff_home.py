import flet as ft
def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/staff_home"
        )
    )
    page.bgcolor = "#F5F7FB"
    page.window.width=300
    id=page.session.store.get("staff_id")
    page.session.store.set("id",id)
    fullname=page.session.store.get("staff_name")
    def card(icon, title, subtitle, primary=False):
        return ft.Container(
            width=155, height=115,
            bgcolor="#1E4DB7" if primary else "white",
            border_radius=12,
            padding=12,
            content=ft.Column([
                ft.Icon(icon, color="white" if primary else "#1E4DB7"),
                ft.Text(title, weight="bold", size=12, color="white" if primary else "black"),
                ft.Text(subtitle, size=10, color="white" if primary else "grey")
            ], horizontal_alignment="center"),expand=True
        )
    def create_att(e):
       page.navigate("/create_att")
    def sessions(e):
        page.navigate("/staff_session")       
    page.add(
        ft.Container(bgcolor="#1E4DB7", padding=20, border_radius=ft.BorderRadius.only(bottom_left=20, bottom_right=20),
            content=ft.Column([
                ft.Row([ft.Icon(ft.Icons.MENU, color="white"), ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color="white")], alignment="spaceBetween"),
                ft.Text(f"Welcome,\n{fullname}", color="white", size=18, weight="bold"),
                
            ])
        ),
        
            
            
        ft.Container(padding=15, content=ft.Column([
            ft.Text("Smart Attendance", weight="bold", size=18),
            ft.Text("Fast • Simple • Reliable", size=12, color="grey"),
            ft.Row([ft.Container(card(ft.Icons.ADD_CIRCLE, "Create Attendance", "Start a new class session", True),on_click=lambda e :create_att(e),expand=True),
                    ft.Container(card(ft.Icons.LIST_ALT, "View Sessions", "Check past & current sessions"),on_click=lambda e:sessions(e))]),
            ft.Row([card(ft.Icons.PEOPLE, "My Classes", "Manage your courses"),
                    card(ft.Icons.SETTINGS, "Settings", "App preferences")])
        ]))
    )
