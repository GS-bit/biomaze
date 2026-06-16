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

def help() -> None:
    """
    It shows how to play the game.
    """

    clear_screen()

    print("❓ COMO JOGAR BIOMAZE:\n")

    print("Você é um hormônio que está perambulando pelo corpo humano. Seu objetivo é passar por todos os órgãos uma única vez, sem repetição.\n")
    print("Se isso ocorrer, você será declarado vencedor. Caso contrário, será fim de jogo.")

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

    options = {1: new_game, 2: show_ranking, 3: help, 4: exit_game}
    chosen_option = show_menu(["Novo jogo", "Mostrar ranking", "Como jogar", "Sair"])

    options[chosen_option]()

if __name__ == "__main__":
    main()