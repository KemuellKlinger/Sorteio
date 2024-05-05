from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

class Sorteio:
    def __init__(self):   
        self.fontePadrao = "Small Fonts"
        self.fonteNegrito = self.fontePadrao, 10, "bold"    
        self.nomes = []
        self.sorteados = []

        self.criarJanela()
        
    def criarJanela(self):
        self.root = Tk()
        self.root.geometry("310x500")
        self.root.title("SORTEIO")
        self.root.resizable(False, False)

        self.botaoAdicionar = Button(self.root, text="Adicionar Nomes", command=lambda:self.telaAdicionarNomes(),font=self.fonteNegrito)
        self.botaoAdicionar.pack(pady=5)
        
        self.botaoMostrarTodos = Button(self.root, text="Exibir nomes", command=lambda:self.mostrarTodos(), font=self.fonteNegrito)
        self.botaoMostrarTodos.pack()

        self.quantidade = Label(self.root, text="Quantidade: ", font=self.fonteNegrito)
        self.quantidade.place(x=8, y=65)

        self.entrada = Entry(self.root, font=self.fonteNegrito)
        self.entrada.place(x=100, y=65, width=70)

        self.botaoSortear = Button(self.root, text="SORTEAR", command=lambda:self.sorteio(), font=self.fonteNegrito)
        self.botaoSortear.place(x=180, y=60, height=28, width=70)

        self.campo = LabelFrame(self.root, text="Sorteio", bg="grey", font=self.fonteNegrito)
        self.campo.place(x=10, y=100, width=286, height=350)

        self.treeview = ttk.Treeview(self.campo, columns=("Nome",), show="headings")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.pack(fill="both", expand=True)
        
        self.carregarNomes()

        self.root.mainloop()

    def telaAdicionarNomes(self):
        self.rootAdd = Toplevel(self.root)
        self.rootAdd.geometry("310x400")
        self.rootAdd.title("ADICIONAR NOMES")
        self.rootAdd.resizable(False, False)

        Label(self.rootAdd, text="Digite o nome ", font=self.fonteNegrito).place(x=8, y=50)

        self.entradaAdd = Entry(self.rootAdd, font=self.fonteNegrito)
        self.entradaAdd.place(x=110, y=50, width=90)

        Button(self.rootAdd, text="Adicionar", command=lambda:self.addNomes(),
                            font=self.fonteNegrito).place(x=210, y=50, height=28, 
                                                          width=70)

        self.campoExibir = LabelFrame(self.rootAdd, text="Nomes", bg="grey", font=self.fonteNegrito)
        self.campoExibir.place(x=10, y=100, width=286, height=290)

        self.treeviewAdd = ttk.Treeview(self.campoExibir, columns=("Nome",), show="headings")
        self.treeviewAdd.heading("Nome", text="Nome")
        self.treeviewAdd.pack(fill="both", expand=True)
        
        # Adicionando evento de clique duplo na tabela
        self.treeviewAdd.bind("<Double-1>", self.removerNome)

        janelaAdd = True
        self.carregarNomes(janelaAdd)

        self.rootAdd.mainloop()

    def addNomes(self):
        nome = self.entradaAdd.get()
        if nome:
            with open('nomes.txt', 'a') as arquivoAdd: 
                arquivoAdd.write(nome + '\n')
            self.nomes.append(nome)
            self.treeviewAdd.insert("", "end", values=(nome,))
            self.entradaAdd.delete(0, END)  # Limpar o campo de entrada após adicionar o nome
        else:
            messagebox.showwarning("Aviso", "Insira um nome para adicionar.")
            self.rootAdd.lift()
            
    def mostrarTodos(self):
        try:
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            with open('nomes.txt', 'r') as arquivo:
                for linha in arquivo:
                    nome = linha.strip()
                    self.treeview.insert("", "end", values=(nome,)) 
        except FileNotFoundError:
            messagebox.showwarning("Aviso", "O arquivo 'nomes.txt' não foi encontrado.")
        
    def carregarNomes(self, janelaAdd=NONE):
        try:
            with open('nomes.txt', 'r') as arquivo:
                for linha in arquivo:
                    nome = linha.strip()
                    if janelaAdd == True:
                        self.treeviewAdd.insert("", "end", values=(nome,))
                    else:
                        self.nomes.append(nome)
                        self.treeview.insert("", "end", values=(nome,))
        except FileNotFoundError:
            messagebox.showwarning("Aviso", "O arquivo 'nomes.txt' não foi encontrado.")

    def sorteio(self):
        quant = self.entrada.get()
        try:
            quant = int(quant)
        except ValueError:
            messagebox.showwarning("Aviso", "Insira um número válido para a quantidade.")
            return

        if quant <= 0:
            messagebox.showwarning("Aviso", "Insira uma quantidade válida.")
            return

        if len(self.nomes) < quant:
            messagebox.showwarning("Aviso", f"A quantidade de nomes disponíveis ({len(self.nomes)}) é menor do que a quantidade solicitada ({quant}).")
            return

        random.shuffle(self.nomes)
        self.sorteados = random.sample(self.nomes, quant)

        # Limpar a exibição anterior
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Exibir os sorteados na tabela
        for nome in self.sorteados:
            self.treeview.insert("", "end", values=(nome,))

    def removerNome(self, event):
        item_selecionado = self.treeviewAdd.selection()
        
        if item_selecionado:
        
            nome_selecionado = self.treeviewAdd.item(item_selecionado, "values")[0]
        
            confirmar = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir '{nome_selecionado}'?")
            if confirmar:
                self.nomes.remove(nome_selecionado)
                self.treeviewAdd.delete(item_selecionado)
                self.atualizarArquivo()
                
    def atualizarArquivo(self):
        with open('nomes.txt', 'w') as arquivo:
            for nome in self.nomes:
                arquivo.write(nome + "\n")

if __name__ == "__main__":
    app = Sorteio()
