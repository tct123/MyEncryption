import flet as ft
from caesar import caesar_encrypt


def main(page: ft.Page):
    text = ft.TextField(hint_text="Text")
    count = ft.TextField(hint_text="Count")
    textfield = ft.Text("")
    page.add(ft.SafeArea(ft.Column([text, count, textfield])))


ft.app(main)
