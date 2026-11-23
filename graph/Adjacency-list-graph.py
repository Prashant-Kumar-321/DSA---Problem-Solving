from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')

def solution() -> None:
    vertices = int(input())
    graph = [[]] * vertices

    # Forming the Graph
    for i in range(vertices): 
        adjacency_list = list(map(int, input().split(' ')))
        graph[i] = adjacency_list

    # Find neighbours of given vertices
    # TC = O(|V|)
    vertex = int(input())
    print(f"Neighbours of {vertex}: ", end = " ")

    for neigh in graph[vertex]: 
        print(neigh, end = ", ")
        
    print()

    # Print the Adjacency list graph
    # TC = O(|V| + |E|)
    for i in range(vertices): 
        print(i, end = ": ")
        for neigh in graph[i]: 
            print(neigh, end = " ")

        print()


if __name__ == "__main__":
    solution()