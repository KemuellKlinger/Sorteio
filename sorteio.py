from tkinter import *
import random

fontePadrao = "Small Fonts"
fonteNegrito = fontePadrao, 10, "bold"
class sorteio:
    def __init__(self):       
        self.nomes = []
        self.sorteados = []

        self.criarJanela()
        
    def criarJanela(self):
        self.root = Tk()
        self.root.geometry("300x500")
        self.root.title("SORTEIO")
        self.root.resizable(False, False)

        self.texTipo = Label(self.root, text="Informe a quantidade", font=fonteNegrito).place(x=8, y=10)

        self.entrada = Entry(self.root, font=fonteNegrito)
        self.entrada.place(x=150, y=10, width=70)

        self.botao = Button(self.root, text="SORTEAR", command=lambda:self.sorteio(), font=fonteNegrito).place(x=120, y=40)

        self.campo = LabelFrame(self.root, text="sorteio", bg="grey", font=fonteNegrito)
        self.campo.place(x=10, y=70, width=286, height=400)

        self.result = Frame(self.campo, width=250, height=380)
        self.result.pack()
        self.root.mainloop()
        
    def addTodosNomes(self):
        self.arquivo = open('nomes.txt', 'r')
        for linha in self.arquivo:
            self.nomes.append(linha.strip())
        self.arquivo.close()

    def quantidade(self):
        if self.entrada.get():
            getQuant = IntVar 
            getQuant = self.entrada.get()
            return getQuant
        else:
            return 0

    def sorteio(self, event=None):  # Adicionamos um parâmetro de evento para o comando do botão e configuração do evento de rolagem do mouse
        self.addTodosNomes()
        quant = int(self.quantidade())

        self.result.destroy()
        self.result = Frame(self.campo, width=245, height=380)
        self.result.pack()

        canvas = Canvas(self.result, width=245, height=380)
        canvas.pack()

        scrollbar = Scrollbar(self.result, command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # Eventos de rolagem do mouse
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))
        canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))

        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="center")

        for i in range(len(self.nomes)):
            num = random.randint(0, len(self.nomes) - 1)
            
            if len(self.nomes)>1 or num<len(self.nomes):
                self.sorteados.append(self.nomes[num])
                self.nomes.pop(num)
                
            if len(self.nomes) == 0:
                if quant > len(self.sorteados):
                    self.mostrar = Label(frame, text="informe uma quantidade valida", font=(fontePadrao, 15), wraplength=245)
                    self.mostrar.pack()
                else:
                    for k in range(0, quant):
                        nomesSorteado = StringVar()
                        nomesSorteado.set(self.sorteados[k])
                        self.mostrar = Label(frame, textvariable=nomesSorteado, font=(fontePadrao, 15), wraplength=150)
                        self.mostrar.pack()
                        
                
                               
        self.sorteados.clear()

if __name__ == "__main__":
    app = sorteio()