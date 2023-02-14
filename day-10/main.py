def solution():
    with open('input.txt') as f:
        raw = f.readlines()
        
    lines = [line.strip() for line in raw]
    
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
                    top = stack.pop()
                    if pairing_lookup[top] != char:
                        error_score += error_score_lookup[char]
                        break
        else:
            #print(''.join(stack))
            completion_score = 0
            while stack:
                completion_score *= 5
                char = stack.pop()
                completion_score += completion_score_lookup[char]
            completion_scores.append(completion_score)
    
    completion_scores.sort()
                 
    return error_score, completion_scores[len(completion_scores)//2]

if __name__ == '__main__':
    print(solution())