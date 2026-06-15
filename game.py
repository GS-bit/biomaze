from utils import show_menu


class Game:
    """
    This class represents the game logic.
    """

    def __init__(self) -> None:
        """
        Game constructor.
        """

        """
        A dictionary of connections: each key corresponds to an organ,
        and their values are lists of the organs connected to the key.
        """
        self.connections = {
            "HIPÓFISE": ["TIREOIDE", "PULMÕES", "CORAÇÃO"],
            "TIREOIDE": ["HIPÓFISE", "ESTÔMAGO", "PÂNCREAS"],
            "PULMÕES": ["HIPÓFISE", "CORAÇÃO", "FÍGADO"],
            "CORAÇÃO": ["HIPÓFISE", "PULMÕES", "ESTÔMAGO", "FÍGADO", "BAÇO", "INTESTINO SUP."],
            "ESTÔMAGO": ["TIREOIDE", "CORAÇÃO", "PÂNCREAS", "RINS"],
            "PÂNCREAS": ["TIREOIDE", "ESTÔMAGO", "RINS"],
            "FÍGADO": ["PULMÕES", "CORAÇÃO", "INTESTINO SUP."],
            "BAÇO": ["CORAÇÃO", "INTESTINO SUP."],
            "INTESTINO SUP.": ["FÍGADO", "INTESTINO INF.", "CORAÇÃO", "BAÇO"],
            "RINS": ["ESTÔMAGO", "PÂNCREAS", "INTESTINO SUP.", "INTESTINO INF."],
            "INTESTINO INF.": ["INTESTINO SUP.", "RINS", "SUPRARRENAL"],
            "SUPRARRENAL": ["INTESTINO INF."]
        }
        
        self.cur_organ = "HIPÓFISE"  # The organ our hormone is located at the moment
        self.activated_organs = ["HIPÓFISE"]  # A list of all organs that received the hormone

        self.running = True  # Boolean variable: True if the game is running, False otherwise.
        self.won = None  # Initially None. In the future, True if player won the game, False otherwise. 

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
                    [INTESTINO SUP.] ------- [RINS]
                           \                 /
                            \               /
                            [INTESTINO INF.] ------ [SUPRARRENAL]
            """)
    
    def status(self) -> None:
        """
        It shows the status of the game on the screen
        and asks the player the desired movement. 
        """

        available_connections = self.connections[self.cur_organ]

        print(f"""------------------------------------------------------------------------
📍 Órgão atual: [ {self.cur_organ} ]
🧪 Hormônio: Adrenalina | Órgãos ativados: {len(self.activated_organs)} de 12
------------------------------------------------------------------------

🩸 VIAS SANGUÍNEAS DISPONÍVEIS:
""")

        way = show_menu([f"Ir para {organ}" for organ in available_connections], "➡ Escolha o seu caminho (digite o número desejado): ")

        self.cur_organ = available_connections[int(way) - 1]

        if self.cur_organ not in self.activated_organs:
            self.activated_organs.append(self.cur_organ)
        else:
            self.running = False
            self.won = False

        if len(self.activated_organs) == 12:
            self.running = False
            self.won = True