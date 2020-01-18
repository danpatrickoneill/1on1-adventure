import random
from classes.player import Player
from classes.match import Match


print(player_one.skills)

while True:
    name = input("Please enter your name: ")
    points = 0
    player_one = Player(name)
    if name in ["Steph", "Curry", "Klay", "Jesus", "Shuttlesworth"]:
        player_one.skills['three_point'] = 20

    factor = random.randrange(1,25)
    if player_one.skills['three_point'] >= factor:
        success_messages = ["It's good from downtown!", "Bang! Bang! Bang!", "Give them all three of those!"]
        print(random.choice(success_messages))
        points += 3
    else:
        failure_messages = ["Brick!", "That's way off from three!", "Off on the jumpshot"]
        print(random.choice(failure_messages))
    
    print(f"{name} scored {points} points. Thanks for playing!")
