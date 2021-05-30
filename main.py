"""Script to run the project. Run this file in a terminal."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
import random
import time
from my_module.player import BballPlayer, PLAYERS
from my_module.team import Team, unassigned_players
from my_module.game import Game

PG = "point guard"
SG = "shooting guard"
SF = "small forward"
PF = "power forward"
C = "center"


# User creates their team name
print('Welcome to the fantasy basketball draft league!, to begin please give your team a name')
team_name = str(input('Name: '))

human = Team(team_name)
computer = Team("Computer")


# prints list of available players
for pos in human.players.keys():
    available = unassigned_players(PLAYERS, human, computer)
    for index, player in enumerate(available):

        print("%d-%s" % (index+1, player.name))


  #human choosing team  
    print("Please draft your %s from the list above by entering the corresponding number" % pos)
    chooseplayer = int(input('Choose your player! '))-1

    human.players[pos] = available[chooseplayer]
    print('You chose %s!' % available[chooseplayer].name)

    available.remove(available[chooseplayer])

    #computer choosing team
    computer.players[pos] = random.choice(available)

# displaying user's team
print('')
print('Your team is called the %s, and its players are:' % human.name)
for k, i in enumerate(human.players.keys()):
    print ('%s' % human.players[i].name)
print('')

#displaying opponent team    
print('Your opponent\'s team is:')
for k, i in enumerate(computer.players.keys()):
    print('%s' % computer.players[i].name)
print('')

#Beginning Simulation
print('Beginning Simulation...')
for i in range(4):
    print('.'*i)
    time.sleep(2)
print('')

# Simulating Game    
the_game = Game(human, computer)
the_game.playgame()
