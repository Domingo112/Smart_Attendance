
import flet as ft,asyncio
def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/pin_verify"
        )
    )
    page.window.width=300
    page.bgcolor="#1A2421"
    async def redirect():
        page.opacity=1
        page.update()
        await asyncio.sleep(3)
        page.opacity=0
        page.update()
        await asyncio.sleep(0.8)
        #put the real redirect
        page.navigate("/submite_pin ")
        
        
    userid=page.session.store.get("id")
    page.session.store.set("userid",userid)
    print(userid)
    page.add(
        ft.Container(expand=True, content=ft.Column([
            ft.ProgressRing(width=120, height=120, stroke_width=5, color="white"),
            ft.Icon(ft.Icons.LOCK, size=40, color="white"),
            ft.Text("Submitting Attendance...", weight="bold", size=18, color="white"),
            ft.Text("Please wait while we verify\nyour PIN and mark your attendance.", color="white70", text_align="center", size=12)
        ], alignment="center", horizontal_alignment="center"),expand_loose=True,alignment=ft.Alignment.CENTER)
    )
    page.run_task(redirect)
