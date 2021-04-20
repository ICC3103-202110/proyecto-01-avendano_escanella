from influences import Influences
from player import Player
class Duke (Influences):

    #Constructor
    def __init__(self, name):
        super(Duke,self).__init__(name)

    #Métodos
    def tax():
        value=3
        return value

    
    def counteract_FA(blocker,player):
        print(f'{player.name} your petition for foreign aid was cancelled by Duke')
        opt=str(input(f'Do you want to challenge {blocked.name}? Options: yes / no: '))
        if opt=='yes':
            print('Tamos trabajando en ello')
        else:
            return 'Not_Today'

