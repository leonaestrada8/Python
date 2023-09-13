#4.2 Football

class FootballStatistics:
    def __init__(self):
        self.games = []

    def add_game(self, goals, cards, fouls):
        game = {'goals': goals, 'cards': cards, 'fouls': fouls}
        self.games.append(game)

    def calculate_statistics(self):
        total_goals, total_cards, total_fouls = 0, 0, 0
        max_goals = max_cards = max_fouls = float('-inf')
        min_goals = min_cards = min_fouls = float('inf')

        for game in self.games:
            total_goals += game['goals']
            total_cards += game['cards']
            total_fouls += game['fouls']
            max_goals = max(max_goals, game['goals'])
            max_cards = max(max_cards, game['cards'])
            max_fouls = max(max_fouls, game['fouls'])
            min_goals = min(min_goals, game['goals'])
            min_cards = min(min_cards, game['cards'])
            min_fouls = min(min_fouls, game['fouls'])

        avg_goals = total_goals / len(self.games)
        avg_cards = total_cards / len(self.games)
        avg_fouls = total_fouls / len(self.games)

        print("Statistics:")
        print("Average goals:", avg_goals)
        print("Average cards:", avg_cards)
        print("Average fouls:", avg_fouls)
        print("Max goals:", max_goals)
        print("Max cards:", max_cards)
        print("Max fouls:", max_fouls)
        print("Min goals:", min_goals)
        print("Min cards:", min_cards)
        print("Min fouls:", min_fouls)


# Exemplo de uso com 10 jogos
if __name__ == "__main__":
    stats = FootballStatistics()
    stats.add_game(2, 4, 10)
    stats.add_game(3, 5, 8)
    stats.add_game(1, 2, 12)
    stats.add_game(0, 3, 7)
    stats.add_game(4, 2, 9)
    stats.add_game(3, 4, 5)
    stats.add_game(2, 1, 11)
    stats.add_game(5, 3, 6)
    stats.add_game(2, 4, 7)
    stats.add_game(1, 5, 8)
    stats.calculate_statistics()

