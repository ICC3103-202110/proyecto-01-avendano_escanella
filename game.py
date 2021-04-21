from player import Player
from influences import Influences
from duke import Duke
from assassin import Assassin
from ambassador import Ambassador
from captain import Captain
from contessa import Contessa
import random

class Game ():
    #Métodos
    def action_income(player):
        player.coins+= 1
    
    def action_FA(player):
        player.coins += 2
    
    def action_Coup(victim):
        print(f'{victim.name} you are being Couped')
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
    
    def action_assassinate(victim,player):
        value=Assassin.assassinate()
        player.coins += value
        print(f'{victim.name}, {player.name} has decided to assassinate you.')
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
            Game.action_assassinate(victim)
    
    def action_exchange(player,deck):
        if player.card1 != None and player.card2 != None:
            deck=Ambassador.exchange_2card(player, deck)
            random.shuffle(deck)
            return deck
        else:
            deck=Ambassador.exchange_1card(player, deck)
            random.shuffle(deck)
            return deck
    
    def action_steal(victim,player):
        if victim.coins==1:
            value=Captain.steal_1()
            victim.coins-=value
            player.coins+=value
        elif victim.coins==0:
            print(f'{victim.name} has no coins')
        else:
            value= Captain.steal_2()
            victim.coins-=value
            player.coins+=value
    
    def lose(Player1, Player2, Player3, Player4):
        if Player1.card1 == None and Player1.card2 == None:
            Player1.coins = 0
        elif Player2.card1 == None and Player2.card2 == None:
            Player2.coins = 0
        elif Player3.card1 == None and Player3.card2 == None:
            Player3.coins = 0
        elif Player4.card1 == None and Player4.card2 == None:
            Player4.coins = 0
        