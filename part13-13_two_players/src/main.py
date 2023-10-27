# WRITE YOUR SOLUTION HERE:



# WRITE YOUR SOLUTION HERE:



import pygame


def handle_movement(robot_stats: dict, movements: dict, triggerred_events: list):
    robot = pygame.image.load("robot.png")
    width = robot.get_width()
    height = robot.get_height()
    print(height, width)
    for event in triggerred_events:
        if event.type == pygame.KEYDOWN:
            if event.key == movements["LEFT"]:
                robot_stats["to_left"] = True
            if event.key == movements["RIGHT"]:
                robot_stats["to_right"] = True
            if event.key == movements["UP"]:
                robot_stats["up"] = True
            if event.key == movements["DOWN"]:
                robot_stats["down"] = True
                
        if event.type == pygame.KEYUP:
            if event.key == movements["LEFT"]:
                robot_stats["to_left"] = False
            if event.key == movements["RIGHT"]:
                robot_stats["to_right"] = False
            if event.key == movements["UP"]:
                robot_stats["up"] = False
            if event.key == movements["DOWN"]:
                robot_stats["down"] = False
                
    if robot_stats["x"] + width >= 640:
        robot_stats["to_right"] = False
    if robot_stats["x"] <= 0:
        robot_stats["to_left"] = False
    if robot_stats["y"] + height >= 480:
        robot_stats["down"] = False
    if robot_stats["y"] <= 0:
        robot_stats["up"] = False
    
    if robot_stats["to_right"]:
        robot_stats["x"] += 2
    if robot_stats["to_left"]:
        robot_stats["x"] -= 2
    if robot_stats["up"]:
        robot_stats["y"] -= 2
    if robot_stats["down"]:
        robot_stats["y"] += 2

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot1 = {"x": 0, "y": 0, "to_right": False, "to_left": False, "up": False, "down": False}
robot2 = {"x": 100, "y": 100, "to_right": False, "to_left": False, "up": False, "down": False}


clock = pygame.time.Clock()

while True:
    triggerred_events = pygame.event.get()
    
    for event in triggerred_events:
        if event.type == pygame.QUIT:
            exit()  
            
    handle_movement(robot1, {"LEFT": pygame.K_LEFT, "RIGHT": pygame.K_RIGHT, "UP": pygame.K_UP, "DOWN": pygame.K_DOWN}, triggerred_events)
    handle_movement(robot2, {"LEFT": pygame.K_a, "RIGHT": pygame.K_d, "UP": pygame.K_w, "DOWN": pygame.K_s}, triggerred_events)
        

    window.fill((200, 150, 200))
    window.blit(robot, (robot1["x"], robot1["y"]))
    window.blit(robot, (robot2["x"], robot2["y"]))
    pygame.display.flip()

    clock.tick(60)          
    

                
        