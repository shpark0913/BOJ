def dfs(root):
    stack = []
    stack.append(root)
    depth = 1

    while stack:
        node = stack.pop()
        if not visited[node]:

            visited[node] = depth
            depth += 1
            stack += sorted(graph[node], reverse=True)

N, M, R = map(int, input().split())

visited = [0] * (N + 1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(R)
print(*visited[1:])