# # WRITE YOUR SOLUTION HERE:


import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

height = robot.get_height()
width = robot.get_width()

x = 0
y = 0
velocity_x = 1
velocity_y = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((200, 100, 140))
    window.blit(robot, (x, y))
    # window.blit(robot, (randint(200, 400), randint(200, 400)))

    pygame.display.flip()
    
    
    if velocity_x > 0 and y <= 0:
        x += velocity_x
        velocity_y = 1
        
    if velocity_y > 0 and x+width >= 640:
        y += velocity_y
        velocity_x = -velocity_x
        
    if velocity_x < 0 and y+height >= 480:
        x += velocity_x
        velocity_y = -velocity_y
          
    if velocity_y < 0 and x <= 0:
        y += velocity_y
        velocity_x = 1

    clock.tick(60)