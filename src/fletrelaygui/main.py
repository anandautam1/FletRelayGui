"""
This is the main file that can serve as a starting point for a Python
console script.

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``run`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import os
import glob
import flet as ft

from fletrelaygui import __version__

def get_list_of_com_ports():
    port_list = []
    if os.name == 'posix':
        port_list = glob.glob('/dev/tty.*')
    return port_list

def create_dynamic_dropdown(choices):
    dropdown_options = []
    for choice in choices:
        dropdown_options.append(ft.dropdown.Option(str(choice)))
    dynamic_dropdown = ft.Dropdown(
        width=100,
        options=dropdown_options
    )
    return dynamic_dropdown

def main(page: ft.Page):
    page.title = "Flet Relay GUI"
    com_ports_list = get_list_of_com_ports()
    com_port_dropdown = create_dynamic_dropdown(com_ports_list)
    page.add(com_port_dropdown)

def start_app():
    ft.app(target=main)

if __name__ == "__main__":
    start_app()
