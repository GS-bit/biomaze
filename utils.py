import os
import platform

def clear_screen() -> None:
    """
    It cleans the screen.
    """

    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def show_menu(options: list[str], msg="> ") -> int:
    """
    It shows a menu on the screen.

    Arguments:
        options: a list of strings containing the menu options.
        msg: the input message.
    Returns:
        the number (int) of the selected option (starting from 1).
    """

    line_width = max([len(option) for option in options + [msg]]) + 20  # The number of "=" chars, representing the line width

    print("=" * line_width)
    for _id, option in enumerate(options):
        print(f"({_id+1}) {option}")
    print("=" * line_width)

    user_choice = input(msg)

    try:
        user_choice = int(user_choice) 

        if user_choice <= 0 or user_choice > len(options):
            raise Exception
    
        return user_choice
    except:
        print("❌ Opção inválida!")
        return show_menu(options)        
