from game import Game
from util import clear_screen

game = Game()

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