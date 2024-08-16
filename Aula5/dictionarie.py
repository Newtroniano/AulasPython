nome="string"
lista=[1,"Luis", True, 1.5] #--- Lista é mutavel e dinamica 

tupla=(1,"Luis", True, 1.5)#--- Estatica não é dinamica

pessoa = {"altura" : 1.80, "cor de olhos": "azuis", "qi" : 120}

usuarios=[{"ID" : 1, 
           "Email":"fulno@gmail.com", 
           "Nome": "Fulano", 
           "Active": True},
          { 
           "ID" : 2, 
           "Email":"ciclano@gmail.com", 
           "Nome": "Ciclano", 
           "Active": True
         }]




#print(pessoa["cor de olhos"])

email = input("Digite o email\n")
verify=""

print(usuarios)


#---- for para interar em UM dicitionarie ou objeto
"""for key, value in usuarios.items():
    print("Atributo:", " ", key, " ", "Valor:", " ", value)

    if(email == usuarios["Email"]):
        verify = usuarios["Email"]
    else:
        verify=""
"""
#--- for para interar em uma LISTA de dicitionarie ou objeto 
for usuario in usuarios:

    print(usuario["Email"])

    if(email == usuario["Email"]):
        verify = usuario["Email"]
    else:
        verify=""


 
if(verify != ""):
    print("Email encontrado")
else:
    print("Email não existe")





