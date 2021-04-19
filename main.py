
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

def menu_options():
    print('What do you want to do?')
    print('1. Nothing')
    print('2. Counteract')
    print('3. Challenge')
    return int(input())

#def challenge(challenged,challenger):
def Coup(victim):
    if victim== Player1.name:
        print(f'{victim} choose a card to reveal')
        print(f'1: {Player1.card1} or 2: {Player1.card2}')
        card_reveal=str(input())
        if card_reveal=='1':
            reveal= Player1.card1
            Player1.card1=None
            return reveal
        else:
            reveal=Player1.card2
            Player1.card2=None
            return reveal

    elif victim== Player2.name:
        print(f'{victim} choose a card to reveal')
        print(f'1: {Player2.card1} or 2: {Player2.card2}')
        card_reveal=str(input())
        if card_reveal=='1':
            reveal= Player2.card1
            Player2.card1=None
            return reveal
        else:
            reveal=Player2.card2
            Player2.card2=None
            return reveal

    elif victim== Player3.name:
        print(f'{victim} choose a card to reveal')
        print(f'1: {Player3.card1} or 2: {Player3.card2}')
        card_reveal=str(input())
        if card_reveal=='1':
            reveal= Player3.card1
            Player3.card1=None
            return reveal
        else:
            reveal=Player3.card2
            Player3.card2=None
            return reveal

    elif victim== Player4.name:
        print(f'{victim} choose a card to reveal')
        print(f'1: {Player4.card1} or 2: {Player4.card2}')
        card_reveal=str(input())
        if card_reveal=='1':
            reveal= Player4.card1
            Player4.card1=None
            return reveal
        else:
            reveal=Player4.card2
            Player4.card2=None
            return reveal
    else:
        print('You didn`t choose a valid player')

def kill(victim):
    if victim== Player1.name:
        print(f'{victim} choose a card to reveal')
        print(f'1: {Player1.card1} or 2: {Player1.card2}')
        card_reveal=str(input())
        if card_reveal=='1':
            reveal= Player1.card1
            Player1.card1=None
            return reveal
        else:
            reveal=Player1.card2
            Player1.card2=None
            return reveal

    elif victim== Player2.name:
        print(f'{victim} choose a card to reveal')
        print(f'1: {Player2.card1} or 2: {Player2.card2}')
        card_reveal=str(input())
        if card_reveal=='1':
            reveal= Player2.card1
            Player2.card1=None
            return reveal
        else:
            reveal=Player2.card2
            Player2.card2=None
            return reveal

    elif victim== Player3.name:
        print(f'{victim} choose a card to reveal')
        print(f'1: {Player3.card1} or 2: {Player3.card2}')
        card_reveal=str(input())
        if card_reveal=='1':
            reveal= Player3.card1
            Player3.card1=None
            return reveal
        else:
            reveal=Player3.card2
            Player3.card2=None
            return reveal

    elif victim== Player4.name:
        print(f'{victim} choose a card to reveal')
        print(f'1: {Player4.card1} or 2: {Player4.card2}')
        card_reveal=str(input())
        if card_reveal=='1':
            reveal= Player4.card1
            Player4.card1=None
            return reveal
        else:
            reveal=Player4.card2
            Player4.card2=None
            return reveal
    else:
        print('You didn`t choose a valid player')

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
nara=['None','None']
if num_player==3:
    Player1=create_players(deck,1)
    Player2=create_players(deck,2)
    Player3=create_players(deck,3)
    Player4=create_players(nara,4)
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
cards_reveals=[]

