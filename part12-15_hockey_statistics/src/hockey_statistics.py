# Write your solution here
import json

def commands():
    print("commands: ")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")
    
def print_stats(player):
    print(f'{player["name"]:20} {player["team"]} {player["goals"]:3} {"+"} {player["assists"]:2} {"="} {player["goals"] + player["assists"]:>3}')
    
def get_player(players: list, name:str):
    player = [player for player in players if player["name"] == name]
    return player[0]
    
def all_teams(players: list):
    return sorted(set([player["team"] for player in players]))

def get_nationalities(players: list):
    return sorted(set([player["nationality"] for player in players]))

def players_in_team(players: list, team: str):
    players_in_team = [player for player in players if player["team"] == team]
    ordered = sorted(players_in_team, key=(lambda player : player["goals"] + player["assists"]), reverse=True)
    for p in ordered: 
        print_stats(p)
        
def players_in_country(players: list, country: str):
    players_in_country = list(filter(lambda player : player["nationality"] == country, players))
    ordered = sorted(players_in_country, key=(lambda player : player["goals"] + player["assists"]), reverse=True)
    for p in ordered: 
        print_stats(p)
        
def most_points(players: list, amount: int):
    ordered = list(sorted(players, key=(lambda player : (player["goals"] + player["assists"], player["goals"])), reverse=True))
    counter = 0 
    for p in ordered: 
        if counter < amount:
            print_stats(p)
            counter += 1
            
def most_goals(players: list, amount: int):
    ordered = list(sorted(players, key=(lambda player : (player["goals"], -(player["games"]))), reverse=True))
    counter = 0 
    for p in ordered: 
        if counter < amount:
            print_stats(p)
            counter += 1
   
def main():
    file_name = input("file name: ")
    with open(file_name) as file: 
        data = file.read()
        players = json.loads(data)
    print (f"read the data of {len(players)} players")
    
    commands()
    
    while True:
        command = input("command: ")
        
        if command == "0":
            break
        
        if command == "1":
            name = input("name: ")
            player = get_player(players, name)
            print_stats(player)
            
        if command == "2": 
            teams = all_teams(players)
            for team in teams:
                print(team)
                
        if command == "3":
            nationalities = get_nationalities(players)
            for n in nationalities:
                print(n)
                
        if command == "4":
            team = input("team: ")
            players_in_team(players, team)
            
        if command == "5":
            country = input("country: ").upper()
            if not len(country) == 3:
                print("not valid input")
            players_in_country(players, country)
            
        if command == "6":   
            amount = int(input("how many? "))
            most_points(players, amount)
    
        if command == "7":   
            amount = int(input("how many? "))
            most_goals(players, amount)

    

main()