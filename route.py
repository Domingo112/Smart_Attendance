import flet as ft
import pin_confirm,user_pin,user_view,register,staff_register
import landing,login,staff_home,create_att,pinview,user_home,submit_pin,attendance_history
import user_profile,useredit,live_att,staff_session
def main(page:ft.Page):
    def route_change():
        page.views.clear()
        if page.route == "/":
            landing.main(page)
        elif page.route == "/login":
               login.main(page)
        elif page.route == "/user_register":
                register.main(page)
        elif page.route == "/staff_register":
                staff_register.main(page) 
        elif page.route == "/staff_home":
                staff_home.main(page)   #                 
        elif page.route == "/create_att":
            create_att.main(page)
        elif page.route == "/pin":
            user_pin.main(page)    
        elif page.route == "/user_home":
            user_home.main(page)
        elif page.route == "/user_view":
            user_view.main(page)
        elif page.route == "/pin_verify":
            pin_confirm.main(page) 
        elif page.route == "/submite_pin ":
            submit_pin.main(page)
        elif page.route == "/history":
            attendance_history.main(page) 
        elif page.route == "/profile":
            user_profile.main(page)
        elif page.route == "/useredit":
            useredit.main(page)
        elif page.route == "/live_att":
            live_att.main(page)
        elif page.route == "/pinview":
            pinview.main(page)
        elif page.route == "/staff_session":
            staff_session.main(page)                                         
        
    page.on_route_change=route_change
    route_change()
ft.run(main)               