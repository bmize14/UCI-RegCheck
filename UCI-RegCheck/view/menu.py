"""menu.py

Contains helper functions for displaying menus and other messages to the user.
"""


def display_welcome_message():
    """Prints a welcome message to be displayed at the program's start."""
    print("Welcome to UCI RegCheck! Enter a number corresponding to a menu"
          " command to continue.\n\n")


def display_main_menu(time_delay: int):
    """Prints a formatted main menu to be displayed to the user."""
    main_menu = "Select a menu option:\n"
    "  1. Add new course to monitor\n"
    "  2. Edit time delay between updates (current: {} seconds)\n"
    "  3. Quit\n"

    print(main_menu.format(time_delay))
