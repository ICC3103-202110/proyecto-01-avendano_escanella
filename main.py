
import random
from player import Player
from game import Game

def create_players (deck,i):
    card1=deck[0]
    deck.pop(0)
    card2=deck[0]
    deck.pop(0)
    ply=f'Player{i}'
    player_=Player(ply,card1,card2,2)
    return player_

def menu_selection():
    print("\nSelect one of the following actions: ")
    print("1. Income")
    print("2. Foreign Aid")
    print("3. Coup")
    print("4. Influences actions")
    return int(input())

def influences_actions():
    print("\nSelect one of the following actions: ")
    print("5. Tax: +3 coins (Duke)")
    print("6. Assassinate: -3 coins (Assassin)")
    print("7. Exchange: Exchange cards with Court Deck (Ambassador)")
    print("8. Steal: Take 2 coins from other player (Captain)")
    return int(input())

deck=['Duke','Duke','Duke','Assassin','Assassin','Assassin','Ambassador','Ambassador','Ambassador',
    'Captain','Captain','Captain','Contessa','Contessa','Contessa']
random.shuffle(deck)

a=True
while a==True:
    num_player = int(input( "How many players?: " ))
    if num_player==3 or num_player ==4:
        a=False
    else:
        print("You can play with 3 or 4 players")
        print()

total_players=[]
if num_player==3:
    Player1=create_players(deck,1)
    Player2=create_players(deck,2)
    Player3=create_players(deck,3)
    total_players.append(Player1)
    total_players.append(Player2)
    total_players.append(Player3)

else:
    Player1=create_players(deck,1)
    Player2=create_players(deck,2)
    Player3=create_players(deck,3)
    Player4=create_players(deck,4)
    total_players.append(Player1)
    total_players.append(Player2)
    total_players.append(Player3)
    total_players.append(Player4)

round_=1
while True:
    for k in range(num_player):
        print(f'----- Player{k+1} -----')
        menu1 = menu_selection()
        if menu1 == 4:
            menu1 = influences_actions()
        plyer=total_players[k]
        game_=Game(round_,plyer,menu1)
        act,value,plus_min=game_.do_action()
        if plus_min == 'add':
            plyer.coins += value

        elif plus_min == 'take':
            try:
                plyer.coins -= value

            except Exception as e:
                print(e)
            

        print(plyer.coins)
        break
    break
    round_+=1