

import map_handler
import math
from game_session_handler import GameSession
import pygame
pygame.init()

import datetime
temporal_scale = 0.5
BACKGROUND_COLOR = (255, 255, 255)
(width, height) = (855 * temporal_scale, 1100 * temporal_scale)
window = pygame.display.set_mode((width, height))
game_session = GameSession(window, scale=temporal_scale)
pygame.display.set_caption("Minesweeper")
window.fill(BACKGROUND_COLOR)
pygame.display.flip()


title_img = pygame.image.load("./sprites/Title.png")
title_img = pygame.transform.scale(title_img, (504*game_session.sprites_scale, 69*game_session.sprites_scale))
#1.5217
clock_img = pygame.image.load("./sprites/Clock.png")
clock_img = pygame.transform.scale(clock_img, (46*game_session.sprites_scale, 46*game_session.sprites_scale))

flag_img = pygame.image.load("./sprites/Flag.png")
flag_img = pygame.transform.scale(flag_img, (46*game_session.sprites_scale, 46*game_session.sprites_scale))

font = pygame.font.Font("./fonts/Indigo.otf", math.ceil(40*game_session.sprites_scale))


def update_ui():
    """
    The update_ui function updates the UI elements on the screen. It draws the title, clock, and flag images to
    the screen.

    :return: A tuple of the following items:
    :doc-author: Trelent
    """

    window.blit(title_img, (185*game_session.sprites_scale, 25*game_session.sprites_scale))
    window.blit(clock_img, (185*game_session.sprites_scale, 135*game_session.sprites_scale))
    window.blit(flag_img, (550*game_session.sprites_scale, 135*game_session.sprites_scale))

game_map = map_handler.Map(12, 12,game_session)
while game_session.game_is_running:
    pygame.display.flip()
    window.fill((255, 255, 255))
    update_ui()
    game_map.update_cells()
