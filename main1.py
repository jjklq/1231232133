def jaccard_similarity(set1, set2):
    if len(set1) == 0 or len(set2) == 0:
        return 0.0
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return float(intersection) / union

def bus_timing(bus_stop, minutes):
    if bust_stop in a3_bus:
        for time in a3_bus[bus_stop]:
            if time >= minutes:
                return time - minutes
    return -1

    def common_courses(studen1, student2):
        if student in student_courses and student in student_courses:
            courses1 = student_courses[student1]
            courses2 = student_courses[student2]
            common_courses = list(courses.intersection(course2))
            return common_courses
        return[]


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

print(shortest_route(subway_system, 'Station A', 'Station F'))
