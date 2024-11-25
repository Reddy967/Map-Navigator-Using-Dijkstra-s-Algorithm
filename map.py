import heapq

def dijkstra(graph, start, end):
    # Priority queue to store (cost, vertex) tuples
    pq = []
    heapq.heappush(pq, (0, start))
    
    # Dictionary to store the shortest path to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Dictionary to store the path taken to reach each vertex
    previous_vertices = {vertex: None for vertex in graph}
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # If we reached the target vertex, break out of the loop
        if current_vertex == end:
            break
        
        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_vertices[current]
    path.reverse()
    
    return path, distances[end]

# Example graph: Nodes are cities, edges are distances between them
graph = {
    'Hyderabad': {'Nagpur': 500, 'Bangalore': 570},
    'Nagpur': {'Hyderabad': 500, 'Delhi': 1000, 'Bhopal': 350},
    'Bangalore': {'Hyderabad': 570, 'Pune': 840},
    'Bhopal': {'Nagpur': 350, 'Delhi': 700},
    'Pune': {'Bangalore': 840, 'Delhi': 1400},
    'Delhi': {'Nagpur': 1000, 'Bhopal': 700, 'Pune': 1400}
}

# Run Dijkstra's algorithm
start_city = 'Hyderabad'
end_city = 'Delhi'
path, distance = dijkstra(graph, start_city, end_city)

print(f"Shortest path from {start_city} to {end_city}: {path}")
print(f"Total distance: {distance} km")
