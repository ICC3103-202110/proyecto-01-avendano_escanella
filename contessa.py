from influences import Influences
from player import Player
from challenge import Challenge

class Contessa(Influences):
    def __init__(self, name):
        super(Contessa,self).__init__(name)
    
    def counteract_assassin(blocker,player,deck):
        print(f'{player.name} your assassination was counteracted by Contessa')
        opt=str(input(f'Do you want to challenge {blocker.name}? Options: yes / no: '))
        if opt=='yes':
            valid,deck =Challenge.challenge_counteraction(player, blocker,'Contessa',deck)
            return valid,deck
        else:
            return 'Not_Today',deck