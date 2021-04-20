
import random
from player import Player
from game import Game
from influences import Influences
from duke import Duke
from assassin import Assassin
from ambassador import Ambassador
from captain import Captain
from contessa import Contessa

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

def replace_card(player,pos_card,deck):
    a=deck[0]
    if pos_card==1:
        old_card=player.card1
        deck.append(old_card)
        player.card1=a
        deck.pop(0)
    else:
        old_card=player.card2
        deck.append(old_card)
        player.card1=a
        deck.pop(0)
    
    return deck

def challenge(challenged,challenger,action,deck):
    print (f'{challenged.name} which card you are going to reveal?')
    print(f'1. {challenged.card1} or 2. {challenged.card2}')
    card=int(input())

    if card==1:
        card_=challenged.card1
    else:
        card_= challenged.card2

    # DOUBT ACTION
    if act=='Tax' and card_!='Duke':
        if card==1:
            card_to_deck=challenged.card1
            challenged.card1=None
        if card==2:
            card_to_deck=challenged.card2
            challenged.card2=None
        return 'Not_Today', card_to_deck,deck
    
    elif act=='Assassinate' and card_!='Assassin':
        if card==1:
            card_to_deck=challenged.card1
            challenged.card1=None
        if card==2:
            card_to_deck=challenged.card2
            challenged.card2=None
        return 'Not_Today', card_to_deck,deck
    
    elif act=='Exchange' and card_!='Ambassador':
        if card==1:
            card_to_deck=challenged.card1
            challenged.card1=None
        if card==2:
            card_to_deck=challenged.card2
            challenged.card2=None
        return 'Not_Today', card_to_deck ,deck

    elif act=='Steal' and card!='Captain':
        if card==1:
            card_to_deck=challenged.card1
            challenged.card1=None
        if card==2:
            card_to_deck=challenged.card2
            challenged.card2=None
        return 'Not_Today', card_to_deck ,deck
    
    # DOUBT COUNTERACT
    elif act=='doubt Contessa' and card_!='Contessa':
        if card==1:
            card_to_deck=challenged.card1
            challenged.card1=None
        if card==2:
            card_to_deck=challenged.card2
            challenged.card2=None
        return 'Not_Today', card_to_deck ,deck

    elif act=='doubt Duke' and card_!='Duke':
        if card==1:
            card_to_deck=challenged.card1
            challenged.card1=None
        if card==2:
            card_to_deck=challenged.card2
            challenged.card2=None
        return 'Not_Today', card_to_deck ,deck

    elif act=='doubt Ambassador or Captain' and (card_!='Ambassador' or card_!='Captain'):
        if card==1:
            card_to_deck=challenged.card1
            challenged.card1=None
        if card==2:
            card_to_deck=challenged.card1
            challenged.card2=None
        return 'Not_Today', card_to_deck ,deck
    
    else:
        print(f'{challenger.name} you have lost the challenge')
        print('Which card are you going to reveal?')
        print(f'1. {challenger.card1} or 2. {challenger.card2}')
        reveal_=int(input())
        if reveal_==1:
            reveal_card=challenger.card1
        else:
            reveal_card=challenger.card2

        deck=replace_card(challenged,card_,deck)

        return 'Today', reveal_card, deck
    
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
        
                            elif ch > 1:
                                ran = random.uniform(1,ch)
                                pos = do.index('Challenge',ran)
                                pp = p_action[pos]
                                print (f'---{pp.name}---')
                                print('Challenge')
                                works,card_to_deck,deck=challenge(plyer, ppact,deck)
                                #cards_reveals.append(card_to_deck)
                                if act=='Tax' and works=='Not_Today':
                                    plyer.coins-=3
                                elif act=='Assassinate' and works=='Not_Today':
                                    cancel_assassination(victim1,reveal,pos_)
                                    reveal=None
                                elif act=='Exchange' and works!='Not_Today':
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
                            
                            if encounter == 1:
                                pos = do.index('Counteract')
                                pp = p_action[pos]
                                print (f'---{pp.name}---')
                                print('Counteract')
                                count_=menu_counteract()
                                if count_ == 1:
                                    valid=Duke.counteract_FA(pp,plyer)
                                elif count_ == 2:
                                    valid=Ambassador.counteract_stealing(pp, plyer)
                                elif count_ == 3:
                                    valid=Captain.counteract_stealing(pp, plyer)
                                elif count_ == 4:
                                    valid=Contessa.counteract_assassin(pp, plyer)

                            elif encounter > 1:
                                ran = random.uniform(1,ch)
                                pos = do.index('Counteract',ran)
                                pp = p_action[pos]
                                print (f'---{pp.name}---')
                                print('Counteract')
                                count_=menu_counteract()
                                if count_ == 1:
                                    valid=Duke.counteract_FA(pp,plyer)
                                elif count_ == 2:
                                    valid=Ambassador.counteract_stealing(pp, plyer)
                                elif count_ == 3:
                                    valid=Captain.counteract_stealing(pp, plyer)
                                elif count_ == 4:
                                    valid=Contessa.counteract_assassin(pp, plyer)
                                
                        else:
                            value='Today'
                        #DO ACTION!
                        if menu1 == 2 and value != 'Not_Today':
                            Game.action_FA(plyer)
                        elif menu1 == 5 and value != 'Not_Today':
                            Game.action_tax(plyer)
                        elif menu1 == 6 and value != 'Not_Today':
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
                        elif menu1 == 7 and value != 'Not_Today':
                            deck=Game.action_exchange(plyer,deck)
                        elif menu1 == 8 and value != 'Not_Today':
                            mugged = str(input('Choose a player to steal coins from (Ex: Player1): '))
                            if mugged == Player1.name:
                                Game.action_steal(Player1,plyer)
                            elif mugged == Player2.name:
                                Game.action_steal(Player2,plyer)
                            elif mugged == Player3.name:
                                Game.action_steal(Player3,plyer)
                            elif mugged == Player4.name:
                                Game.action_steal(Player4,plyer)

                        else:
                            print('Your action isn`t valid')



                    else:
                        #DO ACTION 2
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
                
                print(plyer.coins)
                random.shuffle(deck)
                break
            
        
        round_+=1
        break

if __name__ == "__main__":
    game()