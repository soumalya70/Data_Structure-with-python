from collections import deque

MAX_M = 20
MAX_N = 20

class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

class CustomQueue:
    def _init_(self):
        self.array = [None] * (MAX_M * MAX_N)
        self.front = -1
        self.rear = -1

def init_queue(q):
    q.front = -1
    q.rear = -1

def is_empty(q):
    return q.front == -1

def enqueue(q, p):
    if is_empty(q):
        q.front = 0
        q.rear = 0
    else:
        q.rear += 1
    q.array[q.rear] = p

def dequeue(q):
    p = q.array[q.front]
    if q.front == q.rear:
        q.front = -1
        q.rear = -1
    else:
        q.front += 1
    return p

def max_val(a, b):
    return max(a, b)

def min_val(a, b):
    return min(a, b)

def max_thief_time(m, n, fortress):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    placementlelo = 0

    distance = bfs(0, 0, m, n, fortress, directions)
    placementlelo = distance

    for i in range(m):
        for j in range(n):
            if fortress[i][j] == 0:
                fortress[i][j] = 1
                distance = bfs(0, 0, m, n, fortress, directions)
                placementlelo = max_val(placementlelo, distance)
                fortress[i][j] = 0

    return placementlelo

def bfs(start_x, start_y, m, n, fortress, directions):
    visited = [[False] * MAX_N for _ in range(MAX_M)]
    distance = [[0] * MAX_N for _ in range(MAX_M)]
    q = CustomQueue()
    init_queue(q)
    start = Point(start_x, start_y)
    enqueue(q, start)
    visited[start_x][start_y] = True

    while not is_empty(q):
        p = dequeue(q)

        for i in range(4):
            nx = p.x + directions[i][0]
            ny = p.y + directions[i][1]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and fortress[nx][ny] <= 0:
                distance[nx][ny] = distance[p.x][p.y] + 1
                visited[nx][ny] = True
                new_point = Point(nx, ny)
                enqueue(q, new_point)

    return distance[m - 1][n - 1]

if __name__ == "_main_":
    m, n = map(int, input().split())
    fortress = [list(map(int, input().split())) for _ in range(m)]

    result = max_thief_time(m, n, fortress)
    print(result)