import collections
def part_one():
    with open('input.txt') as f:
        raw = f.readlines()
        
    patterns = list(map(lambda x: x.split('|')[1].strip().split(' '), raw))
    appearances = 0
    possible_lengths = set([2, 4, 3, 7])
    
    for line in patterns:
        for digit in line:
            if len(digit) in possible_lengths:
                appearances += 1
    
    return appearances

def part_two():
    with open('input.txt') as f:
        raw = f.readlines()
        
    patterns = list(map(lambda x: x.strip().split(' | '), raw))
    signal_patterns = [p[0].split(' ') for p in patterns]
    digits = [p[1].split(' ') for p in patterns]
    
    total_output = 0
    
    for signal_patterns, digits in patterns:
        signal_patterns = signal_patterns.split(' ')
        signal_patterns.sort(key=lambda x: len(x))
        digits = digits.split(' ')
        lookup = {}
        line_output = ''
        lookup['1'] = set(signal_patterns[0])
        lookup['7'] = set(signal_patterns[1])
        lookup['4'] = set(signal_patterns[2])
        lookup['8'] = set(signal_patterns[-1])
        for i in range(6, 9):
            s = set(signal_patterns[i])
            if not lookup['1'].issubset(s):
                lookup['6'] = s
            elif not lookup['4'].issubset(s):
                lookup['0'] = s
            else:
                lookup['9'] = s
        for i in range(3, 6):
            s = set(signal_patterns[i])
            if lookup['1'].issubset(s):
                lookup['3'] = s
            elif s.issubset(lookup['9']):
                lookup['5'] = s
            else:
                lookup['2'] = s
                
        for digit in digits:
            for n in lookup:
                if set(digit) == lookup[n]:
                    line_output += n
                    break
        total_output += int(line_output)
            
    return total_output
    
if __name__ == '__main__':
    print(f'part one: {part_one()} \npart two: {part_two()}')