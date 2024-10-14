class Animal():

    def __init__(self, nome, idade, peso):
        self.__nome  = nome
        self.__idade = idade
        self.__peso  = peso
    
    def Comer(self, comida):
        return f"{self.__nome} esta comendo {comida}"
    
    def Som(self, som):
        return f"Faz o som: {som} "
    
    def Dormir(self):
        return f"{self.__nome} esta dormindo"
    
