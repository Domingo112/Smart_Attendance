import flet as ft,os,sqlite3
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
c=conn.cursor()


def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/profile"
        )
    )
    page.bgcolor = "#EEF6FF"
    page.padding = 0
    page.window.width = 300
    page.window.height=600
    userid=page.session.store.get("ide")
    page.session.store.set("userid",userid)

    BLUE = "#1D4ED8"
    DARK_BLUE = "#1E3A8A"
    LIGHT_BG = "#EEF6FF"
    username=ft.Text("Dr. Adeyemi", size=24, weight=ft.FontWeight.BOLD,color="black")
    email=ft.Text("dr.adeyemi@university.edu", size=13,color="black")
    phone=ft.Text("Computer Science", size=13,color="black")
    user_id=ft.Text("Lecturer", size=14,color="black")
    app_bar = ft.Container(
        bgcolor=DARK_BLUE,
        padding=ft.Padding.only(top=5, left=16, right=16, bottom=20),
        content=ft.Row(
            controls=[
                #back arrow
                ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", on_click=lambda _: print("back")),
                ft.Text("My Profile", size=22, weight=ft.FontWeight.BOLD, color="white", expand=True, text_align=ft.TextAlign.CENTER),
                ft.Container(width=40) # spacer
            ]
        )
    )

    profile_header = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(
                width=90, height=90,
                bgcolor="#DBEAFE",
                border_radius=45,
                border=ft.Border.all(4, "#93C5FD"),
                content=ft.Icon(ft.Icons.PERSON, size=50, color=DARK_BLUE)
            ),
            username,
            user_id,
            ft.Container(height=10),
            ft.Row([
                ft.Icon(ft.Icons.PERSON, size=18, color="#64748B"),
                phone,
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.Icon(ft.Icons.EMAIL, size=18, color="#64748B"),
                email,
            ], alignment=ft.MainAxisAlignment.CENTER),
            
        ]
    )

    
    def profile():
        try:
            c.execute("select * from users where id=?",(userid,))
            users_details=c.fetchone()
            username.value=users_details["fullname"]
            email.value=users_details["email"]
            phone.value=users_details["age"]
            user_id.value=f"Users ID :{users_details["user_id"]}"
        except Exception as e:
            print(f"error{e}")    
    
    

    edit_btn = ft.Button(
        "Edit Profile", bgcolor=BLUE, color="white",on_click=lambda e:page.navigate("/useredit"),
        width=400, height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )
    logout_btn = ft.OutlinedButton(
        "Logout", icon=ft.Icons.LOGOUT,
        width=400, height=50,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    

    body = ft.Container(
        bgcolor="white",
        border_radius=ft.BorderRadius.only(top_left=20, top_right=20),
        padding=16,
        expand=True,
        content=ft.Column([
            profile_header,
            ft.Container(height=10),
            ft.Container(height=12),
            edit_btn,
            ft.Container(height=8),
            logout_btn,
        ], scroll=ft.ScrollMode.AUTO, expand=True)
    )
    page.add(
        ft.Column([
            app_bar,
            body,
        ], spacing=0, expand=True)
    )
    profile()
    page.update()
