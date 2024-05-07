import numpy
from genetic_algorithm import GeneticAlgorithm


def main():
    expected_output = [3, 1, 0, 0, 1, 0, 1, 1, 0, 2]

    def fitness_function(solution):
        score = 0
        for expected, output in zip(expected_output, solution):
            score -= numpy.abs(expected - output)
        return score

    yane_ga = GeneticAlgorithm()
    yane_ga.set_fitness_function(fitness_function)
    yane_ga.set_population_size(10)
    yane_ga.set_max_generations(100)

    yane_ga.run()

    print("Expected output:", expected_output)
    print("Actual output:", yane_ga.get_best_solution())


if __name__ == "__main__":
    main()
