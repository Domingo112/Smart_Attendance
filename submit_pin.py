import flet as ft,os,sqlite3
from datetime import datetime
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
c=conn.cursor()
def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/submite_pin"
        )
    )
    page.bgcolor="#F0FAF2"
    page.window.width=300
    userid=page.session.store.get("userid")
    print(userid)
    Attendance_name= ft.Text("Computer Science 101", size=12)
    # Attendance_date= ft.Text("Wed, 15 Oct 2025", size=12)
    submitted_at= ft.Text("10:00 AM", size=12)
    def attendance_detail():
        
        try:
            c.execute("""select attendance.id as ide, attendance.name,attendance.submitted_at as att,
                      user_att.submitted_at as timing,user_att.subject_id as sub_ide,user_att.userid,user_att.id
                      from user_att inner join attendance on ide=sub_ide
                      where sub_ide=? order by user_att.id desc""",(userid,))
            userdetails=c.fetchone()
            Attendance_name.value=userdetails["name"]
            dt=userdetails["timing"]
            de=datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
            now=de.strftime("%d/%B/%Y %I:%M %p")
            # Attendance_date.value=userdetails["att"]
            submitted_at.value=now
            
        except Exception as e:
            print(f"Error{e}")    
            
        
    attendance_detail()   
    page.add(
        ft.Container(padding=20, content=ft.Column([
            ft.Icon(ft.Icons.CHECK_CIRCLE, size=80, color="#2E7D32"),
            ft.Text("Attendance Submitted!", weight="bold", size=18),
            ft.Text("Your attendance has been successfully\nrecorded.", size=12, color="Black", text_align="center"),
            ft.Container(bgcolor="white", border_radius=10, padding=15, content=ft.Column([
                ft.Row([ft.Icon(ft.Icons.CABIN, size=16),Attendance_name]),
                # ft.Row([ft.Icon(ft.Icons.CALENDAR_MONTH, size=16),Attendance_date]),
                ft.Row([ft.Icon(ft.Icons.ACCESS_TIME, size=16),submitted_at]),
            ])),
            ft.Button("Back to Home", icon=ft.Icons.HOME, bgcolor="#1B8A3D", color="white", width=400,on_click=lambda e:page.navigate("/user_home"))
        ], horizontal_alignment="center", spacing=15),expand=True)
    )
