from collections import deque

def topological_sort(graph_dic, indegree_dic, all_node_set):
    sorted = []
    q = deque()

    for node in all_node_set:
        if indegree_dic[node] == 0:
            q.append(node)

    while q:
        curr = q.popleft()
        sorted.append(curr)
        for node in graph_dic[curr]:
            indegree_dic[node] -= 1
            if indegree_dic[node] == 0:
                q.append(node)

    return sorted

if __name__ == '__main__':
    with open("rosalind_ba5n.txt") as file:
        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
        
        all_nodes = []
        for entry in data_list:
            first, _ = entry.split(' -> ')
            second = _.split(',')
            first = int(first)
            all_nodes.append(first)
            for s in second:
                s = int(s)
                all_nodes.append(s)

        all_nodes_set = set(all_nodes)

        node_num = len(all_nodes_set)

        graph_dic = {}
        indegree_dic = {}

        for node in all_nodes_set:
            graph_dic[node] = []
            indegree_dic[node] = 0

        for entry in data_list:
            first, _ = entry.split(' -> ')
            first = int(first)
            second = _.split(',')
            for s in second:
                s = int(s)
                graph_dic[first].append(s)
                indegree_dic[s] += 1

        print(topological_sort(graph_dic, indegree_dic, all_nodes_set))
        