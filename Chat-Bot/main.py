import chat as pc
from tkinter import *

nome_maquina= "ola"


main_window = Tk()
main_window.title(nome_maquina)
main_window.geometry("780x780")
main_window.grid()



frame = Frame(main_window)
frame.grid()

l_indentif = Label(frame, text="Insira a sua pergunta  neste campo")
l_indentif.grid(row=0, column=0)
e_messagem = Entry(frame)
e_messagem.grid(row=0, column=1)

frame2= Frame(main_window)
frame2.grid(row=1, column=0)
v = StringVar()
Label(frame2, textvariable=v).grid()

v.set("Qual seu nome?")
entry_segest = False
entry_name_user = True
user_name= ""
history=""

def roda_ChatBot():
    global entry_segest
    global entry_name_user
    global user_name
    global history

    if entry_name_user:
        user_name = e_messagem.get()
        greetings = pc.greetings(nome_maquina)
        history = nome_maquina +": " + greetings + "\n"
        v.set(history)
        entry_name_user = False
    else:
        text= e_messagem.get()
        history += "\n" + user_name + ": " + text
        v.set(history)

    if entry_segest:
        pc.save_sgestion(text)
        entry_segest = False
        history += "\nAgora eu saquei agora eu entendi"
        v.set(history)
    else:
        resposta = pc.search_answer(nome_maquina,"Cliente: " + text + "\n")
        
        if resposta == "Me desculpa não entendi":
            history += "\nFoi mal, não sei o que falar, o que você esperava?\n"
            v.set(history)
            entry_segest = True
        else:
            history += "\n" + pc.display_response(resposta, nome_maquina)
            v.set(history)


Button(frame, text='Clique', command=roda_ChatBot).grid(row=0, column=2)

pc.greetings(nome_maquina)

main_window.mainloop()
# while True:
#     texto = pc.recibe_text()
#     resposta = pc.search_answer(nome_maquina, texto)
#     # if pc.display_response(resposta, nome_maquina) == "fim":
#     #     break


