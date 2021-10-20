import pygame
from game import Game

#import time

pygame.init() # initialiser pygame





# générer la fenêtre du jeu

pygame.display.set_caption('Doodle Jump')# Titre et icône

screen = pygame.display.set_mode((1080, 700)) # Taille de la fenêtre(Tuple)

background = pygame.image.load('sprites/BG_03.png')

# charger le je
game = Game()



running = True

# Boucle du demmareur
sens = 0
compteur = 1
clock = pygame.time.Clock()
while running:

    # appliquer l'arrière plan

    screen.blit(background, (0,  -250))

    # appliquer le joueur

    screen.blit(game.player.image, game.player.rect)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        sens = 0
        game.player.move_right()
        game.player.image = pygame.image.load('sprites/Run_right/run{}.png'.format(compteur))
        compteur += 1
        if compteur == 8:
            compteur = 1
    

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        sens = 1
        game.player.move_left()
        game.player.image = pygame.image.load('sprites/Run_left/run{}.png'.format(compteur))
        compteur += 1
        if compteur == 8:
            compteur = 1


    # mettre a jour son écran
    pygame.display.flip()

    # fermeture de fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # fermeture
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            if sens == 0:
                game.player.image = pygame.image.load('sprites/knight.png')
            elif sens == 1:
                game.player.image = pygame.image.load('sprites/knightl.png')

    pygame.display.update()
    clock.tick(30)

