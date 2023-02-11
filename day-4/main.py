import re
from collections import deque

def solution():
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    drawing_numbers = deque(map(lambda x: int(x), data[0].strip().split(',')))
    boards = []
    for i in range(1, len(data)):
        boards.append([list(map(lambda x: [int(x), False], re.split('\s+', row.strip()))) for row in data[i].split('\n')])
    while drawing_numbers:
        curr = drawing_numbers.popleft()
        for board in boards:
            for y in range(5):
                for x in range(5):
                    if board[y][x][0] == curr:
                        board[y][x][1] = True
        winners = []
        for id, board in enumerate(boards):
            if has_won(board):
                if len(boards) == 1:
                    return winning_board(board)*curr
                winners.append(id)
        boards = [board for id, board in enumerate(boards) if id not in winners]
        
def has_won(board):
    for row in board:
        if all([b for i, b in row]):
            return True
    for x in range(5):
        if all([board[y][x][1] for y in range(5)]):
            return True
    return False

def winning_board(board):
    total = 0
    for y in range(5):
        for x in range(5):
            if not board[y][x][1]:
                total += board[y][x][0]
    return total    

if __name__ == '__main__':
    print(solution())