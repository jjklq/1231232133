from collections import deque

def shortest_route(subway_system, start, end):
    if start not in subway_system or end not in subway_system:
        return None
    
    visited = set()
    queue = deque([(start, [])])

    while queue:
        station, path = queue.popleft()
        if station == end:
            return path + [station]
        visited.add(station)
        for neighbor in subway_system[station]:
            if neighbor not in visited:
                queue.append((neighbor, path + [station]))


subway_system = {
    'Station A': {'Station B'},
    'Station B': {'Station A', 'Station C', 'Station D'},
    'Station C': {'Station B', 'Station D', 'Station E'},
    'Station D': {'Station B', 'Station C', 'Station E', 'Station F'},
    'Station E': {'Station C', 'Station D', 'Station F'},
    'Station F': {'Station D', 'Station E'}
}

start_station = 'Station A'
end_station = 'Station F'

shortest_path = shortest_route(subway_system, start_station, end_station)
if shortest_path:
    print("Shortest Route:", shortest_path)
else:
    print("route not found.")
