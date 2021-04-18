
class Game:
    #Constantes -> MAYUSCULA
    
    #Constructor
    def __init__(self,round_,player,action):
            self.__round_=round_
            self.__player=player
            self.__action=action
    

    # Getter y Setters
    @property
    def round_(self):
        return self.__round_
        
    @property
    def player(self):
        return self.__player

    @property
    def action(self):
        return self.__action

  

    #Metodos
    def do_action (self):
        if self.action == 1:
            #INCOME
            return None,1,'add'
        elif self.action == 2:
            #Foreign Aid
            return None,2,'add'
        elif self.action == 3:
            #Coup
            return 'Coup',7,'take'