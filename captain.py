from influences import Influences


class Captain(Influences,Player):
    MIN_COIN=1
    MAX_COINS=2
    def __init__(self, name):
        super(Captain,self).__init__(name)

    def steal_1():
        value=1
        return value

    def steal_2():
        value=2
        return value

        
    def counteract_stealing(blocker,player):
        print(f'{player.name} your attent for stealing was cancelled by Captian')
        opt=str(input(f'Do you want to challenge {blocked.name}? Options: yes / no: '))
        if opt=='yes':
            print('Tamos trabajando en ello')
        else:
            return 'Not_Today'