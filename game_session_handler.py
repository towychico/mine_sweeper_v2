class GameSession:
    def __init__(self,window_object, pause=False, game_is_over=False, scale=1.0):
        self.window = window_object
        self.game_is_paused = pause
        self.game_over = game_is_over
        self.time = 0
        self.number_of_flagged_mines = 0
        self.number_of_mines = 0
        self.mines_positions = []
        self.initial_click_cords = []
        self.marked_mines = []
        self.number_of_clicks = 0
        self.sprites_scale = scale
        self.game_is_running = True

