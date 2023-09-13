'''
Desenvolva um programa utilizando Java (versão 20.0.2) que gerencie uma biblioteca. 
O programa deve ser capaz de adicionar, listar e remover livros, com ou sem acesso 
a um banco de dados fictício. O livro deve ter título, autor e ISBN.
'''

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        
    def __str__(self):
        return(f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}")
    

class Biblioteca:
    def __init__(self):
        self.livros = []
        
    def adicionar_livro(self, livro):
        print(f"Adicionar livro na Biblioteca:\n                                {livro} ")
        self.livros.append(livro)
        
    def remover_livro(self, isbn):
        print(f"\n Remover livro com ISBN: {isbn} \n")
        self.livros = [livro for livro in self.livros if livro.isbn != isbn]
    
    def listar_livros(self):
        return self.livros[:]
    
    def __str__(self):
        print(f"\n Listando Livros da Biblioteca: \n")
        return "\n".join(str(livro) for livro in self.livros)
    
biblioteca = Biblioteca()


# Adicionar livros
biblioteca.adicionar_livro(Livro("Hitchhiker Guide", "Douglas Adams", "123456789"))
biblioteca.adicionar_livro(Livro("Effective Java", "Joshua Bloch", "987654321"))
#biblioteca.adicionar_livro(Livro("XXXXXXXXXXXX", "YYYYYYYYYYYY", "9999888"))
#biblioteca.adicionar_livro(Livro("ZZZZZZZZZZZZZ", "WWWWWWWWWWWW", "11111888"))

print(biblioteca)

print("---------------------------------")
# Remover um livro pelo ISBN

biblioteca.remover_livro("987654321")

print("---------------------------------")

print(biblioteca)

print("++++++++++++++++++++++++++++++")

lista_livros = biblioteca.listar_livros()
for livro in lista_livros:
    print(str(livro))

'''
# Listar livros
print("Livros na Biblioteca:")
for livro in biblioteca.listar_livros():
    print(str(livro))



# Listar livros novamente
print("\nLivros na Biblioteca apos remocao:")
for livro in biblioteca.listar_livros():
    print(str(livro))
'''
    
    
    