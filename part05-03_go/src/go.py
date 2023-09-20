# Write your solution here

def who_won (game_board: list):
    p_one = 0
    p_two = 0

    for list in game_board:
        for item in list:
            if item == 1:
                p_one += 1
            if item == 2:
                p_two += 1
        
    if p_one == p_two:
      return 0
    elif p_one > p_two:
        return 1
    else: 
        return 2
    
if __name__ == "__main__":
    game = [[0, 2, 0], [0, 2, 1], [1, 0, 2]]
    print(who_won(game))


    
      

