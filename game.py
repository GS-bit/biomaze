from random import choice, randint
import time


class Game:
    """
    This class represents the game logic.
    """

    def __init__(self) -> None:
        """
        Game constructor. It creates the necessary attributes to the game.
        """

        """
        A dictionary of connections: each key corresponds to an organ,
        and their values are lists of the organs connected to the key.
        """
        self.connections = {
            "HIPÓFISE": ["TIREOIDE", "PULMÕES", "CORAÇÃO"],
            "TIREOIDE": ["HIPÓFISE", "ESTÔMAGO", "PÂNCREAS"],
            "PULMÕES": ["HIPÓFISE", "CORAÇÃO", "FÍGADO"],
            "CORAÇÃO": ["HIPÓFISE", "PULMÕES", "ESTÔMAGO", "FÍGADO", "BAÇO", "INTESTINO DELGADO"],
            "ESTÔMAGO": ["TIREOIDE", "CORAÇÃO", "PÂNCREAS", "RINS"],
            "PÂNCREAS": ["TIREOIDE", "ESTÔMAGO", "RINS"],
            "FÍGADO": ["PULMÕES", "CORAÇÃO", "INTESTINO DELGADO"],
            "BAÇO": ["CORAÇÃO", "INTESTINO DELGADO"],
            "INTESTINO DELGADO": ["FÍGADO", "INTESTINO GROSSO", "CORAÇÃO", "BAÇO", "RINS"],
            "RINS": ["ESTÔMAGO", "PÂNCREAS", "INTESTINO DELGADO", "INTESTINO GROSSO"],
            "INTESTINO GROSSO": ["INTESTINO DELGADO", "RINS", "SUPRARRENAIS"],
            "SUPRARRENAIS": ["INTESTINO GROSSO"]
        }
        
        # The list of possible initial organs in the maze:
        start_organs = list(self.connections.keys())
        start_organs.remove("INTESTINO GROSSO")  # Starting at "Intestino grosso" won't give us solution to the maze.

        self.start_organ = choice(start_organs)  # The initial organ in the maze.
        self.cur_organ = self.start_organ  # The organ our hormone is located at the moment.
        self.activated_organs = [self.cur_organ]  # A list of all organs that received the hormone.

        self.running = True  # Boolean variable: True if the game is running, False otherwise.
        self.gameover = False  # Boolean variable: True if the game is in gameover, False otherwise.

        self.random_seed = randint(1,1000) # Seed used for graph renderization on the browser.

        self.start_time = 0 # A number that represents the beginning of the time on the game.
        self.end_time = 0 # A number that represents the end of the time of the game.