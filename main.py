import game_session_handler
import map_handler
import math
from game_session_handler import GameSession
import pygame
pygame.init()

import datetime


def fix_map(upper_i,lower_i):
    global game_map
    if game_session.number_of_clicks == 0 and game_map.board[upper_i][lower_i].number !=0:

        valid_map = False
        while not valid_map:
            del game_map

            game_map = map_handler.Map(12, 12, game_session)

            if game_map.board[upper_i][lower_i].number == 0:
                valid_map = True




def adjust_dimensions():
    screen = pygame.display.set_mode()
    screen_width, screen_height = screen.get_size()
    if screen_height <= 670 and screen_width <= 1280:
        return 0.22
    if screen_height <= 770 and 1280 < screen_width <= 1440:
        return 0.38
    if 770 < screen_height <= 1080 and screen_width <= 1920:
        return 0.59
    if 1310 < screen_height < 1870:
        return 0.85
    if 1870 < screen_height:
        return 1.0


initial_scale = adjust_dimensions()
BACKGROUND_COLOR = (255, 255, 255)
(width, height) = (855 * initial_scale, 1100 * initial_scale)
window = pygame.display.set_mode((width, height))
game_session = GameSession(window, scale=initial_scale)
pygame.display.set_caption("Minesweeper")
window.fill(BACKGROUND_COLOR)
pygame.display.flip()


title_img = pygame.image.load("./sprites/Title.png")
title_img = pygame.transform.scale(title_img, (504*game_session.sprites_scale, 69*game_session.sprites_scale))

clock_img = pygame.image.load("./sprites/Clock.png")
clock_img = pygame.transform.scale(clock_img, (46*game_session.sprites_scale, 46*game_session.sprites_scale))

flag_img = pygame.image.load("./sprites/Flag.png")
flag_img = pygame.transform.scale(flag_img, (46*game_session.sprites_scale, 46*game_session.sprites_scale))

font = pygame.font.Font("./fonts/Indigo.otf", math.ceil(40*game_session.sprites_scale))


def update_game_ui():
    """
    The update_game_ui function updates the UI game elements on the screen. It draws the title, clock,  flag and cell
    sprites to the screen.

    :return:Nothing:
    :doc-author: Trelent & Lou
    """

    window.blit(title_img, (185*game_session.sprites_scale, 25*game_session.sprites_scale))
    window.blit(clock_img, (185*game_session.sprites_scale, 135*game_session.sprites_scale))
    #I ran out of time for implementing this :(
    #window.blit(flag_img, (550*game_session.sprites_scale, 135*game_session.sprites_scale))
    game_map.update_cells()



def check_for_game_inputs():
    global start_ticks2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_session.game_is_running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()

            try:
                upper_i, lower_i = game_map.get_cell_position((mouse_x, mouse_y))
                if game_session.number_of_clicks == 0:
                    fix_map(upper_i, lower_i)
                    game_map.flood_fill_BFS(game_map.board, upper_i, lower_i)
                    game_map.check_for_sourrondedd_mines()
                else:
                    game_map.show_cell(upper_i,lower_i)
                    game_map.check_for_sourrondedd_mines()
                print('\n')
                print(game_map.matrix)
            except:
                pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_session.game_is_paused = not game_session.game_is_paused
                start_ticks2 = pygame.time.get_ticks()
                print("paused")


def check_for_app_inputs():
    global start_ticks2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_session.game_is_running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_session.game_is_paused = not game_session.game_is_paused
                start_ticks2 = pygame.time.get_ticks()
                print("paused")

game_map = map_handler.Map(12, 12,game_session)
start_ticks = pygame.time.get_ticks()

seconds_after_pause = 0

temp = 0
while game_session.game_is_running:




    pygame.display.flip()
    window.fill((255, 255, 255))
    seconds = math.floor((pygame.time.get_ticks() - start_ticks) / 1000)
    if not game_session.game_is_paused:
        #- seconds_after_pause
        print(seconds)

        format_time = str(datetime.timedelta(seconds=math.floor(seconds - game_session.time)))

        timer_text = font.render(format_time, True, (0, 0, 0))
        window.blit(timer_text, (285*game_session.sprites_scale, 150*game_session.sprites_scale))
        update_game_ui()

        check_for_game_inputs()
    else:

        seconds_after_pause = math.floor((pygame.time.get_ticks()-start_ticks) / 1000)
        game_session.time =  seconds_after_pause
        print(seconds_after_pause)
        paused_label = font.render("Paused ", True, (0, 0, 0))
        window.blit(paused_label, (285 * game_session.sprites_scale, 150 * game_session.sprites_scale))
        check_for_app_inputs()
        update_game_ui()


