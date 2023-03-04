from collections import defaultdict
def solution():
    with open('input.txt') as f:
        lines = f.readlines()
        
    edges = defaultdict(set)
    for line in lines:
        u, v = line.strip().split('-')
        edges[u].add(v)
        edges[v].add(u)
    
    num_of_paths = 0
    
    discovered = {}
    for vertex in edges.keys():
        discovered[vertex] = 0
    discovered['start'] = 2
    
    def bfs(discovered, curr_vertex, twice):
        if curr_vertex == 'end':
            nonlocal num_of_paths
            num_of_paths += 1
            return
        for connection in edges[curr_vertex]:
            if (discovered[connection] == 1 and not twice) or discovered[connection] <= 0:
                if connection.islower():
                    discovered[connection] += 1
                if discovered[connection] == 2:
                    bfs(discovered, connection, True)
                else:
                    bfs(discovered, connection, twice)
                discovered[connection] -= 1
                
    bfs(discovered, 'start', False)
    
    print(num_of_paths)
    
if __name__ == '__main__':
    solution()