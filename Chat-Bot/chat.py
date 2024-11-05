swearWords = ["feio"]

def greetings(name):
    import random
    frases = ["Ola Meu name é " + name + ". Como vai você", "Eae","Oi tudo bem?"]
    return frases[random.randint(0,2)]


def save_sgestion(sugest):
    with open("base.txt", "a+") as know:
        know.write("Chatbot:" + sugest + "\n")

def prohibited_words(text):
   
    for p in swearWords:
        if p in text:
            return True
        
        return  False

def recibe_text():
        
        text = "Cliente" + input("Cliente: ")

        swearWords = prohibited_words(text)

        if swearWords == False:  
            return text
        else:
            return recibe_text()

        
    

def search_answer(name, text):
    with open("base.txt", "a+") as know:
        know.seek(0)
        while True:
            see = know.readline()
            #print(see)
            if see !="":
                if jaccard(text, see)>0.3:
                    nextline= know.readline()
                    if "Chatbot:" in nextline:
                        return nextline
            else:
                know.write(text)
                return "Me desculpa não entendi"
            #     if text.replace("Cliente: ","") == "TEM NADA AQUI ADEUS":
            #         print(name+ ": volte sempre!")
            #         return "fim"
            #     elif see.strip() == text.strip():
            #         nextLine = know.readline()
            #         if "chatbo:" in nextLine:
            #             return nextLine
            # else:
            #     print("Me desculpe, não tenho esse conhecimento ainda mestre")
            #     know.write("\n" + text)   
            #     userAwnser = input("O que esperava?\n")
            #     isSwerword = prohibited_words(userAwnser)

            #     if isSwerword == False:
            #         know.write("\n" + "chatbo: " + userAwnser)
            #         return "Hummmmmmmmmmmmm"    
            #     return "Não pode"    


def jaccard(usertext , basetext):
    usertext = clean(usertext)
    basetext = clean(basetext)

    if len(basetext)<1 : return 0
    else:
        commum = 0
        for p in usertext.split():
            if p in basetext.split():
                commum += 1
        return commum/(len(basetext.split()))



def clean(frase):
    tirar=["?", "!", "...", ".", ",", "Cliente:","\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase

def display_response(resposta, name):
    return resposta.replace("Chatbot", name)

