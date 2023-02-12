from collections import deque
from functools import reduce
def solution():
    with open('input.txt') as f:
        raw = f.readlines()
    
    grid = [list(line.strip()) for line in raw]
    
    def is_lowest(y, x):
        if x > 0 and grid[y][x] >= grid[y][x-1]:
            return False
        if x < width-1 and grid[y][x] >= grid[y][x+1]:
            return False
        if y > 0 and grid[y][x] >= grid[y-1][x]:
            return False
        if y < height-1 and grid[y][x] >= grid[y+1][x]:
            return False
        return True
    
    height = len(grid)
    width = len(grid[0])
    low_points = deque()
    for y in range(height):
        for x in range(width):
            if is_lowest(y, x):
                low_points.append((y, x))      
    
    basin_sizes = []
    discovered = [[False for _ in range(width)] for _ in range(height)]
    
    while low_points:
        curr_low_pt = low_points.popleft()
        basin_size = 1
        discovered[curr_low_pt[0]][curr_low_pt[1]] = True
        basin = deque([curr_low_pt])
        while basin:
            y, x = basin.popleft()
            if x > 0 and grid[y][x-1] < '9' and not discovered[y][x-1]:
                discovered[y][x-1] = True
                basin.append((y, x-1))
                basin_size += 1
            if x < width-1 and grid[y][x+1] < '9' and not discovered[y][x+1]:
                discovered[y][x+1] = True
                basin.append((y, x+1))
                basin_size += 1
            if y > 0 and grid[y-1][x] < '9' and not discovered[y-1][x]:
                discovered[y-1][x] = True
                basin.append((y-1, x))
                basin_size += 1
            if y < height-1 and grid[y+1][x] < '9' and not discovered[y+1][x]:
                discovered[y+1][x] = True
                basin.append((y+1, x))
                basin_size += 1
                
        basin_sizes.append(basin_size)
            
    basin_sizes.sort(reverse=True)
    return reduce(lambda x, y: x*y, basin_sizes[:3], 1)
    
if __name__ == '__main__':
    print(solution())