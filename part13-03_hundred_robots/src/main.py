# WRITE YOUR SOLUTION HERE:


import pygame


pygame.init()
window = pygame.display.set_mode((640, 480))


robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((250,90,170))

x = 0
y = 50
z = 0

for i in range(100):
    if i % 10 == 0:
        y += height // 4
        x = 50 + z
        z += 10 
    window.blit(robot, (x,y ))
    x += width - 8
    
    
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()