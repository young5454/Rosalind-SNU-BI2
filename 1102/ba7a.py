import heapq

def get_nodes_weights(string):
    # Function to split data format

    get_node = string.split(sep='->')
    get_weight = get_node[1].split(sep=':')

    start_node = get_node[0]
    end_node = get_weight[0]
    weight = get_weight[1]

    return start_node, end_node, weight


def dijkstra(graph, start):
    # Implement dijkstra algorithm to find path distance

    # Initialize with inf
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Initialize a priority queue: (distance, node) format
    min_heap = [(0, start)]

    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)
        if current_dist > distances[current_node]:
            continue

        # Find current neighbors and distances
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


def dijkstra_with_path(graph, start, end):
    # Implement dijkstra algorithm to find path info

    # Initialize with inf
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    min_heap = [(0, start)]
    previous = {node: None for node in graph}

    # Initialize a priority queue: (distance, node) format
    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)
        if current_node == end:
            break

        if current_dist > distances[current_node]:
            continue

        # Find current neighbors and distances
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))

    # Save path info
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]

    if path[0] == start:
        return path
    else:
        return []


def leaf_distances(graph_dic, n):
    leaf_nodes = [node for node in graph_dic if int(node) < n]
    print(leaf_nodes)
    num_leaf_nodes = len(leaf_nodes)
    distance_matrix = [[0] * num_leaf_nodes for _ in range(num_leaf_nodes)]

    for i in range(num_leaf_nodes):
        for j in range(i, num_leaf_nodes):
            if i == j:
                distance_matrix[i][j] = 0
            else:
                distances = dijkstra(graph_dic, leaf_nodes[i])
                distance_matrix[i][j] = distances[leaf_nodes[j]]
                # Symmetric
                distance_matrix[j][i] = distance_matrix[i][j]

    return distance_matrix


if __name__ == '__main__':
    with open("rosalind_ba7a.txt") as file:
        # n-number of data points
        # m-dimensional space
        n = file.readline()
        n = int(n)

        data_list = []
        for line in file.readlines():
            data_list.append(line.strip('\n'))
        
        # Save data into graph
        new_data = []
        for d in data_list:
            three_list = get_nodes_weights(d)
            new_data.append(three_list)

        graphy = {}
        for new in new_data:
            start = new[0]
            end = new[1]
            weight = int(new[2])
            if start in graphy:
                curr = graphy[start]
                curr[end] = weight
            else:
                curr = {end: weight}
                graphy[start] = curr
        
        # Print final matrix
        result = leaf_distances(graphy, n)
        for row in result:
            print(' '.join(str(i) for i in row))

        start_node = '0'
        end_node = '1'
        path = dijkstra_with_path(graphy, start_node, end_node)
        print(path)

