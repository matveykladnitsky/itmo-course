from tasks import benchmarkTask, histogramTask, formulaChartTask

# Task 1
benchmarkTask.ArrayMultiplicationBenchmark().run()
# Task 2
histogramTask.ChartPlotter(file_path='./data/data1.csv').run()
# Task 3
formulaChartTask.ThreeDimensionalPlotter().run()
