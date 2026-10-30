import flet as ft,os,sqlite3
import asyncio
#for database


def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/pin"
            )
        )
    dbname=os.path.join(os.path.dirname(__file__),"attend.db")
    conn=sqlite3.connect(dbname)
    conn.row_factory=sqlite3.Row
    c=conn.cursor()
    page.bgcolor="white"
    id=page.session.store.get("id")
    page.session.store.set("id",id)
    print(id)
    pinfield=ft.TextField(label="Enter PIN", prefix_icon=ft.Icons.LOCK, border_radius=10,keyboard_type=ft.KeyboardType.NUMBER)
    userid=page.session.store.get("ide")
    print(userid)  
    def submit(txt):
        text=txt.value.strip()
        async def shake():
            for x in [-0.1,0.1,-0.08,0.08,0]:
                pinfield.offset=ft.Offset(x,0)
                pinfield.update()
                await asyncio.sleep(0.07)
        try:
            if not text:
                pinfield.border_color="red"
                pinfield.error="Pin is emoty"
                shake()            
            c.execute("select * from attendance where id = ? ",(id,))
            row=c.fetchone()
            conn.commit()
            if row["Pin"]==int(text):
                try:
                    uid=id
                    c.execute("insert into user_att(userid,subject_id)values(?,?)",(userid,uid,))
                    conn.commit()
                    page.navigate("/pin_verify")
                except Exception as ex:
                    print(f"error{ex}")
                        
               
            else:
                pinfield.error=F"PIN {text} is incorrect"
                pinfield.border_color="red"
               
        except Exception as e:
            print(f"error{e}")    
        
    page.add(
        ft.Container(padding=20, content=ft.Column([
            ft.Icon(ft. Icons.PERSON, size=100, color="#1A2421"),
            ft.Text("Smart Attendance", weight="bold", size=22, color="#1A2421"),
            ft.Text("Your Attendance, Made Easy", size=12),
            ft.Text("Enter the PIN provided by your lecturer\nto mark your attendance.", size=12, text_align="center", color="grey"),
            pinfield,
            ft.Button("Submit", bgcolor="#1A2421", color="white", width=400,on_click=lambda e:submit(pinfield)
                ),
            ft.Text("Need help? Contact your lecturer", size=11, color="#1E4DB7")
        ], horizontal_alignment="center", spacing=15))
    )
