##
# Interactive 2D Animation
##

import pygame, random, sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

bubbles = [[random.randint(0,800), random.randint(0,600), random.randint(10,50)] for _ in range(30)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 20))
    for b in bubbles:
        pygame.draw.circle(screen, (100, 200, 255), (b[0], b[1]), b[2])
        b[1] -= 1
        if b[1] < -b[2]:
            b[1] = 600 + b[2]

    pygame.display.flip()
    clock.tick(60)
