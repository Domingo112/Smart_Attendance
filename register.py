
import re,os,sqlite3,random
import flet as ft

#for database
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
c=conn.cursor()

def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/user_register"
        )
    )
    page.title = "Smart Attendance"
    page.padding = 0
    page.bgcolor = "#F5F5F5"
    page.window.width = 300
    page.window.height = 600
    arr=[]

    # DARK MODE FUNCTION — KEPT
    def mode(e):
        if page.bgcolor == "#F5F5F5":
            toggle_icon.icon=ft.Icons.LIGHT_MODE
            page.bgcolor = "black"
        else:
            page.bgcolor = "#F5F5F5"
            toggle_icon.icon=ft.Icons.DARK_MODE

        update_theme()
        page.update()

    # -----------------------------
    # Registration
    # -----------------------------

    class register:
        def __init__(self,fullname,email,age,password,id=None):
            self.fullname=fullname.strip().title()
            self.email=email.strip().lower()
            self.age=age.strip()
            self.password=password.strip()
            self.id=id

        def fulname(self):
           if not self.fullname:
               return False,"input your fullname"
           return True,"fullname Valid"

        def ageing(self):
            if not self.age:
                return False, "input your age"
            return True,"Age is valid"

        def email_check(self):
            if not self.email:
                return False, "Input your email"

            if "@" not in self.email:
                return False, "Email must contain @"

            if "." not in self.email:
                return False, "Email must contain ."
            if " " in self.email:
                return False, "Email must not contain spaces"

            if self.email.endswith(";"):
                return False, "Email cannot end with ;"

            return True, "Email is valid"

        def password_check(self):
            if not self.password:
               return False,"Fill in your password"
            if len(self.password)>=6 and len(self.password)<=12:
                return True,"password valid"

            return False, "Password invalid"

        def save(self):
            passok,passmsg=self.password_check()
            if not passok:
                return False,passmsg

            emailok,emailmsg=self.email_check()
            if not emailok:
                return False,emailmsg

            okfull,okmsg=self.fulname()
            if not okfull:
                return False,okmsg

            okage,msgage=self.ageing()
            if not okage:
                return False,msgage

            check=c.execute(
                "select * from users where email=?",
                (self.email,)
            )

            if check.fetchone():
                return False,"Email Already exist"
            else:
                try:
                    c.execute("""
                    insert into users
                    (fullname,email,age,password,user_id)
                    values(?,?,?,?,?)
                    """,(self.fullname,
                         self.email,
                         self.age,
                         self.password,self.id,))
                    conn.commit()
                    return True,"Registration Successful"

                except sqlite3.IntegrityError:
                    return False,"Email already exist"

                except Exception as e:
                    return False, f"Error: {e}"

                

    # -----------------------------
    # LOGO AND APP NAME
    # -----------------------------

    logo = ft.Container(
        content=ft.Icon(
            ft.Icons.HOW_TO_REG,
            size=32,
            color="white",
        ),
        width=60,
        height=60,
        bgcolor="#3F704D",
        border_radius=18,
        alignment=ft.Alignment.CENTER,
    )

    app_name = ft.Text(
        "Smart Attendance",
        size=23,
        weight=ft.FontWeight.BOLD,
        color="#3F704D",
    )

    display_name = ft.Text(" ")

    tagline = ft.Text(
        "Attendance made simple.",
        size=12,
        color="#777777",
    )

    # -----------------------------
    # INPUT FIELDS
    # -----------------------------

    fullname = ft.TextField(
        label="Fullname",
        hint_text="Domingo",
        width=240,
        border_color="#B7C8BA",
        focused_border_color="#3F704D",
        label_style=ft.TextStyle(color="#3F704D", size=12),
        autofocus=True,
        prefix_icon=ft.Icons.PERSON_OUTLINE,
    )

    email = ft.TextField(
        label="Email",
        hint_text="example@gmail.com",
        width=240,
        border_color="#B7C8BA",
        focused_border_color="#3F704D",
        label_style=ft.TextStyle(color="#3F704D", size=12),
        keyboard_type=ft.KeyboardType.EMAIL,
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
    )

    age = ft.TextField(
        label="Age",
        hint_text="Enter your age",
        width=240,
        border_color="#B7C8BA",
        focused_border_color="#3F704D",
        label_style=ft.TextStyle(color="#3F704D", size=12),
        keyboard_type=ft.KeyboardType.NUMBER,
        prefix_icon=ft.Icons.CALENDAR_TODAY,
    )

    password = ft.TextField(
        label="Password",
        hint_text="Enter your password",
        width=240,
        border_color="#B7C8BA",
        focused_border_color="#3F704D",
        label_style=ft.TextStyle(color="#3F704D", size=12),
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        helper="Password must be > 6 and < 12"
    )

    # -----------------------------
    # CARD TITLES
    # -----------------------------

    card_title = ft.Text(
        "Create Account",
        size=19,
        weight=ft.FontWeight.BOLD,
        color="#263D2C",
    )

    card_subtitle = ft.Text(
        "Fill in your details to get started",
        size=11,
        color="#777777",
    )

    # -----------------------------
    # REGISTER BUTTON
    # -----------------------------

    register_button = ft.Button(
        on_click=lambda e:submit(e),
        content="Register",
        width=240,
        style=ft.ButtonStyle(
            bgcolor="#3F704D",
            color="#FFFFFF",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=15,
        ),
    )

    # -----------------------------
    # REGISTRATION FUNCTION
    # -----------------------------

    def submit(e):
        x=random.randint(10000,99999)

        name=fullname.value
        mail=email.value
        ages=age.value
        keying=password.value

        registering=register(name,mail,ages,keying,x)
        ok,msg=registering.save()

        if ok:
            display_name.value=msg
            display_name.color="green"
        else:
            display_name.value=msg
            display_name.color="red"
        page.update()

    # -----------------------------
    # REGISTRATION CARD
    # -----------------------------

    card = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(
                            ft.Icons.PERSON_ADD_ALT_1,
                            color="#3F704D",
                            size=23,
                        ),
                        card_title,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                ),
                card_subtitle,
                ft.Container(height=5),
                fullname,
                email,
                age,
                password,
                ft.Container(height=5),
                register_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
            tight=True,
        ),
        bgcolor="#FFFFFF",
        width=280,
        padding=15,
        border_radius=18,
        shadow=ft.BoxShadow(
            blur_radius=18,
            spread_radius=1,
            color="#18000000",
            offset=ft.Offset(0, 5),
        ),
    )

    # -----------------------------
    # THEME COLORS
    # -----------------------------

    def update_theme():
        dark = page.bgcolor == "black"

        card.bgcolor = "#000000" if dark else "#FFFFFF"
        app_name.color = "#FFFFFF" if dark else "#3F704D"
        tagline.color = "#CCCCCC" if dark else "#777777"
        card_title.color = "#FFFFFF" if dark else "#263D2C"
        card_subtitle.color = "#CCCCCC" if dark else "#777777"
        footer.color = "#CCCCCC" if dark else "#789187"

        for field in [fullname, email, age, password]:
            field.bgcolor = "#000000" if dark else "#FFFFFF"
            field.color = "#FFFFFF" if dark else "#000000"
            field.border_color = "#666666" if dark else "#B7C8BA"
            field.focused_border_color = "#8BC49A"
            field.label_style = ft.TextStyle(
                color="#FFFFFF" if dark else "#3F704D",
                size=12,
            )

        register_button.style = ft.ButtonStyle(
            bgcolor="#3F704D",
            color="#FFFFFF",
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=15,
        )

        toggle_icon.icon_color = "#FFFFFF" if dark else "#3F704D"

    # -----------------------------
    # DARK MODE TOGGLE
    # -----------------------------

    toggle_icon = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        icon_color="#3F704D",
        tooltip="Toggle Dark Mode",
        on_click=mode,
    )

    toggle_button = ft.Container(
        content=toggle_icon,
        alignment=ft.Alignment.CENTER_RIGHT,
        width=280,
    )

    # -----------------------------
    # FOOTER
    # -----------------------------

    footer = ft.Text(
        "SMARTER RECORDS. BETTER RESULTS.",
        size=10,
        color="#789187",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    # -----------------------------
    # MAIN PAGE
    # -----------------------------

    page_container = ft.Container(
        content=ft.Column(
            [
                toggle_button,
                logo,
                app_name,
                tagline,
                ft.Container(height=2),
                ft.Container(
                    content=display_name,
                    width=280,
                    on_click=lambda e:print("clicked"),
                    alignment=ft.Alignment.CENTER,
                ),
                card,
                ft.Container(height=2),
                footer,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
        expand=True,
        alignment=ft.Alignment.CENTER,
        padding=10,
    )

    # -----------------------------
    # RESPONSIVE HEIGHT LAYOUT
    # -----------------------------

    def resize_layout(e=None):
        screen_height = page.height or 500

        if screen_height <= 250:
            gap = 0
            field_height = 30
            logo.visible = False
            tagline.visible = False
            footer.visible = False
            toggle_button.visible = False
            app_name.size = 14
            padding = 2
            card_title.size = 14
            card_subtitle.size = 9

        elif screen_height <= 350:
            gap = 2
            field_height = 35
            logo.visible = True
            tagline.visible = True
            footer.visible = False
            toggle_button.visible = True
            app_name.size = 18
            padding = 4
            card_title.size = 17
            card_subtitle.size = 10

        else:
            gap = 8
            field_height = 45
            logo.visible = True
            tagline.visible = True
            footer.visible = True
            toggle_button.visible = True
            app_name.size = 23
            padding = 10
            card_title.size = 19
            card_subtitle.size = 11

        # Resize input fields
        for field in [fullname, email, age, password]:
            field.height = field_height
            field.text_size = 11 if screen_height <= 250 else 13
            field.content_padding = (
                2 if screen_height <= 250 else 8
            )

        # Resize card and page spacing
        card.padding = padding
        card.content.spacing = gap
        page_container.padding = padding
        page_container.content.spacing = gap

        page.update()

    # -----------------------------
    # RUN PAGE
    # -----------------------------

    page.add(page_container)

    # Detect screen resizing
    page.on_resized = resize_layout

    resize_layout()
    update_theme()


