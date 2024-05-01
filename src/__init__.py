from genetic_algorithm import GeneticAlgorithm
import numpy


def main():
    yane_ga = GeneticAlgorithm()

    function_inputs = [4, -2, 3.5, 5, -11, -4.7]
    desired_output = 44

    def fitness_function(solution):
        output = numpy.sum(numpy.array(function_inputs) * numpy.array(solution))
        fitness = 1.0 / numpy.abs(desired_output - output) + 0.0001
        print(f"Fitness: {fitness}")
        return fitness

    yane_ga.set_fitness_function(fitness_function)
    yane_ga.set_population_size(100)
    yane_ga.set_max_generations(1000)

    yane_ga.run()


if __name__ == "__main__":
    main()
