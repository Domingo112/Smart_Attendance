import flet as ft,os,sqlite3
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
c=conn.cursor()

def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/useredit"
        )
    )
    displaytxt=ft.Text("",text_align="center")
    userid=page.session.store.get("userid")
    page.window.width=300
    try:
        c.execute("""
                  select * from users where id=?
                  """,(userid,))
        userdetails=c.fetchone()
    except Exception as e:
        print(e)    
    class update:
        def __init__(self,fullname,email,password,age):
            self.fullname=fullname
            self.email=email
            self.password=password
            self.age=age
        def save(self):
            if not self.fullname:
                self.fullname=userdetails["fullname"]
            if not self.email:
                self.email=userdetails["email"]
            if not self.password:
                self.password=userdetails["password"]
            if not self.age:
                self.age=userdetails["age"]
            try:
                c.execute("""update  users set fullname=?,email=?,password=?,age=?
                          where id =?
                          """,(self.fullname,self.email,self.password,self.age,userid,))
                print(self.fullname,self.age,self.password)
                conn.commit()
                return True,"Updated successfully"
            
            except Exception as e:
                print(e)
            page.update() 
    def updateuser(e):
        name=surname.value
        mail=email.value
        passkey=password.value
        userage=age.value
        u=update(name,mail,passkey,userage)
        ok,msg=u.save()
        if ok:
            displaytxt.value=msg
            displaytxt.color="green"
        else:
            displaytxt.value=msg
            displaytxt.color="red"    
            
                                 
       
    DARK = "#1a2421"
    page.bgcolor = "#F5F5F0"
    
    surname = ft.TextField(label="Surname", prefix_icon=ft.Icons.PERSON_OUTLINE, border_radius=10)
    email = ft.TextField(label="Email",  prefix_icon=ft.Icons.EMAIL_OUTLINED, border_radius=10)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, prefix_icon=ft.Icons.LOCK_OUTLINE, border_radius=10)
    age = ft.TextField(label="Age", value="28", prefix_icon=ft.Icons.CALENDAR_MONTH, border_radius=10)
    
    page.add(
        ft.Column([
            ft.Container(bgcolor=DARK, padding=ft.Padding.only(top=40, bottom=20, left=10), content=ft.Row([ft.Icon(ft.Icons.ARROW_BACK, color="white"), ft.Text("Edit Profile", color="white", size=20, weight=ft.FontWeight.BOLD)]), border_radius=ft.BorderRadius.only(bottom_left=20, bottom_right=20)),
            ft.Column([displaytxt,surname, email, password, age,  ft.Button("Save Changes", bgcolor=DARK, color="white", width=400, height=55,on_click=lambda e:updateuser(e))], spacing=15, expand=True, scroll=ft.ScrollMode.AUTO)
        ], expand=True)
    )
