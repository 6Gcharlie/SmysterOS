"""
This file contains all of the inner workings of the overworld
"""

import pygame

def world(game):
    "The function is entirely responsible for a majority of the game"

    game.get_prev_time()

    while game.loop == "world":

        game.delta_clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.loop = "NA"

            game.events(event)

        game.surface.fill([100, 100, 100])
        game.draw()
