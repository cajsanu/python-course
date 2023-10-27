# WRITE YOUR SOLUTION HERE:


import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 320
y = 240
x_speed = 1
y_speed = 1
clock = pygame.time.Clock()

size = ball.get_height()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((50, 50, 50))
    window.blit(ball, (x, y))
    pygame.display.flip()
    
    x += x_speed
    y += y_speed
    
    if x_speed > 0 and y_speed > 0:
        if y + size >= 480:
            y_speed = -y_speed
        elif x + size >= 640:
            x_speed = -x_speed
              
    if x_speed > 0 and y_speed < 0:
        if x + size >= 640: 
            x_speed = -x_speed
        elif y <= 0:
            y_speed = -y_speed
        
    if x_speed < 0 and y_speed < 0:
        if y <= 0:
            y_speed = -y_speed
        elif x <= 0:
            x_speed = -x_speed
        
    if x_speed < 0 and y_speed > 0:
        if x <= 0:
            x_speed = -x_speed
        elif y + size >= 480:
            y_speed = -y_speed
        
            
       
        
        

        
        
    
    # y and x increase or decrease by one
    
    # if y > 240 and x_velocity < 0:
        
    
    # if velocity > 0 and x+robot.get_width() >= 640:
    #     velocity = -velocity
    # if velocity < 0 and x <= 0:
    #     velocity = -velocity

    clock.tick(60)