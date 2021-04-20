from player import Player
from influences import Influences
from duke import Duke
from assassin import Assassin
from ambassador import Ambassador
from captain import Captain
from contessa import Contessa

class Game ():
    #Métodos

    def action_income(player):
        player.coins+= 1
    
    def action_FA(player):
        player.coins += 2
    
    def action_Coup(victim):
        print(victim.name)
        print(f'1: {victim.card1} or 2: {victim.card2}')
        card_reveal=int(input())
        if card_reveal==1 and victim.card1 != None:
            reveal= victim.card1
            victim.card1=None
            victim.card1_reveal=reveal
        elif card_reveal==2 and victim.card2 != None:
            reveal= victim.card2
            victim.card2=None
            victim.card2_reveal=reveal
        elif victim.card1==None and victim.card2==None:
            print('This player has already lost')
        else:
            print('You can`t choose that card')
            Game.action_Coup(victim)

    def action_tax(player):
        value=(Duke.tax())
        player.coins += value
    