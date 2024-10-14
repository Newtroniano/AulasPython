string="Fabian David González Acurero"

#print(string)

frase="Ola meu nome é fulano"
print(len(frase))

if(len(frase)>=31):
    print("NÃO AUTORIZADO")
else:
    print("PERMITIDO")


print(frase[0])
print(frase[-1])
print(frase[10:15])
print(frase[:7])
print(frase[::2])


email= "fulano@ctrlplay.com.br"
print(email.find("@"))
print(email.count("."))

nome="Luis"
sobrenome="Fidelis"
saldo= 100000

print(nome + " " + sobrenome +  " " + str(saldo))

print(string.upper())
print(string.lower())

user = input("Ola digite o seu nome")
print("Bem vindo" + " " + user)






