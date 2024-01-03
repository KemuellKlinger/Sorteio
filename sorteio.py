from tkinter import *
import random

nomes = []
sorteados = []


fontePadrao = "Small Fonts"
fonteNegrito = fontePadrao, 10, "bold"

root = Tk()
root.geometry("300x500")
root.title("SORTEIO")
root.resizable(False, False)

def addTodosNomes():
    arquivo = open('nomes.txt', 'r')
    for linha in arquivo:
        nomes.append(linha.strip())
    arquivo.close()

def pergarTipo():
    getTp = tipo.get()
    if getTp == 1:
        getTp = "vs"
    elif getTp == 2:
        getTp = "com"
    else:
        getTp = "?"
    return getTp

def sorteio(event=None):  # Adicionamos um parâmetro de evento para o comando do botão e configuração do evento de rolagem do mouse
    addTodosNomes()
    tp = pergarTipo()

    global result
    result.destroy()
    result = Frame(campo, width=250, height=380)
    result.pack()

    canvas = Canvas(result, width=250, height=380 , bg="grey")
    canvas.pack(side="top", fill="both", expand=True)

    scrollbar = Scrollbar(result, command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    # Eventos de rolagem do mouse
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
    canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
    canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))

    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    for i in range(len(nomes)):
        num = random.randint(0, len(nomes) - 1)
        
        if len(nomes)>1 or num<len(nomes):
            sorteados.append(nomes[num])
            nomes.pop(num)
            
        if len(nomes) == 0:
            for k in range(len(sorteados)):
                nomesSorteado = StringVar()
                if k % 2 == 0:
                    nomesSorteado.set(sorteados[k])
                    
                    mostrar1 = Label(frame, textvariable=nomesSorteado, font=(fontePadrao, 15)).pack()
                              
                    tipoSorteio = Label(frame, text=tp, padx=20, font=fonteNegrito).pack()
                    
                elif k % 2 == 1:
                    nomesSorteado.set(sorteados[k])
                    
                    mostrar2 = Label(frame, textvariable=nomesSorteado, font=(fontePadrao, 15)).pack()
                
                    barra = Label(frame, text="-" * 50).pack()
            
    sorteados.clear()

tipo = IntVar()

texTipo = Label(root, text="Tipo de Torneio: ", font=fonteNegrito).place(x=8, y=10)

tipo1 = Radiobutton(root, text="vs" , value=1, variable=tipo, font=fonteNegrito)
tipo1.place(x=120, y=10)

tipo2 = Radiobutton(root, text="com", value=2, variable=tipo, font=fonteNegrito)
tipo2.place(x=180, y=10)

botao = Button(root, text="SORTEAR", command=lambda:sorteio(), font=fonteNegrito).place(x=120, y=40)

campo = LabelFrame(root, text="sorteio", bg="grey", font=fonteNegrito)
campo.place(x=10, y=70, width=286, height=400)

result = Frame(campo, width=250, height=380)
result.pack()

root.mainloop()