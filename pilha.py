class Pilha:
    def __init__(self):
        self.pilha = []
        
    def empilhar(self,elemento):
        self.pilha.append(elemento)
        print(f"Adicionado elemento: {elemento}")
        
    def desempilhar(self):
        if (self.isEmpty()):
            print ("Pilha Vazia")
        else:
            removido = self.pilha.pop(-1)
            print (f" Removido elemento: {removido}")
        
    def isEmpty(self):
        return len(self.pilha) == 0
    
    def mostrar(self):
        if (self.isEmpty()):
            print("Pilha Vazia.")
        else:
            print(self.pilha)
    

stack = Pilha()
stack.mostrar()
stack.empilhar(66)
stack.empilhar(69)
stack.empilhar(42)
stack.empilhar(81)
stack.mostrar()
stack.desempilhar()
stack.mostrar()



