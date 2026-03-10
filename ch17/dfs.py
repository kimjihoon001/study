# def.py

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
from ch17.graph import myGraph

def my_dfs(graph, start_node):
    # 1. 탐색할 노드를 담을 스텍
    stack = list()
    # 2. 방문 여부 확인 리스트
    visited = list()
    # 3. 탐색 시작 노드
    stack.append(start_node)
    
    while stack:
        # 4. 방문할 노드를 스텍에서 제거
        node = stack.pop()
        # 5. 방문 리스트에 스텍에서 꺼낸 노드가 없으면,
        if node not in visited:
            # 인접노드를 스텍에 추가
            stack.extend(reversed(graph[node]))
            # 방문처리
            visited.append(node)
    print("dfs - ", visited)
    return visited
my_dfs(myGraph, 'C')
