from influences import Influences
from player import Player
class Assassin(Influences,Player):
    COST = 3
    def __init__(self, name):
        super(Assassin,self).__init__(name)
    
    #Métodos
    def action_assassinate(player):
        if player.coins<COST:
            print(f'You can´t assassinate because you have ¢{player.coins} coins')
        else:
            victim=str(input('Choose a player to assassinate (Ex: Player1): '))
            if victim== Player1.name:
                print(f'{victim} choose a card to reveal')
                print(f'1: {Player1.card1} or 2: {Player1.card2}')
                card_reveal=str(input())
                if card_reveal=='1':
                    reveal= Player1.card1
                    Player1.card1=None
                    Player1.card1_reveal=reveal
                else:
                    reveal=Player1.card2
                    Player1.card2=None
                    Player1.card2_reveal=reveal

            elif victim== Player2.name:
                print(f'{victim} choose a card to reveal')
                print(f'1: {Player2.card1} or 2: {Player2.card2}')
                card_reveal=str(input())
                if card_reveal=='1':
                    reveal= Player2.card1
                    Player2.card1=None
                    Player2.card1_reveal=reveal
                else:
                    reveal=Player2.card2
                    Player2.card2=None
                    Player2.card2_reveal=reveal

            elif victim== Player3.name:
                print(f'{victim} choose a card to reveal')
                print(f'1: {Player3.card1} or 2: {Player3.card2}')
                card_reveal=str(input())
                if card_reveal=='1':
                    reveal= Player3.card1
                    Player3.card1=None
                    Player3.card1_reveal=reveal
                else:
                    reveal=Player3.card2
                    Player3.card2=None
                    Player3.card2_reveal=reveal

            elif victim== Player4.name:
                print(f'{victim} choose a card to reveal')
                print(f'1: {Player4.card1} or 2: {Player4.card2}')
                card_reveal=str(input())
                if card_reveal=='1':
                    reveal= Player4.card1
                    Player4.card1=None
                    Player4.card1_reveal=reveal
                else:
                    reveal=Player4.card2
                    Player4.card2=None
                    Player4.card2_reveal=reveal
            else:
                print('You didn`t choose a valid player')
    