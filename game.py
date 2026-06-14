class Game:
    def __init__(self):
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
        
        self.cur_organ = "HIPÓFISE"
        self.activated_organs = ["HIPÓFISE"]

        self.running = True
        self.won = None

    def show_map(self):
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
    
    def status(self):
        available_connections = self.connections[self.cur_organ]

        print(f"""------------------------------------------------------------------------
📍 Órgão atual: [ {self.cur_organ} ]
🧪 Hormônio: Adrenalina | Órgãos ativados: {len(self.activated_organs)} de 12
------------------------------------------------------------------------
🩸 VIAS SANGUÍNEAS DISPONÍVEIS:
""")
    
        for i, organ in enumerate(available_connections, 1):
            print(f"[ {i} ] Ir para {organ}")
        print("")

        way = input(f"➡ Escolha o seu caminho (digite o número desejado): ")

        self.cur_organ = available_connections[int(way) - 1]

        if self.cur_organ not in self.activated_organs:
            self.activated_organs.append(self.cur_organ)
        else:
            self.running = False
            self.won = False

        if len(self.activated_organs) == 12:
            self.running = False
            self.won = True