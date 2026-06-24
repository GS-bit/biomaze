import time

from flask import Flask, jsonify, render_template, request, redirect, url_for

from database import Database
from game import Game

app = Flask(__name__)

game = Game()

@app.route('/')
def index():
    """
    Main page.
    """

    database = Database()
    ranking = database.get_ranking()

    return render_template('index.html', ranking=ranking)

@app.route('/game')
def new_game():
    """
    It opens the "new game" page.
    """

    game.start_time = time.perf_counter()

    return render_template('game.html', game=game)

@app.route('/gamestatus', methods=['GET'])
def game_status():
    """
    It gives the game status to client side.
    """

    game.end_time = time.perf_counter()

    information = {
        "connections": game.connections,
        "start_organ": game.start_organ,
        "cur_organ": game.cur_organ,
        "activated_organs": game.activated_organs,
        "running": game.running,
        "gameover": game.gameover,
        "time_spent": round(game.end_time - game.start_time, 2),
        "random_seed": game.random_seed
    }

    return jsonify(information)

@app.route('/gamemovement', methods=['POST'])
def game_movement():
    """
    It applies a movement to the game, receiving the command from the client side.
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

        game.end_time = time.perf_counter()

    return game_status()

@app.route('/resetgame', methods=['POST'])
def reset_game():
    """
    It resets the game.
    """

    global game
    game = Game()

    return ""

@app.route('/savescore', methods=['POST'])
def save_score():
    """
    It saves the score.
    """

    received_data = request.get_json()
    name = received_data["name"]
    start_organ = received_data["start_organ"]
    time_spent = received_data["time_spent"]

    database = Database()

    if database.new_score(name, start_organ, time_spent) == 0:  # Adding the score onto the DB
        return "Pontuação adicionada no ranking! Volte sempre 👋"
    else:
        return "⚠️ Falha ao adicionar pontuação no banco de dados!" 

if __name__ == '__main__':
    app.run(debug=True)