
import flet as ft
import asyncio


def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/"
        )
    )
    page.title = "Smart Attendance"
    page.padding = 0
    page.bgcolor = "#F5F8F6"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 350
    page.window.height = 700
    page.window.resizable = True

    # -------------------------------
    # FLOATING BACKGROUND ICONS
    # -------------------------------

    floating_items = [
        {"icon": ft.Icons.PEOPLE, "left": 25, "top": 70, "size": 35},
        {"icon": ft.Icons.CALENDAR_MONTH, "left": 260, "top": 130, "size": 32},
        {"icon": ft.Icons.CHECK_CIRCLE, "left": 40, "top": 270, "size": 34},
        {"icon": ft.Icons.ACCESS_TIME, "left": 275, "top": 350, "size": 34},
        {"icon": ft.Icons.FINGERPRINT, "left": 25, "top": 470, "size": 38},
        {"icon": ft.Icons.BADGE, "left": 260, "top": 540, "size": 35},
    ]

    floating_controls = []

    for item in floating_items:
        control = ft.Container(
            content=ft.Icon(
                item["icon"],
                size=item["size"],
                color="#B8D8C6",
            ),
            left=item["left"],
            top=item["top"],
            animate_position=ft.Animation(
                1800,
                ft.AnimationCurve.EASE_IN_OUT,
            ),
        )
        floating_controls.append(control)

    # -------------------------------
    # MAIN CONTENT
    # -------------------------------

    logo = ft.Container(
        content=ft.Icon(
            ft.Icons.HOW_TO_REG,
            size=48,
            color=ft.Colors.WHITE,
        ),
        width=90,
        height=90,
        bgcolor="#176B4D",
        border_radius=26,
        alignment=ft.Alignment.CENTER,
        shadow=ft.BoxShadow(
            blur_radius=20,
            color="#30176B4D",
            offset=ft.Offset(0, 8),
        ),
    )

    title = ft.Text(
        "Smart Attendance",
        size=29,
        weight=ft.FontWeight.BOLD,
        color="#163D2E",
        text_align=ft.TextAlign.CENTER,
    )

    subtitle = ft.Text(
        "Attendance made simple.",
        size=16,
        color="#547164",
        text_align=ft.TextAlign.CENTER,
    )

    description = ft.Text(
        "Track attendance, manage records, and "
        "save time with a smarter way to stay organized.",
        size=13,
        color="#71847A",
        text_align=ft.TextAlign.CENTER,
    )

    get_started = ft.Container(
        content=ft.Row(
            [
                ft.Text(
                    "GET STARTED",
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=14,
                ),
                ft.Icon(
                    ft.Icons.ARROW_FORWARD,
                    color=ft.Colors.WHITE,
                    size=19,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        ),
        width=220,
        height=54,
        bgcolor="#176B4D",
        border_radius=16,
        alignment=ft.Alignment.CENTER,
        ink=True,
        on_click=lambda e: page.navigate("/login"),
    )

    footer = ft.Text(
        "SMARTER RECORDS. BETTER RESULTS.",
        size=10,
        color="#789187",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    main_content = ft.Container(
        expand=True,
        padding=25,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            [
                logo,
                ft.Container(height=22),
                title,
                subtitle,
                ft.Container(height=12),
                ft.Container(
                    content=description,
                    width=280,
                ),
                ft.Container(height=30),
                get_started,
                ft.Container(height=35),
                footer,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=7,
        ),
    )

    # -------------------------------
    # LAYER EVERYTHING TOGETHER
    # -------------------------------

    page.add(
        ft.Stack(
            controls=floating_controls + [main_content],
            expand=True,
            clip_behavior=ft.ClipBehavior.NONE,
        )
    )

    # -------------------------------
    # FLOATING ANIMATION
    # -------------------------------

    async def animate_icons():
        direction = 1

        while True:
            await asyncio.sleep(1.8)
            direction *= -1

            for index, control in enumerate(floating_controls):
                item = floating_items[index]

                control.top = (
                    item["top"] + (12 * direction)
                )

                control.left = (
                    item["left"]
                    + (6 * direction if index % 2 == 0 else -6 * direction)
                )

            page.update()

    page.run_task(animate_icons)


