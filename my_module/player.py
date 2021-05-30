
import random

class BballPlayer():
    """ This class creates players with a name, offensive rating, and defensive rating"""
    
    
    def __init__(self, name, offense, defense):

        self.name = name
        self.offense = offense
        self.defense = defense
        self.points = 0

    def play(self, defender):
        """ Function takes one offensive player and one defensive player (the input) and compares the score of each by finding a random number from 0 to that players offensive/defensive rating. If the offensive number is higher than the defensive, the offensive player scores a point"""
        
        return random.randint(0, self.offense) > random.randint(0, defender.defense)
        
        
    def scoring(self, defender = 5):
        """lets the offensive player attempt to score on the defensive player 20 times, and returns the amount of points scored in total, as well as record the amount of points the individual player scored"""
        points = 0

        for i in range(20):
            points += 1 if self.play(defender) else 0
        self.points += points


        return points
    

# Full list of available players at the beginning of the game
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
    BballPlayer('Lebron James', 9, 7),
    BballPlayer('Kawhi Leonard', 8, 8),
    BballPlayer('Brandon Ingram', 7, 5),
    BballPlayer('Harrison Barnes', 5, 6),
    BballPlayer('Cam Reddish', 5, 4),
    BballPlayer('Anthony Davis', 8, 9),
    BballPlayer('Giannis Antetokounmpo', 8, 8),
    BballPlayer('Draymond Green', 4, 9),
    BballPlayer('John Collins', 7, 3),
    BballPlayer('Aaron Gordon', 5, 5),
    BballPlayer('Nikola Jokic', 9, 6),
    BballPlayer('Rudy Gobert', 4, 9),
    BballPlayer('Steven Adams', 5, 7),
    BballPlayer('James Wiseman', 7, 4),
    BballPlayer('Javale Mcgee', 5, 5),
]