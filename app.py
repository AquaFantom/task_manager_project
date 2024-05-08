from flet_core import Page, AppBar, Text, icons, colors, Row, IconButton


class TaskManager(Row):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.appbar = AppBar(
            leading=IconButton(icons.TABLE_ROWS_ROUNDED,
                               icon_color=colors.WHITE,
                               icon_size=30,
                               on_click=''),
            leading_width=75,
            title=Text("TaskManager", size=32, text_align="start", color=colors.WHITE, font_family="Comfortaa_Bold"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_500

        )
        self.page.appbar = self.appbar
        self.page.update()
