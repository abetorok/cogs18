PG = "point guard"
SG = "shooting guard"
SF = "small forward"
PF = "power forward"
C = "center"

class Team:
    """ creates a dictionary with the five basketball positions, as well as a team name
    Example: 
    my_team = Team('UCSD Tritons')
    my_team.name
    >>> 'UCSD Tritons'
    """
    
    
    def __init__(self, name):

        self.name = name
        self.players = {
            PG: None,
            SG: None,
            SF: None,
            PF: None,
            C: None,
        }
        self.wins = 0

        
def unassigned_players(players, team_a, team_b):
    """ looks through list of all players and removes players that have been picked already"""
    
    playerlist = []

    for player in players:
        if player not in team_a.players.values() and player not in team_b.players.values():
            playerlist.append(player)

    return playerlist