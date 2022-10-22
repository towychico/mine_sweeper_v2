class GameSession:
    def __init__(self):
        self.board = []
        self.game_is_paused = False
        self.game_over = False
        self.time = 0
        self.number_of_marked_mines = 0
        self.initial_click_cords = None
        self.marked_mines = None
        self.number_of_clicks = 0
        self.sprites_scale = 1.0

