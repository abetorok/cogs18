""" Tests for functions and classes"""

from player import BballPlayer
from team import Team, unassigned_players
from game import Game, scoring_leader

PG = "point guard"
SG = "shooting guard"
SF = "small forward"
PF = "power forward"
C = "center"

PLAYERS = [
    BballPlayer('Stephen Curry', 10, 4),
    BballPlayer('Ben Simmons', 6, 8),
    BballPlayer('Marcus Smart', 4, 8),
    BballPlayer('Ricky Rubio', 6, 3),
    BballPlayer('Markelle Fultz', 5, 5),
    BballPlayer('Klay Thompson', 8, 7),
    BballPlayer('Jaylen Brown', 7, 6),
    BballPlayer('Demar Derozan', 7, 4),
    BballPlayer('Buddy Hield', 7, 3),
    BballPlayer('Don Smith', 3, 6),
]


def test_BballPlayer():
    
    carson = BballPlayer('Carson Miller', 10, 10)
    abe = BballPlayer('Abraham Torok', 5, 8)

    assert isinstance(carson.defense, int)
    assert carson.defense == 10

    
def test_Team():
    
    my_team = Team('my team')
    my_team.players[PG] = BballPlayer('Stephen Curry', 10, 4)
    
    assert my_team.name == 'my team'
    
    assert my_team.players[SG] == None
    
    assert isinstance(my_team.players, dict)
    
    
def test_unassigned_players():
    
    my_team = Team('my team')
    my_team.players[PG] = PLAYERS[1]
    
    other_team = Team('other team')
    other_team.players[PG] = PLAYERS[2]

    newplayerlist = unassigned_players(PLAYERS, my_team, other_team)
    
    assert len(newplayerlist) == 8
    
    assert isinstance(newplayerlist, list)
    
    assert PLAYERS[2] not in newplayerlist
    
    
test_BballPlayer()    
test_Team()    
test_unassigned_players()

print('hello')




                 
    