from pathlib import Path
import sys
import math

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')


def bfs(graph: list[list[bool]], source: int, predecesor: list[int], shortest_path: list[int], level: int) -> None: 
    curr_level = [source]
    visited = [False] * len(graph)
    shortest_path[source] = 0
    visited[source] = True

    while curr_level: 
        next_level = list()

        for u in curr_level: 
            for i in range(len(graph[u])): 
                if graph[u][i] and not visited[i]: 
                    next_level.append(i)
                    predecesor[i] = u 
                    shortest_path[i] = level
                    visited[i] = True

        level += 1
        curr_level = next_level
        next_level = list()


def print_shortest_path(predecesor: list[int], dest: int) -> None: 
    if predecesor[dest] == -1: 
        print(dest, end="") 
        return

    print_shortest_path(predecesor, predecesor[dest]) 

    print(f" --> {dest}", end = "")

# Breadth First Search
def breadth_first_search(graph: list[list[bool]], source: int) -> tuple[list[int], list[int]]:
    """
        Traverse the Graph Level wise and return Predecesor list, distance of shortest path from given source
    """
    predecesor = [-1] * len(graph)
    shortest_path = [math.inf] * len(graph)

    shortest_path[source] = 0

    # Internal Breadth First Search Method
    bfs(graph, source, predecesor, shortest_path, level=0)

    return predecesor, shortest_path


def solution() -> None:
    vertices = int(input())
    edges = int(input())

    # Adjacency Matrix Representation of the Graph
    graph = [[False] * vertices for _ in range(vertices)]

    # Record the Edges 
    for _ in range(edges): 
        v, w = list(map(int, input().split()))
        graph[v][w] = True

    source = 0
    predecesor, shortest_paths = breadth_first_search(graph, source=source)

    print_shortest_path(predecesor, 2)  


if __name__ == "__main__":
    solution()