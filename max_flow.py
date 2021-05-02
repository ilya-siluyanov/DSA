from collections import deque
from typing import List

adj_matrix = []  # type: List[List[int]]
residual_network = []  # type: List[List[int]]
flow = []  # type :List[List[int]]
n = 0


def get_augmenting_path(source: int, sink: int) -> List[int]:
    global n
    q = deque()
    used = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    q.append(source)
    used[source] = True
    while len(q) > 0:
        v = q.popleft()
        if v == sink:
            break
        for to, value in enumerate(residual_network[v]):
            if not used[to] and value > 0:
                parent[to] = v
                used[to] = True
                if to == sink:
                    break
                q.append(to)
        if parent[sink] != -1:
            break
    if parent[sink] == -1:
        return []
    else:
        curr = sink
        path = []
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        return path


def build_residual_network():
    global residual_network
    for i in range(1, n):
        for j in range(1, n):
            if adj_matrix[i][j] > 0:
                residual_network[i][j] = adj_matrix[i][j] - flow[i][j]
            elif adj_matrix[j][i] > 0:
                residual_network[i][j] = flow[j][i]


def main():
    global adj_matrix, residual_network, n, flow
    n, m = map(int, input().split())
    n += 1
    adj_matrix = [[0] * n for _ in range(n)]
    residual_network = [[0] * n for _ in range(n)]
    flow = [[0] * n for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        adj_matrix[a][b] = c
    max_flow = 0
    while True:
        build_residual_network()
        augmenting_path = get_augmenting_path(1, n - 1)
        if len(augmenting_path) > 0:
            min_edge = 101
            for i in range(len(augmenting_path) - 1):
                edge = residual_network[augmenting_path[i]][augmenting_path[i + 1]]
                min_edge = min(min_edge, edge)
            for i in range(len(augmenting_path) - 1):
                flow[augmenting_path[i]][augmenting_path[i + 1]] += min_edge
            max_flow += min_edge
        else:
            break
    print(max_flow)


if __name__ == '__main__':
    main()
