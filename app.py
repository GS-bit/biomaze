from flask import Flask, jsonify, render_template, request, redirect, url_for

from database import Database
from game import Game

app = Flask(__name__)

game = Game()

@app.route('/')
def index():
    database = Database()
    ranking = database.get_ranking()

    """
    if ranking == []:
        return "🚨 Nenhuma pontuação registrada até o momento!"
    elif ranking is not None:
        result = "🏆 RANKING BIOMAZE:\n"
        for _id, tuple in enumerate(ranking):
            result += f"#{_id+1} {tuple[0]}: {tuple[1]}s\n"
        return result
    else:
        return "⚠️ Falha ao ler o banco de dados!"
    """

    return render_template('index.html', ranking=ranking)

@app.route('/game')
def new_game():
    """
    It opens the new game page.
    """

    return render_template('game.html', game=game)

@app.route('/gamestatus', methods=['GET'])
def game_status():
    """
    It gives the game status.
    """

    information = {
        "connections": game.connections,
        "cur_organ": game.cur_organ,
        "activated_organs": game.activated_organs,
        "running": game.running,
        "start_time": game.start_time
    }

    return jsonify(information)

@app.route('/gamemovement', methods=['POST'])
def game_movement():
    """
    It gives the game movement.
    """

    new_organ = request.data.decode('utf-8')
    game.cur_organ = new_organ

    if game.cur_organ not in game.activated_organs:
        game.activated_organs.append(game.cur_organ)
    else:
        game.running = False
        game.gameover = True

    if len(game.activated_organs) == 12:
        game.running = False

    return game_status()

if __name__ == '__main__':
    app.run(debug=True)