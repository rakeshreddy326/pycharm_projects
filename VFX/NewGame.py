import pygame

from pygame.locals import (
K_LEFT,
K_RIGHT,
K_UP,
K_DOWN,
K_ESCAPE,
KEYDOWN,
QUIT,
)
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

screen.fill((255, 255, 255))
surf = pygame.Surface((50, 50))

surf.fill((0, 0, 0))
rect = surf.get_rect()

screen.blit(surf, (WIDTH/2, HEIGHT/2))
pygame.display.flip()

surf_center = (
    (WIDTH-surf.get_width())/2,
    (HEIGHT-surf.get_height())/2
)

# Draw surf at the new coordinates
screen.blit(surf, surf_center)
pygame.display.flip()

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()