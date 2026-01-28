#dijkstra's shortest path algorithm
import heapq
def dijkstra(graph, start):
    # Create a priority queue
    priority_queue = []
    # Initialize distances with infinity
    distances = {node: float('infinity') for node in graph}
    # Set the distance to the start node to zero
    distances[start] = 0
    # Push the start node onto the priority queue
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the popped distance is greater than the recorded distance, skip processing
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Shortest distances from node {start_node}:")
for node, distance in distances.items():
    print(f"Distance to {node}: {distance}")