import networkx as nx
import matplotlib.pyplot as plt


graph = [
    ("Bob's House", "Town Hall", {"weight": 6}),
    ("Alice's House", "Cabin", {"weight": 7}),
    ("Cabin", "Marketplace", {"weight": 9}),
    ("Post Office", "Alice's House", {"weight": 5}),
    ("Town Hall", "Marketplace", {"weight": 8}),
    ("Daria's House", "Town Hall", {"weight": 14}),
    ("Ernie's House", "Daria's House", {"weight": 5}),
    ("Ernie's House", "Farm", {"weight": 12}),
    ("Grete's House", "Ernie's House", {"weight": 6}),
    ("Farm", "Grete's House", {"weight": 12}),
    ("Shop", "Grete's House", {"weight": 7}),
    ("Shop", "Town Hall", {"weight": 7}),
    ("Post Office", "Bob's House", {"weight": 9}),
    ("Marketplace", "Post Office", {"weight": 15}),
    ("Marketplace", "Shop", {"weight": 4}),
]

positions = {
    "Alice's House": (0, 0),
    "Bob's House": (0, 20),
    "Cabin": (10, 0),
    "Post Office": (0, 10),
    "Town Hall": (10, 20),
    "Daria's House": (0, 30),
    "Ernie's House": (10, 30),
    "Grete's House": (20, 20),
    "Farm": (20, 30),
    "Shop": (20, 10),
    "Marketplace": (10, 10),
}


def draw_graph():
    DG = nx.DiGraph(graph)

    nx.draw(
        DG,
        positions,
        with_labels=True,
        node_color="lightpink",
        node_size=3400,
        font_size=8,
    )
    nx.draw_networkx_edge_labels(
        DG,
        positions,
        edge_labels=nx.get_edge_attributes(DG, "weight"),
    )

    plt.title("The village of Meadowfield")
    plt.show()


if __name__ == "__main__":
    draw_graph()
