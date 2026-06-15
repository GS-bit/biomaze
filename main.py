import sys

from database import Database
from game import Game
from utils import clear_screen, show_menu

def new_game() -> None:
    """
    It starts a new game.
    """

    game = Game()

    # Game loop:
    while game.running:
        clear_screen()
        game.show_map()
        game.status()

def show_ranking() -> None:
    """
    It shows the game ranking on the screen.
    """

    clear_screen()

    print("🏆 RANKING BIOMAZE:\n")

    database = Database()

    ranking = database.get_ranking()

    if ranking == []:
        print("🚨 Nenhuma pontuação registrada até o momento!")
    elif ranking is not None:
        for _id, tuple in enumerate(database.get_ranking()):
            print(f"#{_id+1} {tuple[0]}: {tuple[1]}s")
    else:
        print("⚠️ Falha ao ler o banco de dados!")


    input("\nPressione <ENTER> para continuar...")

    main()

def exit_game() -> None:
    """
    It exits the game.
    """

    print("Até logo! 👋")
    sys.exit(0)

def main() -> None:
    """
    It shows the initial screen.
    """

    clear_screen()
    print("====================================")
    print(" 🧭 BIOMAZE: LABIRINTO ENDÓCRINO 🧭 ")
    print("====================================\n")

    options = {1: new_game, 2: show_ranking, 3: exit_game}
    chosen_option = show_menu(["Novo jogo", "Mostrar ranking", "Sair"])

    options[chosen_option]()

if __name__ == "__main__":
    main()