import flet as ft
from flet_core import Page, AppBar, Text, icons, colors, Row, IconButton, Column, TextField


class TaskManager(Row):
    def __init__(self, page: Page, app_ref, layout_ref):
        super().__init__(ref=app_ref)
        self.layout_ref = layout_ref
        self.page = page
        self.appbar = AppBar(
            leading=IconButton(icons.TABLE_ROWS_ROUNDED,
                               icon_color=colors.WHITE,
                               icon_size=30,
                               on_click=layout_ref.current.toggle_nav_rail),
            leading_width=75,
            title=Text("TaskManager", size=32, text_align="start", color=colors.WHITE, font_family="Comfortaa_Bold"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_500

        )
        self.page.appbar = self.appbar
        self.page.update()

    def add_board(self, e):
        def close_dlg(e):
            if (hasattr(e.control, "text") and not e.control.text == "Отмена") or (
                    type(e.control) is ft.TextField and e.control.value != ""
            ):
                self.create_new_board(dialog_text.value)
            dialog.open = False
            self.page.update()

        def textfield_change(e):
            if dialog_text.value == "":
                create_button.disabled = True
            else:
                create_button.disabled = False
            self.page.update()

        dialog_text = TextField(
            label="Введите название", on_submit=close_dlg, on_change=textfield_change
        )
        create_button = ft.ElevatedButton(
            text="Создать", bgcolor=colors.BLUE_200, on_click=close_dlg, disabled=True
        )
        dialog = ft.AlertDialog(
            title=Text("Введите название!"),
            content=Column(
                [
                    dialog_text,
                    Row(
                        [
                            ft.ElevatedButton(text="Отмена", on_click=close_dlg),
                            create_button,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
                tight=True,
            ),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        dialog_text.focus()

    def create_new_board(self, board_name):
        # new_board = Board(self, self.store, board_name)
        new_board = board_name
        # self.store.add_board(new_board)
        self.layout_ref.current.hydrate_all_boards_view()

    def delete_board(self, e):
        return
        # self.store.remove_board(e.control.data)
        # self.layout.set_all_boards_view()
