from influences import Influences
from player import Player
import random

class Ambassador(Influences,Player):
    def __init__(self, name):
        super(Ambassador,self).__init__(name)

    def action_exchange(deck,player):
        if player.card1 != None and player.card2 != None:
            c1 = deck[0]
            c2 = deck[1]
            deck.pop(0)
            deck.pop(0)
            numbers = [1,2,3,4]
            print("Choose 2 cards between the ones you've got from the deck and the ones you had before: ")
            tobechosen = [c1, c2, plyer.card1, plyer.card2]
            print(f'1: {c1}, 2: {c2}, 3: {player.card1}, 4: {player.card2}')
            chosen = str(input("Example: 1,3: "))
            chosen = chosen.split(',')
            player.card1 = tobechosen[int(chosen[0])-1]
            player.card2 = tobechosen[int(chosen[1])-1]
            numbers.pop(int(chosen[0])-1)
            numbers.pop(int(chosen[1])-2)
            deck.append(tobechosen[numbers[0]-1])
            deck.append(tobechosen[numbers[1]-1])
            random.shuffle(deck)
            return deck
        else:
            d1 = deck[0]
            d2 = deck[1]
            deck.pop(0)
            deck.pop(0)
            deck.pop(0)
            numbers = [1,2,3]
            print("Choose 1 card between the ones you've got from the deck and the one you had before: ")
            if player.card1 != None:
                tobechosen = [d1, plyer.card1]
                print(f'1: {d1}, 2:{d2}, 3: {player.card1}')
                chosen = str(input("Example (2): "))
                player.card1 = tobechosen[int(chosen[0])-1]
                numbers.pop(int(chosen - 1))
                deck.append(tobechosen[numbers[0]-1])
                deck.append(tobechosen[numbers[1]-1])
                random.shuffle(deck)
                return deck
            else:
                tobechosen = [d1, plyer.card2]
                print(f'1: {d1}, 2:{d2}, 3: {player.card2}')
                chosen = str(input("Example (2): "))
                player.card2 = tobechosen[int(chosen[0])-1]
                numbers.pop(int(chosen - 1))
                deck.append(tobechosen[numbers[0]-1])
                deck.append(tobechosen[numbers[1]-1])
                random.shuffle(deck)
                return deck

    def counteract_stealing(blocker,player):
        print(f'{player.name} your attent for stealing was cancelled by Ambassador')
        opt=str(input(f'Do you want to challenge {blocked.name}? Options: yes / no: '))
        if opt=='yes':
            print('Tamos trabajando en ello')
        else:
            return 'Not_Today'
