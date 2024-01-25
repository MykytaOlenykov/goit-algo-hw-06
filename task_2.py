from collections import deque

from task_1 import graph
from dfs import dfs
from bfs import bfs


def format_graph(graph):
    formatted_graph = dict()

    for edge in graph:
        from_node = edge[0]
        to_node = edge[1]

        if from_node in formatted_graph:
            formatted_graph[from_node].append(to_node)
        else:
            formatted_graph[from_node] = [to_node]

    return formatted_graph


def main():
    formatted_graph = format_graph(graph)

    print("dfs steps:")
    dfs(formatted_graph, "Bob's House")

    print("\nbfs steps:")
    bfs(formatted_graph, deque(["Bob's House"]))


if __name__ == "__main__":
    main()

# {
#     "Bob's House": ["Town Hall"],
#     "Alice's House": ["Cabin"],
#     "Cabin": ["Marketplace"],
#     "Post Office": ["Alice's House", "Bob's House"],
#     "Town Hall": ["Marketplace"],
#     "Daria's House": ["Town Hall"],
#     "Ernie's House": ["Daria's House", "Farm"],
#     "Grete's House": ["Ernie's House"],
#     "Farm": ["Grete's House"],
#     "Shop": ["Grete's House", "Town Hall"],
#     "Marketplace": ["Post Office", "Shop"],
# }
