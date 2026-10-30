import flet as ft,os,sqlite3
from datetime import datetime
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
c=conn.cursor()
#put real userid

list_view=ft.Column(spacing=6,scroll=ft.ScrollMode.HIDDEN)

def main(page: ft.Page):
    page.views.append(
        ft.View(
            rotate="/history"
        )
    )
    page.bgcolor="white"
    userid=page.session.store.get("ide")
    def history(e):
        searching=search.value
        like=f"%{searching}%"
        try:
            c.execute("""select user_att.*,attendance.name as name
                      from user_att inner join attendance on 
                      user_att.subject_Id=attendance.id where (attendance.name like ?) and user_att.userid=? order by id desc""",(like,userid,)
            )
            user_history=c.fetchall()
            list_view.controls.clear()
            for users in user_history:
                dt=users["submitted_at"]
                de=datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
                now=de.strftime("%d/%B/%Y %I:%M %p")
                list_view.controls.append(item(users["name"],now,"Attended"))
                
        except Exception as e:
            print(f"Error {e}")
            page.update()
               
    def item(course, time, status, present=True):
        return ft.Container(border=ft.Border.all(1, "#EEE"), border_radius=10, padding=10, margin=5,
            content=ft.Row([ft.Column([ft.Text(course, weight="bold", size=12,color="black"), ft.Text(time, size=11, color="black")]),
                           ft.Container(content=ft.Text(status, size=11, color="green" if present else "red"), bgcolor="#E8F5E9" if present else "#FFEBEE", padding=5, border_radius=20)], alignment="spaceBetween"))
    search=ft.TextField(hint_text="search...",on_change=lambda e:history(e) ,width=250,border_radius=10)    
    page.add(
        ft.AppBar(title=ft.Text("My Attendance",color="black"), bgcolor="white"),
        ft.Row([
            ft.Container(search),
            
        ], alignment="spaceAround"),
        list_view,
    )
    history(search) 
