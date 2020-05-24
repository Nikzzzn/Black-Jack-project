class Game:
    def __init__(self):
        self.player_count = 0
        self.p_names = {}
        self.winners = []
        self.deal_sum = 0
        self.deal_cards = []
        self.deal_A = 0
        self.player_sum = [0, 0, 0]
        self.player_cards = [[],[],[]]
        self.player_A = [0, 0, 0]
        self.turn = 0
        self.is_running = False
        self.p_stands = [False, False, False]
        self.over = [False, False, False]
        self.pressed_restart = [False, False, False]

