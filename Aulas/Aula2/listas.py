
#Todas lista sempre começa na Pos 0 

jogos = ["call of dut", "far cry3", "devil may cry", "zelda", "god of war"]
ids    = [4,5,7,1]

jogos.sort()
ids.sort()

print(sorted(jogos, reverse=False))
74

print(jogos)
print(ids)
#----------Atualizando a lista
newjogo = "sonic"
jogos.append("mario")
jogos.append(newjogo)


#--- remover passando a posição do elemento
del jogos[0]
#----------Lista Atualizada------------

#--- remove um pilha 
jogos.pop()

#--- remove passando o valor
ids.remove(1)



print(jogos)