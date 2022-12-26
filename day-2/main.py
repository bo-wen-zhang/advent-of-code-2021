def get_input():
    parseInt = lambda x : [x[0],int(x[1])]
    with open('input.txt') as f:
        return list(map(lambda x : parseInt(x.strip().split(' ')), f.readlines()))

#playing with switch case
def part_one_solution():
    lines = get_input()
    hpos, depth = 0, 0
    for [dir, mag] in lines:
        match dir:
            case 'up':      depth -= mag
            case 'down':    depth += mag
            case 'forward': hpos += mag
    print(hpos*depth)
            
def part_two_solution():
    lines = get_input()
    aim, hpos, depth = 0, 0, 0
    for [dir, mag] in lines:
        if dir == 'up':
            aim -= mag
        if dir == 'down':
            aim += mag
        if dir == 'forward': 
            hpos += mag; depth += aim * mag
    print(hpos*depth)   
        

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()