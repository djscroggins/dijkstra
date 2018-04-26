import heapq
import math

def dijkstra(graph, source, target):
    """
    :param dictionary graph: Adjacency list of format string(Key): [(string(Value), int(Distance))]
    :param string source: starting vertex
    :param string target: target vertex
    :return tuple: (shortest_path, length of shortest_path)
    """
    parent = {v: None for v in graph}
    distance = {v: math.inf for v in graph}
    distance[source] = 0
    min_heap = []
    seen = set()

    heapq.heappush(min_heap, [distance[source], source])

    while min_heap:
        # Heap items format: (int(distance), string(vertex))
        u_tuple = heapq.heappop(min_heap)
        u = u_tuple[1]
        if u not in seen:
            seen.add(u)
            for neighbor in graph[u]:
                # Graph dict values format: (string(vertex), int(weight))
                v = neighbor[0]
                weight_uv = neighbor[1]
                if distance[v] > distance[u] + weight_uv:
                    distance[v] = distance[u] + weight_uv
                    heapq.heappush(min_heap, [distance[v], v])
                    parent[v] = u

    # build solution
    shortest_path = []
    vertex = target
    while True:
        shortest_path.append(vertex)
        if vertex is None:
            break
        vertex = parent[vertex]
    shortest_path.reverse()

    # function will return 'None' as source of path. Slicing removes it.
    # Can be avoided by 'if vertex == source,' but prefer None as hard check on end of path.
    return shortest_path[1:], distance[target]

def generate_adjacency_list(file_name):
    """
    Generates undirected graph as dict adjacency list format: {u: (v, weight)}, {v: (u, weight)}
    """
    graph = {}
    with open(file_name, 'r') as file:
        next(file)
        for line in file:
            u, v, weight = line.split()
            graph.setdefault(u, []).append((v, int(weight)))
            graph.setdefault(v, []).append((u, int(weight)))
    return graph

if __name__ == "__main__":

    test_files = ['Case1.txt', 'Case2.txt', 'Case3.txt']
    graphs = [generate_adjacency_list(file) for file in test_files]

    (source, target) = ('A', 'B')   
    solutions = [dijkstra(graph, source, target) for graph in graphs]

    for i in range(len(solutions)):
        print('dijkstra({0}) --> {1} Length = {2}'.format(test_files[i], solutions[i][0], solutions[i][1]), '\n')
