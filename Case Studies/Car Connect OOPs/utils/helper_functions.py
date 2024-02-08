def input_menu_choice(message="Enter your choice: "):
    try:
        choice = int(input(message))
        return choice
    except ValueError:
        return None
