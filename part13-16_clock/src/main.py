# WRITE YOUR SOLUTION HERE:

import pygame
import math
from datetime import datetime, time

pygame.init()
display = pygame.display.set_mode((200, 200))

clock = pygame.time.Clock()

time = datetime.now().strftime('%H:%M:%S')
time = time.split(":")
        
s_angle = (math.pi*2/60*int(time[2])) - math.pi/2
m_angle = (math.pi*2/60*int(time[1])) - math.pi/2
h_angle = (math.pi*2/12*(int(time[0])%12)) - math.pi/2

while True:
    
    pygame.display.set_caption(datetime.now().strftime('%H:%M:%S'))
    display.fill((150, 220, 255))
    
    pygame.draw.circle(display, (5, 140, 250), (100, 100), 80)
    pygame.draw.circle(display, (2, 90, 115), (100, 100), 75)
    pygame.draw.circle(display, (5, 140, 250), (100, 100), 5)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    x = 100+math.cos(s_angle)*65
    y = 100+math.sin(s_angle)*65
    pygame.draw.line(display, (250, 230, 5), (100, 100), (x, y), 2)
    
    z = 100+math.cos(m_angle)*65
    q = 100+math.sin(m_angle)*65
    pygame.draw.line(display, (95, 245, 125), (100, 100), (z, q), 2)
    
    n = 100+math.cos(h_angle)*40
    m = 100+math.sin(h_angle)*40
    pygame.draw.line(display, (255, 140, 50), (100, 100), (n, m), 3)
    
    s_angle += (math.pi*2)/60
    m_angle += (math.pi*2)/60/60
    h_angle += (math.pi*2)/60/60/60
    
    pygame.display.flip()
    clock.tick(1)
    