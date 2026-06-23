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

    return render_template('game.html', game=game)

@app.route('/gamestatus', methods=['GET'])
def game_status():
    """
    It gives the game status to client side.
    """

    information = {
        "connections": game.connections,
        "cur_organ": game.cur_organ,
        "activated_organs": game.activated_organs,
        "running": game.running,
        "start_time": game.start_time,
        "gameover": game.gameover,
        "time_spent": game.time_spent,
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

        game.time_spent = round(time.perf_counter() - game.start_time, 2)  # Time spent on the game

    return game_status()

if __name__ == '__main__':
    app.run(debug=True)