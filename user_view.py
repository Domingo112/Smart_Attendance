import flet as ft,os,sqlite3
#for database
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
c=conn.cursor()
def main(page: ft.Page):
    page.views.append(
            ft.View(
                route="/user_view"
            )
        )
    
    page.bgcolor="white"
    page.window.width=300
    page.scroll=ft.ScrollMode.HIDDEN
    list_view=ft.Column(spacing=6)
    userid=page.session.store.get("id")
    page.session.store.set("userid",userid)
    search=ft.TextField(hint_text="search...",on_change=lambda e: attendance_sheet(e),width=250,border_radius=10)
    def attendance_sheet(s):
        searching=search.value
        like=f"%{searching}%"
        try:
            c.execute("select * from attendance where (name like ? or time like ? or date like ?) order by submitted_at desc",(like,like,like))
            results=c.fetchall()
            list_view.controls.clear()
        except Exception as e:
            print(f"Error{e}")    
        for result in results:
            if not list_view:
                print("hello")
            list_view.controls.append(item(result["name"],f"{result["time"]} • {result["date"]}",result["id"]))
           
    def item(course,time,id,hmm=True):
        def pin(e,uid=id):
            page.session.store.set("id",uid)
            page.navigate("/pin")
        
        return ft.Container(border=ft.Border.all(1, "#EEE"), border_radius=10, padding=10, margin=5,
            content=ft.Row([ft.Column([ft.Text(course, weight="bold", size=12,color="black"), ft.Text(time, size=11, color="black")]),
                            ft.IconButton(icon=ft.Icons.ARROW_FORWARD,icon_color="grey",icon_size=20,on_click=pin)], alignment="spaceBetween"))
        
    page.add(
        ft.AppBar(title=ft.Text("My Attendance",color="black"), bgcolor="white"),
        ft.Row([
            ft.Container(search),
        ], alignment="spaceAround"),
         list_view,
        # ft.Column([item("Computer Science 101", "10:00 AM • 15 Oct 2025", "Present"), item("Physics 101", "02:00 PM • 08 Oct 2025", "Absent", False)])
    )
    attendance_sheet(search)
    page.update()
