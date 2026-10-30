
import flet as ft,os,sqlite3
from datetime import datetime
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
c=conn.cursor()
def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/live_att"
        )
    )
    page.bgcolor="white"
    page.window.width=300
    page.padding=0
    page.scroll=ft.ScrollMode.HIDDEN
    subject_info=ft.Text("", weight="bold")
    subject_info1=ft.Text("Wed, 15 Oct 2025  10:00 AM", size=11)
    subject_id=page.session.store.get("id")
    list_view=ft.Column()
    searching=ft.TextField(hint_text="Search student...", prefix_icon=ft.Icons.SEARCH, border_radius=10, height=40,on_change=lambda e:search(e))
    def details():
        c.execute("select * from attendance where id=?",(subject_id,))
        detail=c.fetchone()
        subject_info.value=detail["name"]
        subject_info1.value=f"{detail["date"]} • {detail["time"]}"
    def search(e):
        searches=searching.value.strip()
        like=f"%{searches}%"
        
        c.execute("select users.fullname,user_att.submitted_at from users inner join user_att on users.id=user_att.userid  where (fullname like ?) and user_att.subject_id=?",(like,subject_id,))
        result=c.fetchall()
        list_view.controls.clear()
        for i, re in enumerate(result,start=1):
            dt=re["submitted_at"]
            de=datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
            now=de.strftime("%d/%B/%Y %I:%M %p")
           
            if not re:
                print(re)
                
                list_view.controls.append("search is empty")
            list_view.controls.append(item(i,re["fullname"],f"Submitted :{now}"))    
            
            
        

    def item(number,name,date):
           
            
            return ft.Container(border=ft.Border.all(1, "#EEE"), border_radius=10, padding=10, margin=5,
                content=ft.Row([ft.Column([
                    ft.Row([ft.Text(number, weight="bold", size=12,color="black"), ft.Text(name, size=11, color="black")]),
                    ft.Text(date, size=11, color="black")]),
                                ], alignment=ft.Alignment.TOP_RIGHT))
    page.add(
        ft.AppBar(title=ft.Text("Live Attendance"), bgcolor="#1E4DB7", color="white"),
        ft.Container(padding=15, content=ft.Column([
            ft.Row([ft.Column([subject_info,subject_info1]),
                    ft.Container(bgcolor="#E8F5E9", content=ft.Text("• Active", size=11, color="green"), padding=5, border_radius=20)]),
            
            searching,
            
            list_view,
            
            
        ]))
    )
    details()
    search(searching)
    page.update()
