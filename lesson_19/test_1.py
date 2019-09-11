'''Научите шарик отскакивать от стенок. Постарайтесь также сделать, чтоб шарик не залетал за края экрана (самым простым, нафизичным способом).'''

import sys
import pygame

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

x = 30
y = 30
vx = 50
vy = 50
check = 1

while True:
    
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            sys.exit()

    if x >= 480 or y >= 480:
        check = -1

    if x <= 20 or y <= 20:
        check = 1

    if check == -1:
        x -= vx * dt
        y -= vy * dt
    else:
        x += vx * dt
        y += vy * dt

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 10, 50), (int(x), int(y)), 20)

    pygame.display.flip()