while True:
    for k in range(num_player):
        pass_=0
        plyer=total_players[k]
        print(f'----- Player{k+1} -----')
        if plyer.coins <10:
            menu1 = menu_selection()
            if menu1 == 4:
                menu1 = influences_actions()
            game_=Game(round_,plyer,menu1)
            act,value,plus_min=game_.do_action()
   
            if act=='Coup':
                if plyer.coins<7:
                    print(f'You can´t coup because you have ¢{plyer.coins} coins')
                    pass_=1
                else:
                    victim=str(input('Choose a player to coup (Ex: Player1): '))
                    reveal=Coup(victim)
                    cards_reveals.append(reveal)
            
            elif act == 'Assassinate':
                victim1=str(input('Choose a player to assassinate (Ex: Player1): '))
                reveal = kill(victim1)
            
            elif act == 'Exchange':
                c1 = deck[0]
                c2 = deck[1]
                deck.pop(0)
                deck.pop(0)
                numbers = [1,2,3,4]
                print("Choose 2 cards between the ones you've got from the deck and the ones you had before: ")
                tobechosen = [c1, c2, plyer.card1, plyer.card2]
                print(f'1: {c1}, 2: {c2}, 3: {plyer.card1}, 4: {plyer.card2}')
                chosen = str(input("Example: 1,3: "))
                chosen = chosen.split(',')
                plyer.card1 = tobechosen[int(chosen[0])-1]
                plyer.card2 = tobechosen[int(chosen[1])-1]
                numbers.pop(int(chosen[0])-1)
                numbers.pop(int(chosen[1])-2)
                deck.append(tobechosen[numbers[0]-1])
                deck.append(tobechosen[numbers[1]-1])
                random.shuffle(deck)
            
            elif act == 'Steal':
                mugged = str(input('Choose a player to steal coins from (Ex: Player1): '))
                if mugged == Player1.name:
                    if Player1.coins == 1:
                        Player1.coins -= 1
                        value = 1
                    else:
                        Player1.coins -= 2
                elif mugged == Player2.name:
                    if Player2.coins == 1:
                        Player2.coins -= 1
                        value = 1
                    else:
                        Player2.coins -= 2
                elif mugged == Player3.name:
                    if Player3.coins == 1:
                        Player3.coins -= 1
                        value = 1
                    else:
                        Player3.coins -= 2
                elif mugged == Player4.name:
                    if Player4.coins == 1:
                        Player4.coins -= 1
                        value = 1
                    else:
                        Player4.coins -= 2
                else:
                    print('You didn`t choose a valid player')
                
        else:
            print('You have to Coup')
            victim=str(input('Choose a player to coup (Ex: Player1): '))
            reveal=Coup(victim)
            cards_reveals.append(reveal)
            plus_min='take'
            value=7

        if plus_min == 'add' and pass_==0:
            plyer.coins += value

        elif plus_min == 'take' and pass_==0:
            try:
                plyer.coins -= value

            except Exception as e:
                print(e)
        
        other_players = total_players.copy()
        other_players.pop(k)
        p_action = []
        do = []

        for y in range(len(other_players)):
            print()
            print(f'---{other_players[y].name}---')
            option = menu_options()
            if option == 2:
                p_action.append(other_players[y])
                do.append('Counteract')
            elif option == 3:
                p_action.append(other_players[y])
                do.append('Challenge')
        
        encounter = 0
        ch = 0
        if len(do) >= 1:
            for j in range(len(do)):
                if do[j] == 'Counteract':
                    encounter += 1
                elif do[j] == 'Challenge'
                    ch += 1
            
            if ch == 1:
                pos = do.find('Challenge')
                pp = p_action[pos]
                #LLAMAR A LA FUNCIÓN CHALLENGE
            elif ch > 1:
                ran = random.uniform(1,ch)
                pos = do.find('Challenge',ran)
                pp = p_action[pos]
                #LLAMAR A LA FUNCIÓN CHALLENGE
            
            if encounter == 1:
                pos = do.find('Counteract')
                pp = p_action[pos]
                #LLAMAR A LA FUNCIÓN CHALLENGE
            elif encounter > 1:
                ran = random.uniform(1,ch)
                pos = do.find('Counteract',ran)
                pp = p_action[pos]
                #LLAMAR A LA FUNCIÓN CHALLENGE
            


        #print('nombre: ',Player2.name,' card1: ',Player2.card1,' card2: ',Player2.card2,' coins: ',Player2.coins)
        print(cards_reveals)
        print(plyer.coins)
        break
    
    
    round_+=1
    break