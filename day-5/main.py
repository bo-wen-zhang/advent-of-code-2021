import re

def solution():
    with open('input.txt') as f:
        raw_txt = f.readlines()
    
    ocean_floor = {}    
    vent_lines = list(map(lambda x: [int(elem) for elem in re.split('\s->\s|,', x.strip())], raw_txt))

    for line in vent_lines:
        x1, y1, x2, y2 = line
        if (x:=x1) == x2:
            start = min(y1, y2)
            end = max(y1, y2)
            for y in range(start, end+1):
                ocean_floor[(x,y)] = ocean_floor.get((x,y), 0) + 1
        elif (y:=y1) == y2:
            start = min(x1, x2)
            end = max(x1, x2)
            for x in range(start, end+1):
                ocean_floor[(x,y)] = ocean_floor.get((x,y), 0) + 1
        else:
            if x2 < x1:
                x_arr = [x for x in range(x1, x2-1, -1)]
            else:
                x_arr = [x for x in range(x1, x2+1)]
            if y2 < y1:
                y_arr = [y for y in range(y1, y2-1, -1)]
            else:
                y_arr = [y for y in range(y1, y2+1)]
            for x, y in zip(x_arr, y_arr):
                ocean_floor[(x,y)] = ocean_floor.get((x,y), 0) + 1
    
    return len([val for val in ocean_floor.values() if val > 1 ])
    
if __name__ == '__main__':
    print(solution())