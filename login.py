
import flet as ft,os,sqlite3
#for database
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
c=conn.cursor()

def main(page: ft.Page):
    page.views.append(
        ft.View(
            rotate="/login"
        )
    )
    page.title = "Smart Attendance - Login"
    page.bgcolor = "#F5F5F5"
    page.padding = 15
    page.window.width = 360
    page.window.height = 700
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.HIDDEN

    dark_green = "#1A2421"
    grey = "#777777"
    msg_dis=ft.Text("")
    # Logo
    logo = ft.Container(
        content=ft.Icon(
            ft.Icons.HOW_TO_REG,
            size=34,
            color="#FFFFFF",
        ),
        bgcolor=dark_green,
        width=65,
        height=65,
        border_radius=20,
        alignment=ft.Alignment.CENTER,
    )
    #login class
    class login:
        def __init__(self,email,passw):
            self.mail=email
            self.key=passw
        def user_log(self):
            if not self.mail:
                return False,"fill in Email/UserId/StaffId" 
            if not self.key:
                return False,"Fill in Password"
            c.execute(""" select * from users where 
                                 (email=? or user_id=?) and password = ?
                                 
                                 """,(self.mail,self.mail,self.key))
            user_table=c.fetchone()
            if user_table:
                page.session.store.set("user_id",user_table["id"])
                page.session.store.set("user_name",user_table["fullname"])
                print(user_table["id"])
                conn.commit()
                return True,page.navigate("/user_home")
            if not user_table:
                c.execute(""" select * from staff where 
                                    (email=? or staff_id=?) and password = ?
                                     """,(self.mail,self.mail,self.key,))
                user_table=c.fetchone()
                page.session.store.set("staff_id",user_table["id"])
                page.session.store.set("staff_name",user_table["fullname"])
                conn.commit()
                return True,page.navigate("/staff_home")
            
            
            return False,"Login failed wrong credentials"    
                
               
    # App heading
    header = ft.Column(
        [
            logo,
            ft.Text(
                "Smart Attendance",
                size=26,
                weight=ft.FontWeight.BOLD,
                color=dark_green,
            ),
            ft.Text(
                "Welcome Back!",
                size=18,
                weight=ft.FontWeight.W_500,
                color="#333333",
            ),
            ft.Text(
                "Sign in to continue",
                size=12,
                color=grey,
            ),msg_dis,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=7,
    )

    # Login fields
    email = ft.TextField(
        label="Email Address/userid/staffid",
        hint_text="Enter your email/userid/staffid",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        border_radius=12,
        border_color="#DADADA",
        focused_border_color=dark_green,
        bgcolor="#FFFFFF",
        text_size=13,
        height=55,
        content_padding=10,
    )

    password = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        password=True,
        can_reveal_password=True,
        border_radius=12,
        border_color="#DADADA",
        focused_border_color=dark_green,
        bgcolor="#FFFFFF",
        text_size=13,
        height=55,
        content_padding=10,
    )

    forgot_password = ft.Row(
        [
            ft.Container(expand=True),
            ft.Text(
                "Forgot Password?",
                size=12,
                color=dark_green,
                weight=ft.FontWeight.W_500,
            ),
        ]
    )
    #for login button
    def click(e):
        mail=email.value
        key=password.value
        login_class=login(mail,key)
        ok,msg=login_class.user_log()
        if ok:
            msg_dis.value=msg
            msg_dis.color="green"
        else:
            msg_dis.value=msg
            msg_dis.color="red"    
    # Login button - UI only
    login_button = ft.Container(
        content=ft.Text(
            "SIGN IN",
            size=14,
            weight=ft.FontWeight.BOLD,
            color="#FFFFFF",
        ),
        bgcolor=dark_green,
        height=48,
        border_radius=12,
        alignment=ft.Alignment.CENTER,
        ink=True,
        on_click=lambda e: click(e),
    )

    # Divider
    divider = ft.Row(
        [
            ft.Container(
                height=1,
                bgcolor="#DDDDDD",
                expand=True,
            ),
            ft.Text(
                "OR CREATE AN ACCOUNT",
                size=10,
                color=grey,
            ),
            ft.Container(
                height=1,
                bgcolor="#DDDDDD",
                expand=True,
            ),
        ],
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # User registration navigation option
    user_register = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Icon(
                        ft.Icons.PERSON_ADD_ALT_1,
                        color=dark_green,
                        size=23,
                    ),
                    bgcolor="#E8EEEB",
                    width=43,
                    height=43,
                    border_radius=12,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Column(
                    [
                        ft.Text(
                            "User Registration",
                            size=13,
                            weight=ft.FontWeight.BOLD,
                            color=dark_green,
                        ),
                        ft.Text(
                            "Create a user account",
                            size=10,
                            color=grey,
                        ),
                    ],
                    spacing=3,
                    expand=True,
                ),
                ft.Icon(
                    ft.Icons.ARROW_FORWARD_IOS,
                    size=16,
                    color=dark_green,
                ),
            ],
            spacing=10,
        ),
        padding=12,
        bgcolor="#FFFFFF",
        border=ft.Border.all(1, "#E3E7E4"),
        border_radius=14,
        ink=True,
        on_click=lambda e: page.navigate("/user_register"),
    )

    # Staff / lecturer registration navigation option
    staff_register = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Icon(
                        ft.Icons.SCHOOL_OUTLINED,
                        color=dark_green,
                        size=23,
                    ),
                    bgcolor="#E8EEEB",
                    width=43,
                    height=43,
                    border_radius=12,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Column(
                    [
                        ft.Text(
                            "Staff / Lecturer Registration",
                            size=13,
                            weight=ft.FontWeight.BOLD,
                            color=dark_green,
                        ),
                        ft.Text(
                            "Register as a lecturer",
                            size=10,
                            color=grey,
                        ),
                    ],
                    spacing=3,
                    expand=True,
                ),
                ft.Icon(
                    ft.Icons.ARROW_FORWARD_IOS,
                    size=16,
                    color=dark_green,
                ),
            ],
            spacing=10,
        ),
        padding=12,
        bgcolor="#FFFFFF",
        border=ft.Border.all(1, "#E3E7E4"),
        border_radius=14,
        ink=True,
        on_click=lambda e: page.navigate("/staff_register"),
    )

    # Login card
    login_card = ft.Container(
        content=ft.Column(
            [
                email,
                password,
                forgot_password,
                login_button,
                divider,
                user_register,
                staff_register,
            ],
            spacing=13,
            tight=True,
        ),
        bgcolor="#FFFFFF",
        padding=18,
        border_radius=20,
        border=ft.Border.all(1, "#EAEAEA"),
        shadow=ft.BoxShadow(
            blur_radius=12,
            color="#12000000",
            offset=ft.Offset(0, 4),
        ),
        width=400,
    )

    page.add(
        ft.Column(
            [
                header,
                login_card,
                ft.Text(
                    "Secure • Simple • Smart",
                    size=10,
                    color="#999999",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,
            expand=True,
        )
    )



