import time

from database import Database
from utils import show_menu

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
            "INTESTINO DELGADO": ["FÍGADO", "INTESTINO GROSSO", "CORAÇÃO", "BAÇO"],
            "RINS": ["ESTÔMAGO", "PÂNCREAS", "INTESTINO DELGADO", "INTESTINO GROSSO"],
            "INTESTINO GROSSO": ["INTESTINO DELGADO", "RINS", "SUPRARRENAIS"],
            "SUPRARRENAIS": ["INTESTINO GROSSO"]
        }
        
        self.cur_organ = "HIPÓFISE"  # The organ our hormone is located at the moment
        self.activated_organs = ["HIPÓFISE"]  # A list of all organs that received the hormone

        self.running = True  # Boolean variable: True if the game is running, False otherwise.

        self.start_time = time.perf_counter()

    def show_map(self) -> None:
        """
        It shows a map of the maze on the screen.
        """

        print(r"""========================================================================
                    🧭 BIOMAZE: LABIRINTO ENDÓCRINO 🧭
========================================================================

            [HIPÓFISE] ----------------------- [TIREOIDE]
            /        \                         /        \
           /          \                       /          \
    [PULMÕES] ---- [CORAÇÃO] ------- [ESTÔMAGO] -- [PÂNCREAS]
           \        /   | \              \             /
            \      /    |  \              \           /
            [FÍGADO]    |  [BAÇO]          \         /
                   \    |     /             \       /
                    \   |    /               \     /
                    [INTESTINO DELGADO] ----- [RINS]
                           \                 /
                            \               /
                            [INTESTINO GROSSO] ------ [SUPRARRENAIS]
            """)
    
    def status(self) -> None:
        """
        It shows the status of the game on the screen
        and asks the player the desired movement. 
        """

        available_connections = self.connections[self.cur_organ]

        print(f"""------------------------------------------------------------------------
📍 Órgão atual: [ {self.cur_organ} ]
🧪 Número de órgãos ativados: {len(self.activated_organs)} de 12
------------------------------------------------------------------------

🩸 VIAS SANGUÍNEAS DISPONÍVEIS:
""")

        way = show_menu([f"Ir para {organ}" for organ in available_connections], "➡ Escolha o seu caminho (digite o número desejado): ")

        self.cur_organ = available_connections[int(way) - 1]

        if self.cur_organ not in self.activated_organs:
            self.activated_organs.append(self.cur_organ)
        else:
            self.running = False
            
            print("=========================================================================")
            print("😔 Game over! Você ativou um órgão mais de uma vez. Tente novamente.")
            print("=========================================================================")

        if len(self.activated_organs) == 12:
            self.running = False

            print("=========================================================================")
            print("🥇 Parabéns! Você ativou todos os órgãos e venceu o jogo!")
            print("=========================================================================")

            time_spent = round(time.perf_counter() - self.start_time, 2)  # Time spent on the game
            print(f"⏳ Tempo gasto: {time_spent}s")
            
            database = Database()
            if database.new_score(input("🪪  Digite seu nome, por favor: "), time_spent) == 0:  # Adding the score onto the DB
                print("\nPontuação adicionada no ranking! Volte sempre 👋")
            else:
                print("\n⚠️ Falha ao adicionar pontuação no banco de dados!")