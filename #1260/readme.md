## what i leaned 
+ DFS/BFS

## DFS/BFS

+ Search : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
+ ex) DFS/BFS 

## 스택 구현 예제
+ 삽입/삭제

```python
stack =[] 

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.append(4)
print(stack)

print(stack[::-1]) # 최상단 원소 부터 출력
```

## Background : 큐
+ 선입 선출 구조

```python
from collections import deque 
# list 보다 queue 자료 구조 이용하는게 시간 복잡도가 낮음
queue= deque()

queue.append(5)
queue.append(3)
queue.append(2)
queue.append(1)
queue.popleft() # 상수시간 복잡도 

print(queue)
print(queue)


```

## Background : 재귀함수
+ 자기 자신을 다시 호출하는 함수 
+ python에는 재귀함수의 깊이 제한이 있음. 오류메세지발생
+ 모든 재귀함수는 반복문을 이용하여 동일한 기능 구현 가능
    + 유/불리는 문제마다 다름
+ 컴퓨터가 함수를 연속적으로 호출하면, 메모리 내부의 스택 프레임에 쌓임
    + 스택을 사용해야할때는, 스택 라이브러리 대신 재귀함수를 이용하는 경우가 많음

```python
# 마치 스택과 같음
def recursive_func(i):
    # 100번째 호출했을때 종료하도록 명시
    if i ==100:
        return
    print(f"{i}번째 재귀함수에서 {i+1} 번째 재귀함수를 호출합니다.")
    recursive_func(i+1)
    print(f'{i} 번째 재귀함수를 종료합니다.')

recursive_func(1)

```

## DFS (Depth First Search)
+ 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
+ DFS는 스택 자료구조(or 재귀함수)를 이용함.

1) 탐색 시작 노드를 스택에 삽입하고 방문 처리.

2) 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면, 그 노드를 스택에 넣고 방문 , 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄.

3) 더이상 2번 과정을 수행할 수 없을 때까지 반복.


```python
# 각 노드가 연결된 정보를 표현 2차원 리스트
graph = [
         [],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
]
# 각 노드가 방문된 정보를 표현
visited = [False]*9 

def dfs(graph, v, visited):
    visited[v] = True 
    print(v, end =' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited) 

```

## BFS (Breadth - First Search)

+ BFS 너비 우선 탐색이라 부름. 가까운 노드부터 우선적으로 탐색하는 알고리즘
+ 큐 자료구조 이용.

1) 탐색 시작 노드를 큐에 삽입하고 방문 처리함.

2) 큐에서 노드를 꺼낸뒤 해당 노드의 인접노드 중에서 방문하지 않은 노드를 모두 큐에서 삽입하고 방문 처리.

3) 2번을 수행할수 없을때 까지 반복

```python 
from collections import deque 

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] =  True 

    # 큐가 빌때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

```