from Animal import Animal


class Mamifero(Animal):
    #construtor de mamifero 
    def __init__(self, nome, idade, peso, temPelo):
        #inicializando os atributos herdados de Animal 
        super().__init__(nome, idade, peso)

        self.__temPelo = temPelo
    
    def __amamentar(self):
        return f"{self.nome} esta amamentando"
    
    #polimorfismo 
    def Comer(self, comida):
        return super().Comer(comida)
    


vaca = Mamifero("vaca", 10, 510, True)

print(vaca.__nome)


