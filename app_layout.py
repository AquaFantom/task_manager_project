import flet as ft
from flet import (
    Control,
    Column,
    Page,
    Row,
    Text,
    IconButton,
    colors,
    icons,
    AppBar
)

from sidebar import Sidebar


class AppLayout(Row):
    def __init__(self, page: Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.appbar = AppBar(
            leading=IconButton(icons.TABLE_ROWS_ROUNDED,
                               icon_color=colors.WHITE,
                               icon_size=30,
                               on_click=self.toggle_nav_rail),
            leading_width=75,
            title=Text("TaskManager", size=32, text_align="start", color=colors.WHITE, font_family="Comfortaa_Bold"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_500

        )
        self.page.appbar = self.appbar

        self.sidebar = Sidebar(page)

        self._active_view: Control = Column(
            controls=[
                Text("Active View")
            ],
            alignment=ft.alignment.center,
            horizontal_alignment=ft.alignment.center
        )

        self.controls = [
            self.sidebar,
            # self.appbar.leading,
            self.active_view,
        ]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.appbar.leading.selected = not self.appbar.leading.selected
        self.page.update()

