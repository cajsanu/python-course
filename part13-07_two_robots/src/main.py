# WRITE YOUR SOLUTION HERE:



import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

height = robot.get_height()
width = robot.get_width()

x1 = 0
y1 = 50
x2 = 0
y2 = 100
velocity = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((50, 200, 140))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))

    pygame.display.flip()
    
    x1 += velocity
    if velocity > 0 and x1+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x1 <= 0:
        velocity = -velocity
        
    x2 += velocity*2
    if velocity > 0 and x2+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x2 <= 0:
        velocity = -velocity

    clock.tick(60)