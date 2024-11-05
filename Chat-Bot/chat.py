palavrasProibidas = ["feio"]

def Saudacoes(nome):
    import random
    frases = ["Ola Meu nome é " + nome + ". Como vai você", "Eae","Oi tudo bem?"]
    print(frases[random.randint(0,2)])


def palvra(texto):
   
    for p in palavrasProibidas:
        if p in texto:
            return True
        
        return  False

def recebeTexto():
        
        texto = "Cliente" + input("Cliente: ")

        palavrasProibidas = palvra(texto)

        if palavrasProibidas == False:  
            return texto
        else:
            return recebeTexto()

        
    

def buscaResposta(nome, texto):
    with open("base.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            #print(viu)
            if viu !="":
                if texto.replace("Cliente: ","") == "TEM NADA AQUI ADEUS":
                    print(nome+ ": volte sempre!")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if "chatbo:" in proximalinha:
                        return proximalinha
            else:
                print("Me desculpe, não tenho esse conhecimento ainda mestre")
                conhecimento.write("\n" + texto)   
                respota_user = input("O que esperava?\n")
                isproibo = palvra(respota_user)

                if isproibo == False:
                    conhecimento.write("\n" + "chatbo: " + respota_user)
                    return "Hummmmmmmmmmmmm"    
                return "Não pode"    
              

def exibeResposta(resposta, nome):
    print(resposta.replace("Chatbot", nome))
    if resposta == "fim":
        return "fim"
    return "continua"