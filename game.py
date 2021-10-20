import pygame
from player import Player

# la classse du jeu
class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {}