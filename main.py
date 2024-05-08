import flet as ft
from flet import (
    Page,
    colors
)

from app import TaskManager
from app_layout import AppLayout
from sidebar import Sidebar

if __name__ == "__main__":
    def main(page: Page):
        page.title = "TaskManager"
        page.padding = 0
        page.bgcolor = colors.GREY_100
        page.fonts = {"Comfortaa": "assets/fonts/Comfortaa-Regular.ttf",
                      "Comfortaa_Bold": "assets/fonts/Comfortaa-Bold.ttf"}
        page.add(
            ft.Row(
                controls=[
                    TaskManager(page),
                    AppLayout(page)
                ]
            )
        )
        page.add()
        page.update()

    ft.app(target=main)