'''
Utilizando Python (versão 3.11.4), projete um programa que gerencie um sistema de vendas de ingressos para um cinema. 
O programa deve ser capaz de exibir filmes em cartaz, selecionar assentos e calcular o preço total. 
Você pode simular o acesso a um banco de dados se desejar.
'''

class Cinema:
    def __init__(self):
        self.filmes = [
            {"nome": "Movie1", "preco": 10},
            {"nome": "Movie2", "preco": 15}
        ]
        self.sala = [
            {"nome": "Sala1", "assentos": self.create_seats()},
            {"nome": "Sala2", "assentos": self.create_seats()}
        ]
    
    def create_seats(self):
        return [["LIVRE" for _ in range(10)] for _ in range(5)]
    
    def exibir_filmes(self):
        print("Filmes em Cartaz:")
        for idx, filme in enumerate(self.filmes):
            print(f"{idx + 1}. {filme['nome']} - {filme['preco']}$")
            
    def exibir_salas(self):
        print("Salas Disponiveis:")
        for idx, sala in enumerate(self.sala):
            print(f"{idx + 1}. {sala['nome']}")
    
    def selecionar_assentos(self, sala_idx, row, col):
        sala = self.sala[sala_idx]
        if sala["assentos"][row][col] == "LIVRE":
            sala["assentos"][row][col] = " N/D "
            return True
        else:
            return False
            
    def calcular_preco(self, filme_idx, qtd):
        return self.filmes[filme_idx]["preco"] * qtd
    
    def exibir_assentos(self, sala_idx):
        print("Assentos:")
        for row in self.sala[sala_idx]["assentos"]:
            print (" | ".join(row))
    
    def info_assento(self):
        row = int(input("Selecione a fileira: \n")) - 1
        col = int(input("Selecione a coluna: \n")) - 1
        return row, col
        
        
    
    
cinema = Cinema()
cinema.exibir_filmes()
filme_selecionado = int(input("Selecione o filme: \n")) - 1
cinema.exibir_salas()
sala_selecionada = int(input("Selecione a sala: \n")) - 1
cinema.exibir_assentos(sala_selecionada)
while True:
    row, col = cinema.info_assento()
    if cinema.selecionar_assentos(sala_selecionada, row, col):
        preco_total = cinema.calcular_preco(filme_selecionado, 1)
        print(f"Ingresso Reservado: preco total: {preco_total}")
        cinema.exibir_assentos(sala_selecionada)
        break
    else:
        print("Assento Reservado! Escolha outro:\n")