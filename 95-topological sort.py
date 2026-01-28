#topological sort of a graph
def topological_sort(graph):
    in_degree = {u: 0 for u in graph}  # Initialize in-degrees of all vertices

    # Calculate in-degrees
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Collect all vertices with in-degree 0
    zero_in_degree = [u for u in graph if in_degree[u] == 0]
    topo_order = []

    while zero_in_degree:
        u = zero_in_degree.pop()
        topo_order.append(u)

        # Decrease the in-degree of neighbors
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                zero_in_degree.append(v)

    if len(topo_order) == len(graph):
        return topo_order
    else:
        raise ValueError("Graph has at least one cycle, topological sort not possible.")

# Example usage
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

try:
    order = topological_sort(graph)
    print("Topological order:", order)
except ValueError as e:
    print(e)