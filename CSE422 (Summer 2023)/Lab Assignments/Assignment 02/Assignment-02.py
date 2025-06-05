### CSE422 - Artificial Intelligence
### Assignment 02: Genetic Algorithm
### ----------------------------------
### Name : Mirza Meherab Hosen Rudra
### ID   : 21101048
### Sec  : 10
### ----------------------------------
# !!! Please Rerun the program if the test case doesn't match !!!
### ----------------------------------
### Input.txt file Format:
### ----------------------
# Total Test Cases
# Total Batsmen, Target Score
# Batsmen Name, Average Runs ...
# ...
"""
3
8 330
Tamim 68
Shoumyo 25
Shakib 70
Afif 53
Mushfiq 71
Liton 55
Mahmudullah 66
Shanto 29
5 240
Bradman 120
Tendulkar 90
Sangakkara 70
Kallis 65
Lara 80
4 100
Ralph 80
John 70
Tom 40
Young 50
"""


import random

    
def calculate_fitness(selected_batsmen, batsmen_data, target_score):
    total_runs = 0
    # If the batsman is selected, add his runs to the total runs
    for name, selected in zip(batsmen_data.keys(), selected_batsmen):
        if selected == 1:
            total_runs += batsmen_data[name]

    # if the total runs are greater than or equal to the target score, return the difference
    return total_runs - target_score if total_runs >= target_score else float("inf")


def crossover(parent1, parent2):
    # Select a random crossover point
    crossover_point = random.randint(1, len(parent1) - 1)

    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2


def mutate(solution, mutation_rate):
    mutated_solution = []
    for gene in solution:
        if random.random() < mutation_rate:
            mutated_solution.append(1 - gene)
        else:
            mutated_solution.append(gene)

    return mutated_solution


def genetic_algorithm(
    total_batsmen,
    target_score,
    batsmen_data,
    population_size,
    mutation_rate,
    max_iterations,
):
    # radomly generating all the initial population
    population = [
        [random.randint(0, 1) for _ in range(total_batsmen)]
        for _ in range(population_size)
    ]

    best_fitness = float("inf")
    best_solution = None

    for _ in range(max_iterations):
        # Calculate the fitness score for each solution / cromosome in the population
        fitness_scores = [
            calculate_fitness(solution, batsmen_data, target_score)
            for solution in population
        ]

        # Check if any solution has a fitness score of 0 (target score achieved)
        for i in range(population_size):
            if fitness_scores[i] == 0:
                return population[i]

            # Update the best solution if a better fitness score is found
            if fitness_scores[i] < best_fitness:
                best_fitness = fitness_scores[i]
                best_solution = population[i]

        # ---------- Selection ----------
        sorted_population = []

        # Sort the population based on fitness scores
        fitness_population = list(zip(fitness_scores, population))
        fitness_population.sort(key=lambda pair: pair[0])

        # Extract the sorted population
        for _, x in fitness_population:
            sorted_population.append(x)

        # Select the top half of the sorted population
        selected_population = sorted_population[: population_size // 2]

        # ---------- Crossover ----------
        new_population = selected_population.copy()
        while len(new_population) < population_size:
            parent1 = random.choice(selected_population)
            parent2 = random.choice(selected_population)

            child1, child2 = crossover(parent1, parent2)

            new_population.append(child1)
            if len(new_population) < population_size:
                new_population.append(child2)

        # ---------- Mutation ----------
        for i in range(1, population_size):
            new_population[i] = mutate(new_population[i], mutation_rate)

        population = new_population

    return best_solution


# Function to format the output
def format_output(batsmen_data, selected_batsmen, target_score):
    # Get all the batsmen names
    all_names = list(batsmen_data.keys())

    selected_names = []
    for name, selected in zip(all_names, selected_batsmen):
        if selected == 1:
            selected_names.append(name)

    total_runs = 0
    # verfying if Genetic Algorithm has selected the
    # correct batsmen combination
    for name in selected_names:
        total_runs += batsmen_data[name]

    if total_runs == target_score:
        binary_string = ""
        for selected in selected_batsmen:
            binary_string += str(selected)

        return all_names, binary_string

    else:
        return all_names, -1


def main():
    # Read input from Input-file
    with open("Lab Assignments/Assignment 02/Input.txt", "r") as file:
        total_test_cases = int(file.readline())

        # Processing each test case
        for _ in range(total_test_cases):
            total_batsmen, target_score = map(int, file.readline().split())
            batsmen_data = {}
            for _ in range(total_batsmen):
                name, average_runs = file.readline().split()
                batsmen_data[name] = int(average_runs)

            # Setting the genetic algorithm parameters
            population_size = 75
            mutation_rate = 0.01
            max_iterations = 1500

            best_solution = genetic_algorithm(
                total_batsmen,
                target_score,
                batsmen_data,
                population_size,
                mutation_rate,
                max_iterations,
            )

            # Format and print the output
            output = format_output(batsmen_data, best_solution, target_score)
            print(*output, sep="\n")

            # Print a newline to separate test cases if there's more than one
            print()


# Run the program
if __name__ == "__main__":
    main()
