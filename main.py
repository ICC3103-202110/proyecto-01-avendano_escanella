
import random
from player import Player
from game import Game
from influences import Influences
from duke import Duke
from assassin import Assassin
from ambassador import Ambassador
from captain import Captain
from contessa import Contessa
from challenge import Challenge

def create_players (deck,i):
    card1=deck[0]
    deck.pop(0)
    card2=deck[0]
    deck.pop(0)
    ply=f'Player{i}'
    player_=Player(ply,card1,card2,None,None,7)
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
   
def menu_counteract():
    print('What do you want to do?')
    print('1. DUKE: Blocks foreign aid')
    print('2. AMBASSADOR: Blocks stealing')
    print('3. CAPTAIN: Blocks stealing')
    print('4. CONTESSA: Blocks assassination')
    return int(input())


def game():
    deck=['Duke','Duke','Duke','Assassin','Assassin','Assassin','Ambassador','Ambassador','Ambassador',
        'Captain','Captain','Captain','Contessa','Contessa','Contessa']
    random.shuffle(deck)
    
    influences=[ Duke('Duke'), Assassin('Assasin'), Ambassador('Ambassador'), Captain('Captain'), Contessa('Contessa')]
    
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


    while True:
        for k in range(num_player):
            plyer=total_players[k]
            print(f'----- Player{k+1} -----')
            if plyer.card1 == None and plyer.card2 == None:
                print('You have lost')
    

            else:
                valid='Today'
                print(f'Your cards are: {plyer.card1}   {plyer.card2}')
                # ACTION
                if plyer.coins <10:
                    menu1 = menu_selection()
                    if menu1 == 4:
                        menu1 = influences_actions()
                     
                    if menu1!=1 and menu1!=3:
                        other_players = total_players.copy()
                        other_players.pop(k)
                        p_action = []
                        do = []
                        if menu1==6:
                            victim_to_kill=str(input('Choose a player to assassinate (Ex: Player1): '))
                        # COUNTERACT / CHALLENGE / NOTHING
                        for y in range(len(other_players)):
                            if other_players[y].card1==None and other_players[y].card2==None:
                                #ACA METER LA FUNCION DE PERDIÓ
                                continue
                    
                            else:
                                print(f'---{other_players[y].name}---')
                                print(f'Your cards are: {other_players[y].card1}   {other_players[y].card2}')
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
                                elif do[j] == 'Challenge':
                                    ch += 1
                            
                            if ch == 1:
                                pos = do.index('Challenge')
                                pp = p_action[pos]
                                print (f'---{pp.name}---')
                                print('Challenge')
                                valid,deck=Challenge.challenge_actions(pp,plyer, menu1, deck)
                            elif ch > 1:
                                ran = int(random.uniform(1,ch))
                                print(ran)
                                for j in range(ran):
                                    do.pop(0)
                                    p_action.pop(0)
                                pp = p_action[0]
                                print (f'---{pp.name}---')
                                print('Challenge')
                                valid,deck=Challenge.challenge_actions(pp,plyer, menu1, deck)
                            
                            if encounter == 1:
                                pos = do.index('Counteract')
                                pp = p_action[pos]
                                print()
                                print (f'---{pp.name}---')
                                print('Counteract')
                                count_=menu_counteract()
                                if count_ == 1:
                                    valid,deck=Duke.counteract_FA(pp,plyer,deck)
                                elif count_ == 2:
                                    valid,deck=Ambassador.counteract_stealing(pp, plyer,deck)
                                elif count_ == 3:
                                    valid,deck=Captain.counteract_stealing(pp, plyer,deck)
                                elif count_ == 4:
                                    valid,deck=Contessa.counteract_assassin(pp, plyer,deck)

                            elif encounter > 1:
                                ran = int(random.uniform(1,encounter))
                                print(ran)
                                for j in range(ran):
                                    do.pop(0)
                                    p_action.pop(0)
                                pp = p_action[0]
                                print (f'---{pp.name}---')
                                print('Counteract')
                                count_=menu_counteract()
                                if count_ == 1:
                                    valid,deck=Duke.counteract_FA(pp,plyer,deck)
                                elif count_ == 2:
                                    valid,deck=Ambassador.counteract_stealing(pp, plyer,deck)
                                elif count_ == 3:
                                    valid,deck=Captain.counteract_stealing(pp, plyer,deck)
                                elif count_ == 4:
                                    valid,deck=Contessa.counteract_assassin(pp, plyer,deck)
                                
                        else:
                            valid='Today'
                        #DO ACTION 1
                        if menu1 == 2 and valid != 'Not_Today':
                            Game.action_FA(plyer)
                        elif menu1 == 5 and valid != 'Not_Today':
                            Game.action_tax(plyer)
                        elif menu1 == 6 and valid != 'Not_Today':
                            if plyer.coins >=3:
                                if victim_to_kill == Player1.name:
                                    Game.action_assassinate(Player1,plyer)
                                elif victim_to_kill == Player2.name:
                                    Game.action_assassinate(Player2,plyer)
                                elif victim_to_kill == Player3.name:
                                    Game.action_assassinate(Player3,plyer)
                                elif victim_to_kill == Player4.name:
                                    Game.action_assassinate(Player4,plyer)
                            else:
                                print(f'You can´t assassinate because you have ¢{plyer.coins} coins')
                        elif menu1 == 7 and valid != 'Not_Today':
                            deck=Game.action_exchange(plyer,deck)
                        elif menu1 == 8 and valid != 'Not_Today':
                            mugged = str(input('Choose a player to steal coins from (Ex: Player1): '))
                            if mugged == Player1.name:
                                Game.action_steal(Player1,plyer)
                            elif mugged == Player2.name:
                                Game.action_steal(Player2,plyer)
                            elif mugged == Player3.name:
                                Game.action_steal(Player3,plyer)
                            elif mugged == Player4.name:
                                Game.action_steal(Player4,plyer)
                        


                     #DO ACTION 2
                    else:
                
                        if menu1==1:
                            Game.action_income(plyer)
                        elif menu1==3:
                            if plyer.coins>=7:
                                plyer.coins-=7
                                victim=str(input('Choose a player to coup (Ex: Player1): '))
                                if victim == Player1.name:
                                    Game.action_Coup(Player1)
                                elif victim == Player2.name:
                                    Game.action_Coup(Player2)
                                elif victim == Player3.name:
                                    Game.action_Coup(Player3)
                                elif victim == Player4.name:
                                    Game.action_Coup(Player4)
                            else:
                                print(f'You can´t coup because you have ¢{plyer.coins} coins')
                else:
                    print('You have to coup')
                    plyer.coins-=7
                    victim=str(input('Choose a player to coup (Ex: Player1): '))
                    if victim == Player1.name:
                        Game.action_Coup(Player1)
                    elif victim == Player2.name:
                        Game.action_Coup(Player2)
                    elif victim == Player3.name:
                        Game.action_Coup(Player3)
                    elif victim == Player4.name:
                        Game.action_Coup(Player4)
                
                print('nombre: ',Player1.name,' card1: ',Player1.card1,' card2: ',Player1.card2,' coins: ',Player1.coins)
                print('nombre: ',Player2.name,' card1: ',Player2.card1,' card2: ',Player2.card2,' coins: ',Player2.coins)
                print('nombre: ',Player3.name,' card1: ',Player3.card1,' card2: ',Player3.card2,' coins: ',Player3.coins)
                print('nombre: ',Player4.name,' card1: ',Player4.card1,' card2: ',Player4.card2,' coins: ',Player4.coins)
                
                random.shuffle(deck)
                break
            
        
        round_+=1
        break

if __name__ == "__main__":
    game()