#!/usr/bin/env python3
from simple_term_menu import TerminalMenu
import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
menu = TerminalMenu(files, title="Select a file")
choice = menu.show()
if choice is not None:
    file = files[choice]
    editor_menu = TerminalMenu(["nano", "vim", "nvim"], title="Choose editor")
    editor_choice = editor_menu.show()
    if editor_choice is not None:
        os.system(f"{['nano','vim','nvim'][editor_choice]} {file}")
