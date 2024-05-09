import flet as ft
from flet import (
    Control,
    Column,
    Page,
    Row,
    Text,
)

from sidebar import Sidebar


class AppLayout(Row):
    def __init__(self, page: Page, ref, *args, **kwargs):
        super().__init__(*args, **kwargs, ref=ref)
        self.page = page

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
        self.page.update()

