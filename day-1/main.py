from functools import reduce
import operator

#playing around with closure
def part_one_solution():
    with open('input.txt') as f:
        measurements = list(map(lambda x: int(x.strip()), f.readlines()))
        increases = 0

        def find_increases(a, b):
            if a < b:
                nonlocal increases
                increases += 1
            return b
        reduce(find_increases, measurements)
        print(increases)
        
#trying to do part two in as few lines as possible
def part_two_solution():
    with open('input.txt') as f:
        m = list(map(lambda x: int(x.strip()), f.readlines()))
        three_m = list(map(lambda x: sum(m[x:x+3]), range(0, len(m)-2)))
        print(reduce(operator.add, list(map(lambda x: 1 if three_m[x]<three_m[x+1] else 0, range(0,len(three_m)-1)))))


if __name__ == '__main__':
    part_one_solution()
    part_two_solution()