import pygame

#Création de joueur

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('sprites/knight.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        self.rect.y -= 0.000000001