# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass
        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")
            
            
class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
    
        
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        vowles = "aieouy"
        player1 = 0
        player2 = 0
        for character in player1_word:
            if character.lower() in vowles: 
                player1 += 1
        for character in player2_word:
            if character.lower() in vowles: 
                player2 += 1
        if player1 > player2: 
            return 1
        elif player2 > player1:
            return 2
        else: 
            return None
        

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        accepted = ["rock", "paper", "scissors"]
        player1_word = player1_word.lower()
        player2_word = player2_word.lower()
        if player1_word not in accepted and player2_word not in accepted: 
            return None
        if player1_word in accepted and player2_word not in accepted:
            return 1
        if player2_word in accepted and player1_word not in accepted:
            return 2
        if player1_word in accepted and player2_word in accepted:
            if player1_word == player2_word:
                return None
            if player1_word == "rock" and player2_word == "scissors":
                return 1
            if player1_word == "scissors" and player2_word == "paper": 
                return 1
            if player1_word == "paper" and player2_word == "rock":
                return 1
            else: 
                return 2
    
            
        

# p = RockPaperScissors(4)
# p.play()