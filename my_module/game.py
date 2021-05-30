
PG = "point guard"
SG = "shooting guard"
SF = "small forward"
PF = "power forward"
C = "center"


class Game:
    """ this class takes two teams as inputs for the method playgame()"""
    def __init__(self, team_a, team_b):

        self.team_a = team_a
        self.team_b = team_b


    def playgame(self):
        """ This function runs the simulation for each game once the two teams have been established.
        it begins by using the scoring functions from the player class to determine how many points each team scores. After each game the series record is updated and printed out. The series ends when either team reaches four wins.
        """
        game_counter = 0

        print('#######################################') # Creating top of outline box
        print('#                                     #')

        while self.team_a.wins < 4 and self.team_b.wins < 4:
        
            team_a_points = 0
            team_b_points = 0
            game_counter += 1
            
            #calculates how many points team a scores
            for k, i in enumerate(self.team_a.players.keys()):
                team_a_points += self.team_a.players[i].scoring(self.team_b.players[i])

            #calculates how many points team b scores
            for k, i in enumerate(self.team_b.players.keys()):
                team_b_points += self.team_b.players[i].scoring(self.team_b.players[i])

            
            if team_a_points > team_b_points:
                self.team_a.wins += 1 
                
            elif team_a_points < team_b_points:
                self.team_b.wins += 1
                
            else: # if the teams tie both teams recieve one win
                self.team_a.wins += 1
                self.team_b.wins += 1

            print('#     GM %d: %d-%d     Series: %d-%d     #' % (game_counter, team_a_points, team_b_points, self.team_a.wins, self.team_b.wins))

        print('#                                     #')
        print('#######################################') # Creating outline of box for final screen
        print('')


        if self.team_a.wins == 4:
            print(' Congrats! The %s win! %d-%d' % (self.team_a.name, self.team_a.wins, self.team_b.wins))
            scoring_leader(self.team_a, game_counter)
        else:
            print('Nice Try! the Computer wins this time :( %d-%d' % (self.team_a.wins, self.team_b.wins))
            scoring_leader(self.team_b, game_counter)
            
def scoring_leader(team, gamecount):
    """ Determines the player that scored the most points on the winning team"""
    highscorer = team.players[PG]
    
    for k, i in enumerate(team.players.keys()):
        if team.players[i].points > highscorer.points:
            highscorer = team.players[i]
            
    avgpoints = highscorer.points/gamecount
            
    print('The scoring leader was %s, averaging %d points per game!' % (highscorer.name, avgpoints))