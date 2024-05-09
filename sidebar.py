import flet as ft
from flet import (
    UserControl,
    Container,
    Text,
    NavigationRail,
    NavigationRailDestination,
    alignment,
    colors,
    icons,
    padding,
    margin,
    Icon
)

# Класс для боковой панели. Здесь описано всё её содержимое
class Sidebar(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.top_nav_items = [
            NavigationRailDestination(
                label_content=Text("Доски", font_family='Comfortaa', size=16),
                label="Доски",
                icon_content=Icon(name=icons.SPACE_DASHBOARD_OUTLINED, size=30, color=colors.LIGHT_BLUE_700),
                selected_icon_content=Icon(name=icons.SPACE_DASHBOARD, size=30, color=colors.LIGHT_BLUE_700),

            ),
            NavigationRailDestination(
                label_content=Text("Заметки", font_family='Comfortaa', size=16),
                label="Заметки",
                icon_content=Icon(name=icons.EVENT_NOTE_OUTLINED, size=30, color=colors.LIGHT_BLUE_700),
                selected_icon_content=Icon(name=icons.EVENT_NOTE, size=30, color=colors.LIGHT_BLUE_700),
            )
        ]
        self.top_nav_rail = NavigationRail(
            min_width=100,
            min_extended_width=400,
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor=colors.GREY_200,
            extended=True,
            expand=True,
        )

    def build(self):
        self.view = Container(
            content=self.top_nav_rail,
            padding=padding.only(left=0, bottom=10, top=15),
            margin=margin.all(-10),
            width=self.page.width * 0.2,
            bgcolor=colors.GREY_200,
            height=self.page.height,
            alignment=alignment.center_left,
        )
        return self.view

    def top_nav_change(self, e):
        self.top_nav_rail.selected_index = e.control.selected_index
        self.update()
