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
    TextField,
    PopupMenuButton,
    PopupMenuItem,
    border_radius,
    border,
    TextThemeStyle,
    TextAlign,
    MainAxisAlignment

)

from sidebar import Sidebar


class AppLayout(Row):
    def __init__(self, page: Page, ref, *args, **kwargs):
        super().__init__(*args, **kwargs, ref=ref)
        self.page = page

        self.sidebar = Sidebar(page)

        self._active_view: Control = Column(
            controls=[],
            alignment=ft.alignment.center,
            horizontal_alignment=ft.alignment.center
        )

        self.members_view = Text("members view")

        self.all_boards_view = Column([
            Row([
                Container(
                    Text(value="Ваши доски", style=TextThemeStyle.HEADLINE_MEDIUM),
                    expand=True,
                    padding=padding.only(top=15)),
                Container(
                    TextButton(
                        "Добавить новую доску",
                        icon=icons.ADD,
                        on_click='',
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

        self.controls = [
            self.sidebar,
            self.active_view,
            self.all_boards_view
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

    def hydrate_all_boards_view(self):
        self.all_boards_view.controls[-1] = Row([
            Container(
                content=Row([
                    Container(
                        content=Text(value=b), data=b, expand=True, on_click=''),
                    Container(
                        content=PopupMenuButton(  # контейнер с кнопкой всплывающего меню
                            items=[
                                PopupMenuItem(
                                    content=Text(value="Удалить", style=TextThemeStyle.LABEL_MEDIUM,
                                                 text_align=TextAlign.CENTER),
                                    on_click='', data=b),
                                PopupMenuItem(),
                                PopupMenuItem(
                                    content=Text(value="Архивировать", style=TextThemeStyle.LABEL_MEDIUM,
                                                 text_align=TextAlign.CENTER),
                                )
                            ]
                        ),
                        padding=padding.only(right=-10),
                        border_radius=border_radius.all(3)
                    )], alignment=MainAxisAlignment.SPACE_BETWEEN),
                border=border.all(1, colors.BLACK38),
                border_radius=border_radius.all(5),
                bgcolor=colors.WHITE60,
                padding=padding.all(10),
                width=250,
                data=b
            ) for b in ["Board"]  # self.store.get_boards()
        ], wrap=True)
        self.sidebar.sync_board_destinations()
