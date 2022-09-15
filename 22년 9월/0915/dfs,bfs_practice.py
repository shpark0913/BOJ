from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


#########################################

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end = ' ')
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

#########################################

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [0] * len(graph)

####################################

dfs(graph, 1, visited)   # 1 2 7 6 8 3 4 5


visited = [0] * len(graph)

bfs(graph, 1, visited)   # 1 2 3 8 7 4 5 6