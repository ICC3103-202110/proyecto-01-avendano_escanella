from player import Player
from influences import Influences
import random

class Challenge ():
    def replace_card(player,deck,pos_card):
        a=deck[0]
        if pos_card==1:
            old_card=player.card1
            deck.append(old_card)
            player.card1=a
            deck.pop(0)
        else:
            old_card=player.card2
            deck.append(old_card)
            player.card2=a
            deck.pop(0)
        
        return deck

    def challenge_actions(player,challenged,menu,deck):
        #player es el que desafia
        print (f'{challenged.name} which card you are going to reveal?')
        print(f'1. {challenged.card1} or 2. {challenged.card2}')
        card=int(input())
        if card==1:
            card_=challenged.card1
        else:
            card_= challenged.card2
        
        if menu==5 and card_!='Duke':
            print(f'{challenged.name} does not have the card Duke')
            if card==1:
                reveal= challenged.card1
                challenged.card1=None
                challenged.card1_reveal=reveal
                return 'Not_Today',deck
            else:
                reveal= challenged.card2
                challenged.card2=None
                challenged.card2_reveal=reveal
                return 'Not_Today',deck
        elif menu==6 and card_!='Assassin':
            print(f'{challenged.name} does not have the card Assassin')
            if card==1:
                reveal= challenged.card1
                challenged.card1=None
                challenged.card1_reveal=reveal
                return 'Not_Today',deck
            else:
                reveal= challenged.card2
                challenged.card2=None
                challenged.card2_reveal=reveal
                return 'Not_Today',deck
        elif menu==7 and card_!='Ambassador':
            print(f'{challenged.name} does not have the card Ambassador')
            if card==1:
                reveal= challenged.card1
                challenged.card1=None
                challenged.card1_reveal=reveal
                return 'Not_Today',deck
            else:
                reveal= challenged.card2
                challenged.card2=None
                challenged.card2_reveal=reveal
                return 'Not_Today',deck
        elif menu==8 and card_!='Captain':
            print(f'{challenged.name} does not have the card Captain')
            if card==1:
                reveal= challenged.card1
                challenged.card1=None
                challenged.card1_reveal=reveal
                return 'Not_Today',deck
            else:
                reveal= challenged.card2
                challenged.card2=None
                challenged.card2_reveal=reveal
                return 'Not_Today',deck
        
        else:
            print(f'{challenged.name} has the card {card_}')
            print(f'{player.name} you have lost a card')
            deck=Challenge.replace_card(challenged,deck,card)
            print(f'1: {player.card1} or 2: {player.card2}')
            card_reveal=int(input())
            if card_reveal==1 and player.card1 != None:
                reveal= player.card1
                player.card1=None
                player.card1_reveal=reveal
            elif card_reveal==2 and player.card2 != None:
                reveal= player.card2
                player.card2=None
                player.card2_reveal=reveal
            elif player.card1==None and player.card2==None:
                print('This player has already lost')
            else:
                print('You can`t choose that card')
                Challenge.challenge_actions(player,challenged,menu,deck)
            
            return 'Today', deck
        

    def challenge_counteraction(player,challenged,card_of_counteraction,deck):
        print (f'{challenged.name} which card you are going to reveal?')
        print(f'1. {challenged.card1} or 2. {challenged.card2}')
        card=int(input())
        if card==1:
            card_=challenged.card1
        else:
            card_= challenged.card2

        if card_ != card_of_counteraction:
            print(f'{challenged.name} does not have the card {card_of_counteraction}')
            if card==1:
                reveal= challenged.card1
                challenged.card1=None
                challenged.card1_reveal=reveal
                return 'Today',deck
            else:
                reveal= challenged.card2
                challenged.card2=None
                challenged.card2_reveal=reveal
                return 'Today',deck
        else:
            print(f'{challenged.name} has the card {card_of_counteraction}')
            print(f'{player.name} you have lost a card')
            deck=Challenge.replace_card(challenged,deck,card)
            print(f'1: {player.card1} or 2: {player.card2}')
            card_reveal=int(input())
            if card_reveal==1 and player.card1 != None:
                reveal= player.card1
                player.card1=None
                player.card1_reveal=reveal
            elif card_reveal==2 and player.card2 != None:
                reveal= player.card2
                player.card2=None
                player.card2_reveal=reveal
            elif player.card1==None and player.card2==None:
                print('This player has already lost')
            else:
                print('You can`t choose that card')
                Challenge.challenge_actions(player,challenged,menu,deck)
            
            return 'Not_Today', deck
