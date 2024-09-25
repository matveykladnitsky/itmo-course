import pandas as pd
import matplotlib.pyplot as plt


class ChartPlotter:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path, encoding='utf-8', sep=';')
        # Прочитаем данные столбца №1
        self.x = self.data.iloc[:, 0]
        self.y1 = self.data.iloc[:, 3]  # Столбец 4
        self.y2 = self.data.iloc[:, 17]  # Столбец 18

    def plot_graphs(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.x, self.y1, label='Положение дроссельной заслонки (%)')
        plt.plot(self.x, self.y2, label='Часовой расход топлива (л\час)')
        plt.title(
            'Графики столбцов положения дроссельной заслонки и часового расхода топлива')
        plt.xlabel('Время (с)')
        plt.ylabel('Значения')
        plt.legend()
        plt.show()

    def plot_correlation(self):
        plt.figure(figsize=(10, 5))
        plt.scatter(self.y1, self.y2)
        plt.title(
            'Корреляция между столбцами положения дроссельной заслонки и часового расхода топлива')
        plt.xlabel('Положение дроссельной заслонки (%)')
        plt.ylabel('Часовой расход топлива (л\час)')
        plt.show()

    def calculate_std_dev(self):
        std_dev = self.y2.std()
        print(f'Среднеквадратичное отклонение: {std_dev}')

    def run(self):
        self.plot_graphs()
        self.plot_correlation()
        self.calculate_std_dev()
