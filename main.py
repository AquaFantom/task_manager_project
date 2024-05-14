import flet as ft
from flet import (
    Page,
    colors
)

from app import TaskManager
from app_layout import AppLayout

# Файл, который отвечает за "разворот" приложения. Именно его мы запускаем
if __name__ == "__main__":
    def main(page: Page):
        app_layout_ref = ft.Ref[AppLayout]()

        app_layout = AppLayout(page=page, ref=app_layout_ref)
        TaskManager(page, app_layout_ref)

        page.title = "TaskManager"
        page.padding = 0
        page.bgcolor = colors.GREY_100
        page.fonts = {"Comfortaa": "assets/fonts/Comfortaa-Regular.ttf",
                      "Comfortaa_Bold": "assets/fonts/Comfortaa-Bold.ttf"}

        page.add(
            ft.Row(
                controls=[
                    app_layout,
                ]
            )
        )
        page.add()
        page.update()


    ft.app(target=main)
