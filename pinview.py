import flet as ft
def main(page: ft.Page):
    page.views.append(
             ft.View(
                 route="/pinview"
            )
         )
    page.bgcolor="#F5F7FB"
    page.window.width=300
    page.padding=0
    pin=page.session.store.get("pin")  
    page.add(
        ft.AppBar(title=ft.Text("Attendance Session"), bgcolor="#1E4DB7", color="white"),
        ft.Container(padding=20, content=ft.Column([
            ft.Icon(ft.Icons.CHECK_CIRCLE, size=70, color="#2E7D32"),
            ft.Text("Attendance Created!", weight="bold", size=18,color="black"),
            ft.Text("Share the PIN with your students\nto mark their attendance.", size=12, text_align="center", color="black"),
            ft.Container(bgcolor="#D7F0DB", border_radius=15, padding=20, width=400, content=ft.Column([
                ft.Text("PIN CODE", size=11, weight="bold", color="grey"),
                ft.Text(pin, size=42, weight="bold", color="#1B5E20")
            ], horizontal_alignment="center")),
            ft.Container(padding=10, content=ft.Column([
                # ft.Row([ft.Icon(ft.icons.Icons.CLASS, size=16), ft.Text("Computer Science 101", size=12)]),
                ft.Row([ft.Icon(ft.icons.Icons.CALENDAR_MONTH, size=16), ft.Text("Wed, 15 Oct 2025", size=12)]),
                ft.Row([ft.Icon(ft.icons.Icons.ACCESS_TIME, size=16), ft.Text("10:00 AM (60 mins)", size=12)]),
            ])),
            ft.Button("Share PIN", icon=ft.Icons.SHARE, bgcolor="#1B8A3D", color="white", width=400,),
            ft.OutlinedButton("View Live Attendance", width=400)
        ], horizontal_alignment="center", spacing=15))
    )
