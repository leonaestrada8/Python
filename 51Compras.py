class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def get_preco(self):
        return self.preco

    def get_quantidade(self):
        return self.quantidade

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto, quantidade):
        for _ in range(quantidade):
            self.produtos.append(produto)

    def calcular_total(self):
        return sum(produto.get_preco() for produto in self.produtos)

    def calcular_desconto(self):
        return self.calcular_total() * 0.1 if self.calcular_total() > 100 else 0

    def calcular_total_com_desconto(self):
        return self.calcular_total() - self.calcular_desconto()


produto1 = Produto('Camiseta', 25.99, 10)
produto2 = Produto('Calça', 50.99, 5)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(produto1, 3)
carrinho.adicionar_produto(produto2, 2)

print('Total:', round(carrinho.calcular_total(), 2))
print('Desconto:', carrinho.calcular_desconto())
print('Total com desconto:', carrinho.calcular_total_com_desconto())

