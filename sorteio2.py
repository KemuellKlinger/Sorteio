from tkinter import *
import random

todosNomes = []
sorteados = []

janela = Tk()
janela.geometry("300x550")
janela.title("SORTEIO")


def addTodosNomes():
    arquivo = open('alunos.txt', 'r')
    for linha in arquivo:
        todosNomes.append(linha.strip())
    arquivo.close()


def sorteio():

    addTodosNomes()
    #----------RESET NO CAMPO "SORTEADOS"
    global campo
    campo.destroy
    campo = LabelFrame(janela, text="sorteio", width=250, height=380, bg="grey")
    campo.place(x=10, y=70)
    #----------
    
    tp = StringVar()
    tp.set(tipo.get())
    
    for i in range(len(todosNomes)):
        
        num = random.randint(0, len(todosNomes) - 1)
        
        if len(todosNomes)>1 or num<len(todosNomes):
            sorteados.append(todosNomes[num])
            todosNomes.pop(num)
            
        if len(todosNomes) == 0:
            for k in range(len(sorteados)):
                textoSorteado = StringVar()
                if k % 2 == 0:
                    textoSorteado.set(sorteados[k])
                    
                    mostrar = Label(campo, textvariable=textoSorteado, bg="grey", fg="yellow")
                    mostrar.place(x=10, y=35 * k)
                
                    com = Label(campo, textvariable=tp, bg="grey")
                    com.place(x=70, y=(35 * k) + 20)
                   
                elif k % 2 == 1:
                    textoSorteado.set(sorteados[k])
                    mostrar = Label(campo, textvariable=textoSorteado, bg="grey", fg="yellow")
                    mostrar.place(x=140, y=35 * k)

                    barra = Label(campo, text="-"*47, bg="grey")
                    barra.place(x=0, y=35*k + 20)
    sorteados.clear()

texTipo = Label(janela, text="Tipo de Torneio: ").place(x=10, y=40)

tipo = Entry(janela)
tipo.place(x=70, y=40)

botao_navegador1 = Button(janela, text="SORTEAR", command=lambda:sorteio()).place(x=30, y=10)

campo = LabelFrame(janela, text="sorteio", width=250, height=380, bg="grey")
campo.place(x=10, y=70)

janela.mainloop()
