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

    @card1.setter
    def card1 (self, new_card):
        self.__card1=new_card


    @property
    def card2(self):
        return self.__card2

    @card2.setter
    def card2 (self, new_card):
        self.__card2=new_card


    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins (self,value):     
        if self.__coins > 0:
            self.__coins=value
        else:
            raise Exception(f'Your coins are not enough to do this action. /nTotal of coins is ¢{self.__coins}')



    
        