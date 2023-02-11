def solution():
    with open('input.txt') as f:
        initial_population = [int(x) for x in f.readline().split(',')]
    
    
        
    population = {}
    for age in initial_population:
        population[age] = population.get(age, 0) + 1

    day = 1
    while day <= 256:
        new_population = {}
        for age in range(0, 8):
            new_population[age] = population.get(age+1, 0)
        new_population[8] = population.get(0, 0)
        new_population[6] += population.get(0, 0)
        population = new_population
        #print('day', day, population)
        day += 1
    return sum(population.values())
    
if __name__ == '__main__':
    print(solution())