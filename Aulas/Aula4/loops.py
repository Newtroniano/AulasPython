impares = [8,7,5,6,1,2,3,5,7,6,4,7,6,2,3,9]

diclist=[{"Email" : "luis.fi@gmail", "senha": "123"}, {"Email":"luisinhogameplay", "senha": "123"}]
dictionarie ={"Email" : "luis.fi@gmail"}


pares = []
email = input("Digite seu email\n")
validemail=""


"""for key, value in dictionarie.items(): 
    if(email == value):
        print("email correto")
    else:
        print("email incorreto")"""
  

"""test = True

tentativas=0
limitetentativas=5

while tentativas<limitetentativas:
    print("Estou em um loop")
    input("Aprte Enter 5x para sair do loop")
    tentativas+=1
    print(tentativas)

print("saiu do loop")"""


for dicionario in diclist:
    print(f"Email: {dicionario['Email']}, Senha: {dicionario['senha']}")
    if(email == dicionario['Email']):
          validemail= dicionario['Email']
    else:
        validemail = ""


  
if(validemail!=""):
      print("email correto")
else:
      print("email incorreto")

