from collections import deque 

dfs_path = [] 
bfs_path = []

def DFS(graph, v, visited):
    visited[v] = True 
    dfs_path.append(v)
    for adj in graph[v]:
        if not visited[adj]:
            DFS(graph, adj, visited)

def BFS(graph, v, visited):
    queue = deque([v])
    visited[v] = True 

    while queue:
        v = queue.popleft()
        bfs_path.append(v)
        for adj in graph[v]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True


def main():
    n, m, start_v = list(map(int, input().split())) 
    graph = [list() for i in range(n+1)]
    visited= [False]*(n+1)
   
    
    input_ = [] 
    for i in range(m) :
        item = list(map(int,input().split())) 
        input_.append(item)

    for j in input_ :
        from_, to_ =sorted(j) 
        if to_ not in graph[from_]:
            graph[from_].append(to_)
            graph[from_].sort()
        if from_ not in graph[to_]:   
            graph[to_].append(from_)
            graph[to_].sort()
    DFS(graph, start_v, visited)
    visited= [False]*(n+1)
    BFS(graph, start_v, visited)
    print(*dfs_path)
    print(*bfs_path)


if __name__ =='__main__':
    main()