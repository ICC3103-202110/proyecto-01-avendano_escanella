from influences import Influences
from player import Player
from challenge import Challenge

class Captain(Influences):
    
    def __init__(self, name):
        super(Captain,self).__init__(name)

    def steal_1():
        value=1
        return value

    def steal_2():
        value=2
        return value

        
    def counteract_stealing(blocker,player,deck):
        print(f'{player.name} your attent for stealing was cancelled by Captain')
        opt=str(input(f'Do you want to challenge {blocker.name}? Options: yes / no: '))
        if opt=='yes':
            valid,deck=Challenge.challenge_counteraction(player, blocker,'Captain',deck)
            return valid,deck
        else:
            return 'Not_Today',deck