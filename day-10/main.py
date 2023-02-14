def solution():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    
    pairing_lookup = {
        '{' : '}',
        '[' : ']',
        '(' : ')',
        '<' : '>'
    }
    
    error_score_lookup = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137
    }
    
    completion_score_lookup = {
        '(' : 1,
        '[' : 2,
        '{' : 3,
        '<' : 4
    }
    
    error_score = 0
    completion_scores = []
    
    for line in lines:
        stack = []
        for char in line:
            match char:
                case '{' | '(' | '[' | '<':
                    stack.append(char)
                case _:
                    if pairing_lookup[stack.pop()] != char:
                        error_score += error_score_lookup[char]
                        break
        else:
            completion_score = 0
            while stack:
                completion_score = completion_score * 5 + completion_score_lookup[stack.pop()]
            completion_scores.append(completion_score)
    
    completion_scores.sort()
                 
    return f'part one: {error_score}\npart two: {completion_scores[len(completion_scores)//2]}'

if __name__ == '__main__':
    print(solution())