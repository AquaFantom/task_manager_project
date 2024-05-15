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
    Icon,
    TextField
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

        self.bottom_nav_rail = NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.bottom_nav_change,
            extended=True,
            expand=True,
            bgcolor=colors.BLUE_GREY,
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

    def sync_board_destinations(self):
        #boards = self.store.get_boards()
        boards = ["Board"]
        self.bottom_nav_rail.destinations = []
        for i in range(len(boards)):
            b = boards[i]
            self.bottom_nav_rail.destinations.append(
                NavigationRailDestination(
                    label_content=TextField(
                        value=b,
                        hint_text=b,
                        text_size=12,
                        read_only=True,
                        #on_focus=self.board_name_focus,
                        #on_blur=self.board_name_blur,
                        border="none",
                        height=50,
                        width=150,
                        text_align="start",
                        data=i
                    ),
                    label="Board",#b.name,
                    selected_icon=icons.CHEVRON_RIGHT_ROUNDED,
                    icon=icons.CHEVRON_RIGHT_OUTLINED
                )
            )
        self.page.update()

    def top_nav_change(self, e):
        self.top_nav_rail.selected_index = e.control.selected_index
        self.update()

    def bottom_nav_change(self, e):
        index = e if (type(e) == int) else e.control.selected_index
        self.top_nav_rail.selected_index = None
        self.bottom_nav_rail.selected_index = index
        self.page.route = f"/board/{index}"
        self.view.update()
        self.page.update()
