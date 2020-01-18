import random
from classes.player import Player
from classes.match import Match

super_skills = {'perimeter_d': 20, 'post_d': 20, 'three_point': 20, 'midrange': 20, 'layup': 20, 'dunk': 20}

potential_opponents = [Player("Generico"), Player("MJ", super_skills)]

# Shootaround test app
# while True:
#     name = input("Please enter your name: ")
#     points = 0
#     player_one = Player(name)
#     if name in ["Steph", "Curry", "Klay", "Jesus", "Shuttlesworth"]:
#         player_one.skills['three_point'] = 20

#     factor = random.randrange(1,25)
#     if player_one.skills['three_point'] >= factor:
#         success_messages = ["It's good from downtown!", "Bang! Bang! Bang!", "Give them all three of those!"]
#         print(random.choice(success_messages))
#         points += 3
#     else:
#         failure_messages = ["Brick!", "That's way off from three!", "Off on the jumpshot"]
#         print(random.choice(failure_messages))
    
#     print(f"{name} scored {points} points. Thanks for playing!")
#     break

# Game involving actual match
while True:
    name = input("Please enter your name: ")
    player_one = Player(name)
    opponent = input("Please choose your opponent: [0] Generico [1] Michael Jeffrey Jordan")
    new_match = (player_one, potential_opponents[opponent])