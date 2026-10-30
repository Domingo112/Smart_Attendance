# import flet as ft de
# import flet as ft
# def main(page: ft.Page):
#     page.bgcolor = "#EEF6FF"
#     page.padding = 0
#     page.window_width = 400
#     page.window_height = 850
# COLORS - from your design
#     BLUE = "#1D4ED8"
#     DARK_BLUE = "#1E3A8A"
#     LIGHT_BG = "#EEF6FF"
# ----- APP BAR -----
#     app_bar = ft.Container(
#         bgcolor=DARK_BLUE,
#         padding=ft.padding.only(top=40, left=16, right=16, bottom=20),
#         content=ft.Row(
#             controls=[
#                 ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="white", on_click=lambda _: print("back")),
#                 ft.Text("My Profile", size=22, weight=ft.FontWeight.BOLD, color="white", expand=True, text_align=ft.TextAlign.CENTER),
#                 ft.Container(width=40) # spacer
#             ]
#         )
#     )
# ----- PROFILE HEADER -----
#     profile_header = ft.Column(
#         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         controls=[
#             ft.Container(
#                 width=90, height=90,
#                 bgcolor="#DBEAFE",
#                 border_radius=45,
#                 border=ft.border.all(4, "#93C5FD"),
#                 content=ft.Icon(ft.Icons.PERSON, size=50, color=DARK_BLUE)
#             ),
#             ft.Text("Dr. Adeyemi", size=24, weight=ft.FontWeight.BOLD),
#             ft.Text("Lecturer", size=14, color="#64748B"),
#             ft.Container(height=10),
#             ft.Row([
#                 ft.Icon(ft.Icons.BUSINESS, size=18, color="#64748B"),
#                 ft.Text("Computer Science", size=13)
#             ], alignment=ft.MainAxisAlignment.CENTER),
#             ft.Row([
#                 ft.Icon(ft.Icons.EMAIL, size=18, color="#64748B"),
#                 ft.Text("dr.adeyemi@university.edu", size=13)
#             ], alignment=ft.MainAxisAlignment.CENTER),
#             ft.Row([
#                 ft.Icon(ft.Icons.PHONE, size=18, color="#64748B"),
#                 ft.Text("+234 801 234 5678", size=13)
#             ], alignment=ft.MainAxisAlignment.CENTER),
#         ]
#     )
# ----- MY DETAILS CARD -----
#     details_card = ft.Container(
#         bgcolor="white",
#         border_radius=12,
#         border=ft.border.all(1, "#E2E8F0"),
#         padding=16,
#         content=ft.Column([
#             ft.Text("My Details", weight=ft.FontWeight.BOLD, size=16, text_align=ft.TextAlign.CENTER),
#             ft.Divider(height=1, color="#E2E8F0"),
#             ft.Row([ft.Text("Department", color="#64748B", expand=1), ft.Text("Computer Science", weight=ft.FontWeight.W500)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
#             ft.Divider(height=1, color="#E2E8F0"),
#             ft.Row([ft.Text("Staff ID", color="#64748B", expand=1), ft.Text("LEC-24015", weight=ft.FontWeight.W500)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
#         ])
#     )
# ----- ACCOUNT STATS -----
#     def stat_box(icon, value, label):
#         return ft.Container(
#             bgcolor="#F1F5F9",
#             border_radius=10,
#             border=ft.border.all(1, "#E2E8F0"),
#             padding=12,
#             expand=1,
#             content=ft.Column([
#                 ft.Icon(icon, color=BLUE),
#                 ft.Text(value, size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
#                 ft.Text(label, size=11, color="#475569", text_align=ft.TextAlign.CENTER),
#             ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
#         )
#     stats_card = ft.Container(
#         bgcolor="white",
#         border_radius=12,
#         border=ft.border.all(1, "#E2E8F0"),
#         padding=16,
#         content=ft.Column([
#             ft.Text("Account Stats", weight=ft.FontWeight.BOLD, size=16, text_align=ft.TextAlign.CENTER),
#             ft.Row([
#                 stat_box(ft.Icons.LIST_ALT, "4", "Total Classes"),
#                 stat_box(ft.Icons.CALENDAR_MONTH, "12", "Total Sessions"),
#                 stat_box(ft.Icons.GROUP, "24", "Students"),
#             ], spacing=8)
#         ])
#     )
# ----- BUTTONS -----
#     edit_btn = ft.ElevatedButton(
#         "Edit Profile", bgcolor=BLUE, color="white",
#         width=400, height=50,
#         style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
#     )
#     logout_btn = ft.OutlinedButton(
#         "Logout", icon=ft.Icons.LOGOUT,
#         width=400, height=50,
#         style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
#     )
# ----- BOTTOM NAV -----
#     bottom_nav = ft.Container(
#         bgcolor="white",
#         padding=10,
#         border_radius=ft.border_radius.only(top_left=20, top_right=20),
#         content=ft.Row([
#             ft.Column([ft.Icon(ft.Icons.HOME, color=BLUE), ft.Text("Home", size=10, color=BLUE)], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=1),
#             ft.Column([ft.Icon(ft.Icons.LIST_ALT), ft.Text("Sessions", size=10)], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=1),
#             ft.Column([ft.Icon(ft.Icons.GROUP), ft.Text("Students", size=10)], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=1),
#             ft.Column([ft.Icon(ft.Icons.SETTINGS), ft.Text("Settings", size=10)], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=1),
#         ], alignment=ft.MainAxisAlignment.SPACE_AROUND)
#     )
# ----- MAIN BODY -----
#     body = ft.Container(
#         bgcolor="white",
#         border_radius=ft.border_radius.only(top_left=20, top_right=20),
#         padding=16,
#         expand=True,
#         content=ft.Column([
#             profile_header,
#             ft.Container(height=10),
#             details_card,
#             ft.Container(height=10),
#             stats_card,
#             ft.Container(height=12),
#             edit_btn,
#             ft.Container(height=8),
#             logout_btn,
#         ], scroll=ft.ScrollMode.AUTO, expand=True)
#     )
#     page.add(
#         ft.Column([
#             app_bar,
#             body,
#             bottom_nav
#         ], spacing=0, expand=True)
#     )
# ft.app(main)