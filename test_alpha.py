class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Example tree:
#        3
#      / | \
#     5  2  9
#    /|\    |
#   1 8 4   7

# leaf1 = TreeNode(1)
# leaf2 = TreeNode(8)
# leaf3 = TreeNode(4)
# leaf4 = TreeNode(7)

# subtree1 = TreeNode(5, [leaf1, leaf2, leaf3])
# subtree2 = TreeNode(2)
# subtree3 = TreeNode(9, [leaf4])

# root = TreeNode(3, [subtree1, subtree2, subtree3])
leaf1 = TreeNode(9)
leaf2 = TreeNode(0)
leaf3 = TreeNode(1)
leaf4 = TreeNode(7)

subtree1 = TreeNode(3, [leaf1, leaf2])

subtree3 = TreeNode(5, [leaf3,leaf4])

root = TreeNode(2, [subtree1,  subtree3])

# Applying Alpha-Beta Pruning
result = alpha_beta_pruning(root, 3, float('-inf'), float('inf'), True)
print("Result:", result)


#############################################################################

########################################################################
# import random
# import math

# # Genetic Algorithm: 2x^2 + 5

# # 1. create a population of random chromosomes
# def create_chromosome(length):
#     return [random.choice([0, 1]) for _ in range(length)]

# def create_population(population_size, chromosome_length):
#     return [create_chromosome(chromosome_length) for _ in range(population_size)]

# # 2. calculate the fitness of each chromosome
# def fitness(chromosome):
#     x = sum([gene * math.pow(2, i) for i, gene in enumerate(chromosome)])
#     return 2 * math.pow(x, 2) + 5

# def calculate_fitness(population):
#     return [fitness(chromosome) for chromosome in population]

# # 3. select the best fit chromosomes using tournament selection
# def tournament_selection(population, fitness_list, tournament_size):
#     selected_population = []
#     for _ in range(len(population)):
#         tournament_indices = random.sample(range(len(population)), tournament_size)
#         tournament_fitness = [fitness_list[i] for i in tournament_indices]
#         selected_population.append(population[tournament_indices[tournament_fitness.index(max(tournament_fitness))]])
#     return selected_population

# # 4. crossover and mutate the chromosomes
# def crossover(chromosome1, chromosome2, crossover_rate):
#     if random.random() < crossover_rate:
#         crossover_point = random.randint(0, len(chromosome1))
#         new_chromosome = chromosome1[:crossover_point] + chromosome2[crossover_point:]
#         return new_chromosome
#     else:
#         return chromosome1

# def mutate(chromosome, mutation_rate):
#     mutated_chromosome = chromosome[:]
#     for i in range(len(mutated_chromosome)):
#         if random.random() < mutation_rate:
#             mutated_chromosome[i] = 1 - mutated_chromosome[i]  # flip 0 to 1 or 1 to 0
#     return mutated_chromosome

# def crossover_and_mutate(population, crossover_rate, mutation_rate):
#     new_population = []
#     for i in range(0, len(population), 2):
#         offspring1 = crossover(population[i], population[i + 1], crossover_rate)
#         offspring2 = crossover(population[i + 1], population[i], crossover_rate)
#         new_population.extend([mutate(offspring1, mutation_rate), mutate(offspring2, mutation_rate)])
#     return new_population

# # 5. repeat from step 2 until the best fit is found
# def genetic_algorithm(population_size, chromosome_length, generations, tournament_size, crossover_rate, mutation_rate):
#     population = create_population(population_size, chromosome_length)
#     fitness_list = calculate_fitness(population)
#     generation = 0

#     while max(fitness_list) != 21 and generation < generations:
#         population = tournament_selection(population, fitness_list, tournament_size)
#         population = crossover_and_mutate(population, crossover_rate, mutation_rate)
#         fitness_list = calculate_fitness(population)
#         generation += 1

#     best_chromosome_index = fitness_list.index(max(fitness_list))
#     best_chromosome = population[best_chromosome_index]
#     x = sum([gene * math.pow(2, i) for i, gene in enumerate(best_chromosome)])
#     print("Generation: ", generation)
#     print("Chromosome: ", best_chromosome)
#     print("Fitness: ", fitness_list[best_chromosome_index])
#     print("x = ", x)
#     print("2x^2 + 5 = ", 2 * math.pow(x, 2) + 5)

#     return best_chromosome

# genetic_algorithm(population_size=100, chromosome_length=4, generations=1000, tournament_size=3, crossover_rate=0.3, mutation_rate=0.1)