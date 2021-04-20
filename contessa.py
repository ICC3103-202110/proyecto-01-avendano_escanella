from influences import Influences


class Contessa(Influences,Player):
    def __init__(self, name):
        super(Contessa,self).__init__(name)
    
    def counteract_assassin(blocker,player):
        print(f'{player.name} your assassination was counteracted by Contessa')
        opt=str(input(f'Do you want to challenge {blocked.name}? Options: yes / no: '))
        if opt=='yes':
            print('Tamos trabajando en ello')
        else:
            return 'Not_Today'