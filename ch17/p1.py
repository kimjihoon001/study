#p1.py
# map1 = [
#     [0,0,1,0,1],
#     [1,0,1,0,0],
#     [0,0,1,1,0],
#     [0,1,0,0,0],
#     [0,0,0,1,1]
# ]


map2 = [
    [0,1,1,1,1,1],
    [0,1,0,0,0,1],
    [0,1,0,1,0,1],
    [0,1,0,1,0,0],
    [0,0,0,1,1,0],
    [1,1,1,1,1,0]
]

moves = [
    [-1,0],
    [1,0],
    [0,-1],
    [0,1]
    ]

def my_dfs(map,start):
    stack=[]
    visited=[]
    
    stack.append(start)
    
    while stack:
        x,y =stack.pop()
        
        if [x,y] not in visited:
            visited.append([x,y])
            for k in range(4):
                i,j = moves[k]
                new_x = x+i
                new_y = y+j
                if 0<= new_x <=5 and 0<= new_y <=5 and map[new_x][new_y] == 0:           
                    stack.append([new_x,new_y])    
    return visited                
print('로봇 경로는 :', my_dfs(map2,[0,0]))
                    
        

# def solve_maze(maze, start):        
#     stack = [start]
#     visited = list()

#     while stack:
#         r,c = stack.pop()
        
#         if (r,c) not in visited:
#             visited.append((r,c))

#             for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 nr, nc = r + dr, c + dc
#                 if 0<= nc < 6 and 0 <= nr < 6 and maze[nr][nc] == 0:
#                     stack.append((nr,nc))
#     return visited

# print("로봇 탐색 경로: ", solve_maze(map2, (0,0)))


# (0,0) => (0,1)    # 오른쪽 이동
# (0,0) => (0,-1)   # 왼쪽 이동
# (0,0) => (1,0)    # 아래 이동
# (0,0) => (-1,0)   # 위 이동

# 범위
# 열 0~5
# 행 0~5

               