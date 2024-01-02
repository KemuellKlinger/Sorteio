from tkinter import *
import random

nomes = []
sorteados = []

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

def sorteio():

    addTodosNomes()
    tp = pergarTipo()

    #----------RESET NO CAMPO "SORTEADOS"
    global result
    result.destroy()
    result = Frame(campo, width=250, height=380)
    result.pack()
    #----------

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
                    
                    mostrar = Label(result, textvariable=nomesSorteado)
                    mostrar.place(x=5, y=35 * k)
                
                    tipoSorteio = Label(result, text=tp, padx=20)
                    tipoSorteio.place(x=90, y=(35 * k) + 20)
                   
                elif k % 2 == 1:
                    nomesSorteado.set(sorteados[k])
                    
                    mostrar = Label(result, textvariable=nomesSorteado)
                    mostrar.place(x=190, y=35 * k)

                    barra = Label(result, text="-"*48)
                    barra.place(x=0, y=35*k + 20)

    sorteados.clear()

tipo = IntVar()

texTipo = Label(root, text="Tipo de Torneio: ").place(x=10, y=10)

tipo1 = Radiobutton(root, text="vs" , value=1, variable=tipo)
tipo1.place(x=110, y=10)

tipo2 = Radiobutton(root, text="com", value=2, variable=tipo)
tipo2.place(x=180, y=10)

botao = Button(root, text="SORTEAR", command=lambda:sorteio()).place(x=120, y=40)

campo = LabelFrame(root, text="sorteio", bg="grey")
campo.place(x=10, y=70, width=286, height=400)

result = Frame(campo, width=250, height=380)
result.pack()

root.mainloop()
