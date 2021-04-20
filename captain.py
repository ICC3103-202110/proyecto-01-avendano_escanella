from influences import Influences
from player import Player

class Captain(Influences,Player):
    MIN_COIN=1
    MAX_COINS=2
    def __init__(self, name):
        super(Captain,self).__init__(name)

    def action_steal(player):
        mugged = str(input('Choose a player to steal coins from (Ex: Player1): '))
        if mugged == Player1.name:
            if Player1.coins == MIN_COIN:
                Player1.coins -= MIN_COIN
                player.coins += MIN_COIN
            else:
                Player1.coins -= MAX_COINS
                player.coins += MAX_COINS
        elif mugged == Player2.name:
            if Player2.coins == MIN_COIN:
                Player2.coins -= MIN_COIN
                player.coins += MIN_COIN
            else:
                Player2.coins -= MAX_COINS
                player.coins += MAX_COINS
        elif mugged == Player3.name:
            if Player3.coins == MIN_COIN:
                Player3.coins -= MIN_COIN
                player.coins += MIN_COIN
            else:
                Player3.coins -= MAX_COINS
                player.coins += MAX_COINS
        elif mugged == Player4.name:
            if Player4.coins == MIN_COIN:
                Player4.coins -= MIN_COIN
                player.coins += MIN_COIN
            else:
                Player4.coins -= MAX_COINS
                player.coins += MAX_COINS

    def counteract_stealing(blocker,player):
        print(f'{player.name} your attent for stealing was cancelled by Captian')
        opt=str(input(f'Do you want to challenge {blocked.name}? Options: yes / no: '))
        if opt=='yes':
            print('Tamos trabajando en ello')
        else:
            return 'Not_Today'