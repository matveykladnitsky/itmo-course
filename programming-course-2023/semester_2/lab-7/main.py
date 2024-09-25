from tasks import benchmarkTask
from tasks import histogramTask
from tasks import formulaChartTask

# Task 1
benchmarkTask.ArrayMultiplicationBenchmark().run()
# Task 2
histogramTask.ChartPlotter(file_path='./data/data1.csv').run()
# Task 3
formulaChartTask.ThreeDimensionalPlotter().run()
