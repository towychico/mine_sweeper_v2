import pygame


CELL_SPRITE_LIST = ['./sprites/0.png', './sprites/1.png', './sprites/2.png', './sprites/3.png', './sprites/4.png',
                    './sprites/5.png', './sprites/6.png', './sprites/7.png', './sprites/8.png', './sprites/-2.png',
                    './sprites/-1.png']


class Cell(pygame.sprite.Sprite):
    """
    The Cell class defines a cell object, it handles all the logic and data of each individual cell
    """
    def __init__(self, row, col, number, x_pos, y_pos,game_session):
        pygame.sprite.Sprite.__init__(self)
        self.game_session = game_session
        self.image_raw = pygame.image.load('./sprites/cell.png')
        self.image = pygame.transform.scale(self.image_raw,(70*game_session.sprites_scale, 70*game_session.sprites_scale))
        self.rect = self.image.get_rect(topleft=(x_pos * game_session.sprites_scale,
                                                 y_pos * game_session.sprites_scale))
        self.x_pos = x_pos * game_session.sprites_scale
        self.y_pos = y_pos * game_session.sprites_scale
        self.row = row
        self.col = col
        self.number = int(number)
        self.is_flagged = False
        self.is_expose = False
        self.is_mine = self.check_for_mine()

    def flag(self):
        """
        The flag function is used to flag a cell as a mine.
        It takes no arguments and returns nothing.

        :param self: Access the attributes and methods of the class in python
        :return: The value of the is_flagged attribute, which is a boolean
        :doc-author: Trelent
        """
        self.is_flagged = True
        self.game_session.number_of_flagged_mines += 1
        self.number = -2
        self.update_sprite()

    def exposed(self):
        """
        The exposed function is used to expose a cell, it changes the value of the is_expose instance variable to True.

        :param self: Access the attributes and methods of the class in python
        :return: The value of the is_expose attribute
        :doc-author: Trelent & Lou, Luis
        """

        self.is_expose = True

    def update_sprite(self):
        """
        The update_sprite function updates the sprite image of a cell.
        It takes in self as an argument, and uses the number attribute to access a list of sprites.
        The function then changes the sprite image to match its state.

        :param self: Refer to the object that is calling the function
        :return: The image of the cell
        :doc-author: Trelent
        """
        self.exposed()

        self.image = pygame.image.load(CELL_SPRITE_LIST[self.number])
        if self.is_mine:
            print("game Over")



    def check_for_mine(self):
        """
        The check_for_mine function checks to see if the number of a tile is - 1.
        if it is: it returns True
        :param self: Access the attributes and methods of the class
        :return: True if the cell has a mine and false otherwise
        :doc-author: Trelent & Lou, Luis
        """

        if self.number == -1:
            return True
