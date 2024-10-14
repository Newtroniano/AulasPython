class Casa():
    porta = "marrom"
    rua= "Rua dos bobos"
    CEP= "0000000"
    numero= "0"

casa1 = Casa()
casa2 = Casa()


#Uma classe é um modelo para se criar objetos 
class Pokemon():

    #O metodo construtor cria e inicializa os atributos da classe
    def __init__(self, nome, tipo, nivel, pontos_de_vida):
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel
        self.pontos_de_vida=pontos_de_vida
    
    #Um metodo é a ação da classe 
    def atacar(self):
        print(f"{self.nome} usou um ataque")
    

pikachu = Pokemon("Pikachu", "eletrico", 5, 150)


charmander = Pokemon("Vini", "Fogo", 12, 200)


print(charmander.atacar())







