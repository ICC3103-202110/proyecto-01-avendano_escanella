class Player:
    #Constantes -> MAYUSCULA

    #Constructor
    def __init__(self,name,card1,card2,coins):
        self.__name = name
        self.__card1 = card1
        self.__card2 = card2
        self.__coins = coins
        
    # Getter y Setters
    @property
    def name(self):
        return self.__name

    @property
    def card1(self):
        return self.__card1
    
    @property
    def card2(self):
        return self.__card2
    
    @property
    def coins(self):
        return self.__coins

    #Metodos