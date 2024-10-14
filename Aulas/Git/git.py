class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.limite:
            self.atual += 1
            return self.atual - 1
        else:
            raise StopIteration

# Uso
contador = Contador(3)
for numero in contador:
    print(numero)