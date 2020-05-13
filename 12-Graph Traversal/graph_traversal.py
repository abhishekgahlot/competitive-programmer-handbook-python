graph = {1: [2, 4], 2: [1, 3, 5], 3: [2, 5], 4: [1], 5: [2, 3]}


# =======================
# Depth first search

def dfs(s):
	visited = [0] * (len(graph) + 1)
	if (visited[s]): return
	visited[s] = True
	print(s)
	for u in graph[s]:
		dfs(u)


dfs(1)


# ==================
# breadth first search

def bfs():
    visited = [0] * (len(graph) + 1)
    distance = [0] * (len(graph) + 1)
    visited[1] = True
    q = [1]

    while len(q) > 0:
        s = q.pop()
        print(s)
        for u in graph[s]:
            if visited[u]: continue
            visited[u] = True
            distance[u] = distance[s] + 1
            q.append(u)
    print(distance[1:])


bfs()

# =======================
# Bellman-Ford shortest distance
import math

e_list = [[1, 2, 5], [1, 4, 7], [1, 3, 3], [2, 1, 5], [2, 4, 3], [2, 5, 2],
          [3, 1, 3], [3, 4, 1], [4, 3, 1], [4, 1, 7], [4, 5, 2], [5, 4, 2], [5, 2, 2]]


def shortest():
    distance = [math.inf for _ in range(len(e_list) + 1)]
    distance[1] = 0
    for e in e_list:
        a, b, w = e
        distance[b] = min(distance[b], distance[a] + w)
    print(distance[1:])


shortest()

# ==============================================================
# Dijkstra's algo
import heapq

graph = {1: [(2, 5), (4, 9), (5, 1)], 2: [(1, 5)], 4: [(1, 9), (5, 1)], 5: [(1, 1), (4, 2)]}


def dijkstra():
    distance = [math.inf for _ in range(6)]
    distance[1] = 0
    stack = [(0, 1)]
    heapq.heapify(stack)
    while stack:
        w, n = heapq.heappop(stack)
        for e in graph[n]:
            if distance[n] + e[1] < distance[e[0]]:
                distance[e[0]] = distance[n] + e[1]
                heapq.heappush(stack, (e[1], e[0]))
    print(distance[1:])


dijkstra()
