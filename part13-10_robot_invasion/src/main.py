# WRITE YOUR SOLUTION HERE:



import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

height = robot.get_height()
width = robot.get_width()

clock = pygame.time.Clock()

speed = 1

robot_positions = []

# init starting positions of robots
for i in range(10):
    robot_positions.append({ 'x': randint(0,640), 'y': randint(-400,0) })


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((50, 250, 150))
  
    for i in range(10):
        # if robot reached the bottom, we don't move him down
        if robot_positions[i]['y'] + height >= 480:
            if robot_positions[i]['x'] >= 320:
                robot_positions[i]['x'] += speed
            elif robot_positions[i]['x'] < 320:
                robot_positions[i]['x'] -= speed
        # otherwise move robot down
        else:
            # move the robot to the bottom
            robot_positions[i]['y'] += speed
         
        window.blit(robot, (robot_positions[i]['x'], robot_positions[i]['y']))
        
    pygame.display.flip()
    clock.tick(60)
   
       