#Livros 1.1

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, isbn):
        self.livros = [livro for livro in self.livros if livro.isbn != isbn]

    def listar_livros(self):
        return self.livros[:]

biblioteca = Biblioteca()

# Adicionar livros
biblioteca.adicionar_livro(Livro("Java Programming", "James Gosling", "123456789"))
biblioteca.adicionar_livro(Livro("Effective Java", "Joshua Bloch", "987654321"))

# Listar livros
print("Livros na Biblioteca:")
for livro in biblioteca.listar_livros():
    print(str(livro))

# Remover um livro pelo ISBN
biblioteca.remover_livro("123456789")

# Listar livros novamente
print("\nLivros na Biblioteca apos remocao:")
for livro in biblioteca.listar_livros():
    print(str(livro))

