class Player:
    #Constantes -> MAYUSCULA

    #Constructor
    def __init__(self,name,card1,card2,card1_reveal,card2_reveal,coins):
        self.__name = name
        self.__card1 = card1
        self.__card2 = card2
        self.__card1_reveal = card1
        self.__card2_reveal = card2
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
    def card1_reveal(self):
        return self.__card1_reveal

    @property
    def card2_reveal(self):
        return self.__card2_reveal

    @property
    def coins(self):
        return self.__coins


    @card1.setter
    def card1 (self, new_card):
        self.__card1=new_card

    @card2.setter
    def card2 (self, new_card):
        self.__card2=new_card

    @card1_reveal.setter
    def card1_reveal (self,reveal):
        self.__card1_reveal=reveal

    @card2_reveal.setter
    def card2_reveal (self,reveal):
        self.__card2_reveal=reveal

    @coins.setter
    def coins (self,value):     
        if self.__coins >= 0:
            self.__coins=value
        else:
            raise Exception(f'Your coins are not enough to do this action. /nTotal of coins is ¢{self.__coins}')



    
        