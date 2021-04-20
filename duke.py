from influences import Influences
from player import Player
from challenge import Challenge

class Duke (Influences):

    #Constructor
    def __init__(self, name):
        super(Duke,self).__init__(name)

    #Métodos
    def tax():
        value=3
        return value

    
    def counteract_FA(blocker,player,deck):
        print(f'{player.name} your petition for foreign aid was cancelled by Duke')
        opt=str(input(f'Do you want to challenge {blocker.name}? Options: yes / no: '))
        if opt=='yes':
            valid,deck=Challenge.challenge_counteraction(player, blocker,'Duke',deck)
            return valid,deck
        else:
            return 'Not_Today',deck

