import flet as ft
from flet import (
    Control,
    Column,
    Page,
    Row,
    Text,
    Container,
    padding,
    TextButton,
    icons,
    ButtonStyle,
    colors,
    RoundedRectangleBorder,
    TextField

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

        self.members_view = Text("members view")

        self.all_boards_view = Column([
            Row([
                Container(
                    Text(value="Ваши доски", style="headlineMedium"),
                    expand=True,
                    padding=padding.only(top=15)),
                Container(
                    TextButton(
                        "Добавить новую доску",
                        icon=icons.ADD,
                        on_click= '',
                        style=ButtonStyle(
                            bgcolor={
                                "": colors.BLUE_200,
                                "hovered": colors.BLUE_400
                            },
                            shape={
                                "": RoundedRectangleBorder(radius=3)
                            }
                        )
                    ),

                    padding=padding.only(right=50, top=15))
            ]),
            Row([
                TextField(hint_text="Поиск доски", autofocus=False, content_padding=padding.only(left=10),
                          width=200, height=40, text_size=12,
                          border_color=colors.BLACK26, focused_border_color=colors.BLUE_ACCENT,
                          suffix_icon=icons.SEARCH)
            ]),
            Row([Text("Нет подходящих досок для отображения")])
        ], expand=True)

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

