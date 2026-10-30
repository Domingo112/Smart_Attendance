
import flet as ft,os,sqlite3,random
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
c=conn.cursor()

def main(page: ft.Page):
    page.views.append(
            ft.View(
                route="/staff_register"
            )
        )
    page.title = "Smart Attendance - Staff Registration"
    page.bgcolor = "#F5F5F5"
    page.padding = 15
    page.window.width = 360
    page.window.height = 750
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    dark_green = "#1A2421"
    grey = "#777777"

    def create_field(label, hint, icon, password=False):
        return ft.TextField(
            label=label,
            hint_text=hint,
            prefix_icon=icon,
            password=password,
            can_reveal_password=password,
            border_radius=12,
            border_color="#DADADA",
            focused_border_color=dark_green,
            bgcolor="#FFFFFF",
            text_size=13,
            height=55,
            content_padding=10,
        )
    #class for staff_registration
    class staff_registration:
        
        def __init__(self,iemail,phone,passw,fulln,id):
            self.iemail=iemail.lower().strip()
            self.phone=phone.strip()
            self.password=passw.strip()
            self.name=fulln.title().strip()
            self.id=id
        def email(self):
            if not self.iemail:
                return False,"Fill in your Email"
            if not "@" in self.iemail:
                return False, "Invalid Email must contain @"
            if "." not in self.iemail:
                return False, "Invalid Email must contain dot"
            if ";" in  self.iemail:
                return False,"Invalid Email"
            return True,"Email Valid"
        def phone_num(self):
            if not self.phone:
                return False,"Fill in Phone Number"
            return True,"fullname valid"
        def user_password(self):
            if not self.password:
                return False,"Fill in password"
            if len(self.password)>=6 and len(self.password)<=12:
                return True ,"Valid "
            return False,"Password should be > 6 and <  or equal 12"
        def fullname(self):
            if not self.name:
                return False,"Fill in Fullname"
            return True,"Fullname Valid"
        def save(self):
            pok,pmsg=self.user_password()
            eok,emsg=self.email()
            fok,fmsg=self.fullname()
            phok,phmsg=self.phone_num()
            if not pok:
                return False,pmsg
            if not eok:
                return False,emsg
            if not fok:
                return False,fmsg
            if not phok:
                return False,phmsg
            check_if_email_exist=c.execute("""select * from staff
                                           where email=?
                                            """,(self.iemail,))
            if check_if_email_exist.fetchone():
                return False,"Email already exist"
            else:
                try:
                    c.execute("""
                    insert into staff
                    (fullname,email,phone,password,staff_id)
                    values(?,?,?,?,?)
                    """,(self.name,
                        self.iemail,
                        self.phone,
                        self.password,self.id,))
                    conn.commit()
                    return True,"Registration Successful"
            
                except sqlite3.IntegrityError:
                    return False,"Email already exist"
            
                except Exception as e:
                    return False, f"Error: {e}"
            
            
            
    def click_btn(e):
        staff_id=random.randint(10000,999999)
        fname= fullname.value
        mail= email.value
        number=phone.value
        key=password.value      
        staff=staff_registration(mail,number,key,fname,staff_id)
        ok,msg=staff.save()
        if ok:
            displaymsg.color="green"
            displaymsg.value=msg
            
        else:
            displaymsg.color="red"
            displaymsg.value=msg              
    # Header
    logo = ft.Container(
        content=ft.Icon(
            ft.Icons.HOW_TO_REG,
            color="#FFFFFF",
            size=32,
        ),
        bgcolor=dark_green,
        width=58,
        height=58,
        border_radius=18,
        alignment=ft.Alignment.CENTER,
    )

    header = ft.Column(
        [
            logo,
            ft.Text(
                "Smart Attendance",
                size=25,
                weight=ft.FontWeight.BOLD,
                color=dark_green,
            ),
            ft.Text(
                "Lecturer Registration",
                size=15,
                weight=ft.FontWeight.W_500,
                color="#555555",
            ),
            ft.Text(
                "Create your staff account",
                size=12,
                color=grey,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=5,
    )

    # Lecturer registration fields
    fullname = create_field(
        "Full Name",
        "e.g. John Okon",
        ft.Icons.PERSON_OUTLINE,
    )

    

    email = create_field(
        "Institutional Email",
        "name@institution.edu",
        ft.Icons.EMAIL_OUTLINED,
    )

    

    phone = create_field(
        "Phone Number",
        "+234 800 000 0000",
        ft.Icons.PHONE_OUTLINED,
    )

    password = create_field(
        "Password",
        "Create a password",
        ft.Icons.LOCK_OUTLINE,
        password=True,
    )

   

    # Registration button - UI only
    register_button = ft.Container(
        content=ft.Text(
            "CREATE STAFF ACCOUNT",
            color="#FFFFFF",
            size=13,
            weight=ft.FontWeight.BOLD,
        ),
        bgcolor=dark_green,
        height=48,
        border_radius=12,
        alignment=ft.Alignment.CENTER,
        ink=True,
        on_click=lambda e: click_btn(e),
    )

    # Login prompt - UI only
    login_prompt = ft.Row(
        [
            ft.Text(
                "Already registered?",
                size=12,
                color=grey,
            ),
            ft.Text(
                "Sign in",
                size=12,
                color=dark_green,
                weight=ft.FontWeight.BOLD,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=4,
    )
    #diaplay message
    displaymsg=ft.Text("",text_align=ft.TextAlign.CENTER)
    # Registration card
    registration_card = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Staff Details",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=dark_green,
                ),
                ft.Text(
                    "Enter your details to get started.",
                    size=11,
                    color=grey,
                ),
                displaymsg,
                fullname,
                email,
                phone,
                password,
                register_button,
                login_prompt,
            ],
            spacing=10,
            tight=True,
        ),
        bgcolor="#FFFFFF",
        padding=16,
        border_radius=18,
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
                registration_card,
                ft.Text(
                    "Secure Staff Access",
                    size=10,
                    color="#999999",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
            expand=True,
        )
    )



