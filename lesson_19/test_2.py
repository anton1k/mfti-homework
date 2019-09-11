'''Добавим управление: пусть при нажатой клавише-стрелке, у шарика появляется ускорение в соответствующую сторону. Испульзуйте список pygame.key.get_pressed().'''

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
checkX = 1
checkY = 1

while True:
    
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vx += 5
            if event.key == pygame.K_LEFT:
                vx -= 5
            if event.key == pygame.K_UP:
                vy += 5
            if event.key == pygame.K_DOWN:
                vy -= 5

    if x > 480:
        checkX = -1
    elif x < 20:
        checkX = 1

    if y > 480:
        checkY = -1
    elif y < 20:
        checkY = 1

    if checkX == -1:
        x -= vx * dt
    else:
        x += vx * dt

    if checkY == -1:
        y -= vy * dt
    else:
        y += vy * dt

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 10, 50), (int(x), int(y)), 20)

    pygame.display.flip()