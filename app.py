from flask import Flask, render_template, request, redirect, url_for

from database import Database
from game import Game

app = Flask(__name__)

@app.route('/')
def index():
    database = Database()
    ranking = database.get_ranking()

    """
    if ranking == []:
        return "🚨 Nenhuma pontuação registrada até o momento!"
    elif ranking is not None:
        result = "🏆 RANKING BIOMAZE:\n"
        for _id, tuple in enumerate(database.get_ranking()):
            result += f"#{_id+1} {tuple[0]}: {tuple[1]}s\n"
        return result
    else:
        return "⚠️ Falha ao ler o banco de dados!"
    """

    return render_template('index.html', ranking=ranking)

@app.route('/game')
def new_game():
    """
    It starts a new game.
    """

    game = Game()

    # Game loop:
    while game.running:
        game.show_map()
        game.status()

if __name__ == '__main__':
    app.run(debug=True)