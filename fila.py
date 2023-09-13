class Fila:
    def __init__(self):
        self.fila = []

    def enfileirar(self, item):
        self.fila.append(item)
        print(f"Item {item} adicionado a fila.")

    def desenfileirar(self):
        if not self.vazia():
            item_removido = self.fila.pop(0)
            print(f"Item {item_removido} removido da fila.")
        else:
            print("Fila está vazia.")

    def vazia(self):
        return len(self.fila) == 0

    def mostrar(self):
        if (self.vazia()):
            print("Fila Vazia.")
        else:
            print("Fila atual:", self.fila)

queue = Fila()
queue.mostrar()
queue.enfileirar(13)
queue.enfileirar(42)
queue.enfileirar(69)
queue.mostrar()
queue.desenfileirar()
queue.mostrar()




