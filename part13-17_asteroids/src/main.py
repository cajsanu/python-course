# WRITE YOUR SOLUTION HERE:


import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

robot_width = robot.get_width()
robot_height = robot.get_height()

rock_width = rock.get_width()
rock_height = rock.get_height()

robot_x = 320
robot_y = 480-robot_height

to_right = False
to_left = False

speed = 1
counter = 0

rock_positions = []

# init starting positions of rocks
for i in range(10):
    rock_positions.append({ 'x': randint(0,640), 'y': randint(-400,0) })

clock = pygame.time.Clock()

while True:
    window.fill((200, 20, 250))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
                
        if event.type == pygame.QUIT:
            exit()
                
    if robot_x + robot_width >= 640:
        to_right = False
    if robot_x <= 0:
        to_left = False
        
    if to_right:
        robot_x += 3
    if to_left:
        robot_x -= 3
            
    for i in rock_positions:
        # move the rock to the bottom
        i['y'] += speed
        window.blit(rock, (i['x'], i['y']))
        if i["y"] + rock_height > robot_y and i["x"] + rock_width > robot_x and i["x"] < robot_x + robot_width: 
            i["y"] = randint(-400,0)
            i["x"] = randint(0, 640)
            counter += 1
            
        if i["y"] + rock_height > 480:
            exit()
         
            
    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {counter}", True, (0, 0, 0))
    window.blit(text, (500, 10))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)