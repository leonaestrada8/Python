# 3.2 Metereologia

class WeatherData:
    def __init__(self, temperatures, humidities, pressures):
        self.temperatures = temperatures
        self.humidities = humidities
        self.pressures = pressures

    def calculate_statistics(self, data):
        return {
            "average": sum(data) / len(data),
            "minimum": min(data),
            "maximum": max(data),
        }

    def report(self):
        temperature_stats = self.calculate_statistics(self.temperatures)
        humidity_stats = self.calculate_statistics(self.humidities)
        pressure_stats = self.calculate_statistics(self.pressures)

        print("Estatisticas de Temperatura:")
        print("Media:", temperature_stats["average"])
        print("Minima:", temperature_stats["minimum"])
        print("Maxima:", temperature_stats["maximum"])

        print("\nEstatisticas de Umidade:")
        print("Media:", humidity_stats["average"])
        print("Minima:", humidity_stats["minimum"])
        print("Maxima:", humidity_stats["maximum"])

        print("\nEstatisticas de Pressao:")
        print("Media:", pressure_stats["average"])
        print("Minima:", pressure_stats["minimum"])
        print("Maxima:", pressure_stats["maximum"])


# Exemplo de uso
temperatures = [20, 22, 18, 19, 23]
humidities = [60, 55, 58, 57, 59]
pressures = [1000, 1005, 999, 1003, 1001]

weather_data = WeatherData(temperatures, humidities, pressures)
weather_data.report()


