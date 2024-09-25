import numpy as np
import random
import time


class ArrayMultiplicationBenchmark:
    def __init__(self, size=1_000_000):
        self.size = size
        self.list1 = [random.random() for _ in range(self.size)]
        self.list2 = [random.random() for _ in range(self.size)]
        self.array1 = np.random.rand(self.size)
        self.array2 = np.random.rand(self.size)

    def run(self):
        start_time = time.perf_counter()
        result_list = [self.list1[i] * self.list2[i] for i in range(self.size)]
        end_time = time.perf_counter()
        list_time = end_time - start_time
        print(f"Время выполнения перемножения списков: {list_time:.6f} секунд")

        start_time = time.perf_counter()
        result_array = np.multiply(self.array1, self.array2)
        end_time = time.perf_counter()
        array_time = end_time - start_time
        print(
            f"Время выполнения перемножения массивов NumPy: {array_time:.6f} секунд")

        return list_time, array_time
