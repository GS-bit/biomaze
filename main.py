from game import Game
from utils import clear_screen, show_menu

if __name__ == "__main__":
    clear_screen()
    print("🧭 BIOMAZE: LABIRINTO ENDÓCRINO 🧭")
    show_menu(["Novo jogo"])

    game = Game()

    # Game loop:
    while game.running:
        clear_screen()
        game.show_map()
        game.status()

    if game.won:
        print("=========================================================================")
        print("🥇 Parabéns! Você ativou todos os órgãos e venceu o jogo!")
        print("=========================================================================")
    else:
        print("=========================================================================")
        print("😔 Game over! Você ativou um órgão mais de uma vez. Tente novamente.")
        print("=========================================================================")