from task_1 import graph
from dijkstra import dijkstra


def format_graph(graph):
    formatted_graph = dict()

    for edge in graph:
        from_node = edge[0]
        to_node = edge[1]
        weight = edge[2]["weight"]

        if from_node in formatted_graph:
            formatted_graph[from_node][to_node] = weight
        else:
            formatted_graph[from_node] = {to_node: weight}

    return formatted_graph


def main():
    formatted_graph = format_graph(graph)
    start_node = "Bob's House"
    distances: dict = dijkstra(formatted_graph, start_node)

    print(f"Distances from {start_node} to nodes\n")
    print(f"| {'To node':^16} | {'Distance':^16} |")
    print(f"| {'-'*16} | {'-'*16} |")

    for node in distances.keys():
        print(f"| {node:^16} | {distances[node]:^16} |")


if __name__ == "__main__":
    main()

# {
#     "Bob's House": {"Town Hall": 6},
#     "Alice's House": {"Cabin": 7},
#     "Cabin": {"Marketplace": 9},
#     "Post Office": {"Alice's House": 5, "Bob's House": 9},
#     "Town Hall": {"Marketplace": 8},
#     "Daria's House": {"Town Hall": 14},
#     "Ernie's House": {"Daria's House": 5, "Farm": 12},
#     "Grete's House": {"Ernie's House": 6},
#     "Farm": {"Grete's House": 12},
#     "Shop": {"Grete's House": 7, "Town Hall": 7},
#     "Marketplace": {"Post Office": 15, "Shop": 4},
# }
