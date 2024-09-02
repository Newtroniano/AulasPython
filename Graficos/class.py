class Reino():
    def __init__(self, nome):
        self.nome = nome
        

    def informarDescrição():
        raise NotImplementedError("metodo base para criar uma classe não é possivel criar um objeto")

class Animais(Reino):
   
        def __init__(self,grupo, epecie, nome):
            
            self.grupo = grupo
            self.especie = epecie
            super().__init__(nome)
           
        def comer(self, comida):
          return f"O {self.nome} está comendo {comida}" 
        
        def informarDescrição(self):
          return f"O {self.nome} é da especie {self.especie}"   


class Felino(Animais):
    def __init__(self, grupo, epecie, nome):
        super().__init__(grupo, epecie, nome)

    def comer(self, comida):
        return super().comer(comida)
    
    def informarDescrição(self):
        return super().informarDescrição()
    def Caça(self):
        return f"O {self.nome} esta caçando"
    
  
leao = Felino("felino", "leao", "leo")

print(leao.informarDescrição())
print(leao.comer("carne"))