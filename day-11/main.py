from itertools import product

def solution():
    with open('input.txt') as f:
        raw = f.readlines()
        
    grid = [list(map(lambda x: int(x), list(line.strip()))) for line in raw]
    width = len(grid[0])
    height = len(grid)
    flashes_count = 0
    print(grid)
    
    def flash(y, x):
        for y_, x_ in product([y-1, y, y+1], [x-1, x, x+1]):
             if (y_, x_) != (y, x) and y_ > -1 and y_ < height and x_ > -1 and x_ < width:
                 increase_energy(y_, x_)
                 
    
    def increase_energy(y, x):
        if grid[y][x] > 9:
            return
        grid[y][x] = grid[y][x] + 1
        if grid[y][x] > 9:
            flash(y, x)

    def simulate_step():
        all_flashed = True
        for y in range(height):
            for x in range(width):
                increase_energy(y, x)
        for y in range(height):
            for x in range(width):
                if grid[y][x] > 9:
                    grid[y][x] = 0
                    nonlocal flashes_count
                    flashes_count += 1
                else:
                    all_flashed = False

        return all_flashed
            
    steps = 1
    while True:
        if simulate_step():
            break
        steps += 1
        
    print(steps)
    
        
    
if __name__ == '__main__':
    solution()