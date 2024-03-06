from collections import deque


def bfs_find_name(graph, start_node):
    queue = deque()
    visited = set()
    found = False

    queue.append(start_node)
    visited.add(start_node)

    while queue and not found:
        node = queue.popleft()
        names = graph.get(node)

        if names:
            for name in names:
                if len(name) > 1 and name[5] == 'e':
                    print(name + " found in key: " + node)
                    found = True
                    break

        neighbors = graph.get(node)
        if neighbors:
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


bfs_search_hash_map = {
    "Me": ["Claire", "Alice", "Bob"],
    "Claire": ["Johny", "Tom"],
    "Alice": ["Peggi"],
    "Bob": ["Peggi", "Anuj"]
}

bfs_find_name(bfs_search_hash_map, "Me")
