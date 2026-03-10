#

myGraph = {
    1:[2,3,4],
    2:[1,5],
    3:[1,6],
    4:[1,6],
    5:[2,6],
    6:[3,4,5]
    }

def dfs_bfs(graph,start):
    stack = []
    queue = []
    s_visited = []
    q_visited = []
    
    stack.append(start)
    queue.append(start)
    
    while stack:
        s_node=stack.pop()
        
        if s_node not in s_visited:
            stack.extend(reversed(graph[s_node]))
            s_visited.append(s_node)
    while queue:
        q_node=queue.pop(0)
        
        if q_node not in q_visited:
            queue.extend(graph[q_node])
            q_visited.append(q_node)
            
    print("dfs - ", s_visited)
    print("bfs - ", q_visited)
    return s_visited,q_visited

dfs_bfs(myGraph,1)