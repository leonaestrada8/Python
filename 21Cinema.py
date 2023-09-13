# Cinema 2.1
class Cinema:

    def __init__(self):
        self.filmes = [
            {"nome": "Movie 1", "preco": 10},
            {"nome": "Movie 2", "preco": 12},
            {"nome": "Movie 3", "preco": 15}
        ]
        self.salas = [{"nome": "Sala 1", "assentos": self.create_seats()},
                      {"nome": "Sala 2", "assentos": self.create_seats()}]

    def create_seats(self):
        return [["Livre" for _ in range(10)] for _ in range(5)]

    def exibir_filmes(self):
        print("Filmes em Cartaz:")
        for idx, filme in enumerate(self.filmes):
            print(f"{idx + 1}. {filme['nome']} - ${filme['preco']}")

    def selecionar_assentos(self, sala_idx, row, col):
        sala = self.salas[sala_idx]
        if sala["assentos"][row][col] == "Livre":
            sala["assentos"][row][col] = "Ocupado"
            return True
        else:
            return False

    def calcular_preco(self, filme_idx, quantidade):
        return self.filmes[filme_idx]["preco"] * quantidade

    def exibir_salas(self):
        print("Salas Disponíveis:")
        for idx, sala in enumerate(self.salas):
            print(f"{idx + 1}. {sala['nome']}")

    def exibir_assentos(self, sala_idx):
        print("Assentos:")
        for row in self.salas[sala_idx]["assentos"]:
            print(" | ".join(row))


# Simulação
cinema = Cinema()
cinema.exibir_filmes()
filme_selecionado = int(input("Selecione o filme: ")) - 1
cinema.exibir_salas()
sala_selecionada = int(input("Selecione a sala: ")) - 1
cinema.exibir_assentos(sala_selecionada)
row = int(input("Selecione a fileira: "))
col = int(input("Selecione a coluna: "))
if cinema.selecionar_assentos(sala_selecionada, row, col):
    preco_total = cinema.calcular_preco(filme_selecionado, 1)
    print(f"Ingresso reservado. Preço Total: ${preco_total}")
else:
    print("Assento já ocupado!")
