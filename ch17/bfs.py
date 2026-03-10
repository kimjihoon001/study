# bfs.p

myGraph = {
    'A':['B','C','D'],
    'B':['A','E'],
    'C':['A','F','G'],
    'D':['A','H'],
    'E':['B','I'],
    'F':['C','J'],
    'G':['C'],
    'H':['D'],
    'I':['E'],
    'J':['F']
    }

def my_bfs(graph,start):
    queue = []
    visited = []
    
    queue.append(start)
    
    
    while queue:
        
        node = queue.pop(0)
        
        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)
            
    print("bfs - ", visited)
    return visited

my_bfs(myGraph, 'C')
        