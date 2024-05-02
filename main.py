import flet
from flet import (
    Page,
    colors
)

from app import TaskManager

if __name__ == "__main__":
    def main(page: Page):
        page.title = "TaskManager"
        page.padding = 0
        page.bgcolor = colors.GREY_100
        page.fonts = {"Comfortaa": "assets/fonts/Comfortaa-Regular.ttf",
                      "Comfortaa_Bold": "assets/fonts/Comfortaa-Bold.ttf"}
        app = TaskManager(page)
        page.add(app)
        page.update()

    flet.app(target=main)
