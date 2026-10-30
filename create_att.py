import flet as ft,random,os,sqlite3
#for database
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
c=conn.cursor()

def main(page: ft.Page):
    page.views.append(
         ft.View(
             route="/create_att"
         )
    )
    id=page.session.store.get("id")
    page.padding=0
    page.bgcolor="white"
    page.window.width=300
    class create_attendance:
        def __init__(self,name,date,time,duration,pin,staff_id):
            self.name=name
            self.date=date
            self.time=time
            self.duration=duration
            self.pin=pin
            self.staff_id=staff_id
            page.session.store.set("pin",self.pin)
        def save_to_database(self):
            if not self.name:
                return False,"Input Attendance Name"
            if not self.date:
                return False,"Input Attendance date"
            try:
                c.execute("""insert into attendance(name,date,time,duration,pin,staff_id)
                          values(?,?,?,?,?,?)""",(self.name,self.date,self.time,self.duration,self.pin,self.staff_id,))
                conn.commit()
                return True,page.navigate("/pinview")
            except Exception as e:
                return False,f"Error {e}"
            finally:
                conn.close()
             
    attendance_name= ft.TextField(hint_text="Physics 101", prefix_icon=ft.Icons.ACCESS_TIME, border_radius=10)
    attendance_date= ft.TextField(hint_text="Wed, 15 Oct 2025", prefix_icon=ft.Icons.CALENDAR_MONTH, border_radius=10)
    attendance_time=ft.TextField(hint_text="10:00 AM", prefix_icon=ft.Icons.ACCESS_TIME, border_radius=10)
    attendance_duration=ft.TextField(hint_text="60", prefix_icon=ft.Icons.TIMER, border_radius=10)
    generated_Pin=random.randint(1000,99999)
    msg=ft.Text("")
    def submit(e):
        att_name=attendance_name.value
        att_date=attendance_date.value
        att_time=attendance_time.value
        att_duration=attendance_duration.value
        att_pin=generated_Pin
        Created_attendance=create_attendance(att_name,att_date,att_time,att_duration,att_pin,id)
        ok,message=Created_attendance.save_to_database()
        if ok:
            msg.value=message
            msg.color="green"
        else:
            msg.value=message
            msg.color="red"
    page.add(
        ft.AppBar(title=ft.Text("Create Attendance"), bgcolor="#1E4DB7", color="white"),
        ft.Container(padding=15, content=ft.Column([
            ft.Text("Attendance Name ", weight="bold", size=12,color="black"),
            #attendance_name
            attendance_name,
            ft.Text("Date", weight="bold", size=12,color="black"),
            #attendance_date
            attendance_date,
           
            ft.Text("Time", weight="bold", size=12,color="black"),
            #attendance_time
            attendance_time,
            
            ft.Text("Duration (minutes)", weight="bold", size=12,color="black"),
            
            #attendance_duration
            attendance_duration,
            ft.Container(
                content=msg,alignment=ft.Alignment.CENTER),
            ft.Button("Create Attendance",on_click=lambda e:submit(e), bgcolor="#1E4DB7", color="white", width=400, height=45, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)))
            
        ], spacing=12),expand=True)
    )
