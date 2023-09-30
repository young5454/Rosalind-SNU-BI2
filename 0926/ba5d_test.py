import numpy as np
from collections import deque
from collections import defaultdict

def topological_sort(no_inward_nodes, no_outward_nodes, in_graph_dic, out_graph_dic):

    # Count number of incoming nodes for each node. Source node = 0
    indegree = {}
    outdegree = {}
    for node in no_inward_nodes:
        indegree[node] = 0

    for node in in_graph_dic.keys():
        incoming = in_graph_dic[node]
        incoming_nodes_num = len(incoming.keys())
        indegree[node] = incoming_nodes_num
    
    for node in no_outward_nodes:
        outdegree[node] = 0

    for node in out_graph_dic.keys():
        outgoing = out_graph_dic[node]
        outgoing_nodes_sum = len(outgoing.keys())
        outdegree[node] = outgoing_nodes_sum

    # Initialize queue with source node
    q = deque()
    for node in no_inward_nodes:
        q.append(node)
    result = []
    # 
    while q:
        now = q.popleft()
        if outdegree[now] == 0:
            result.append(now)
        else:
            result.append(now)
            for g in out_graph_dic[now].values():
                indegree[g] -= 1
                if indegree[g] == 0:
                    q.append(g)
    
    print(indegree)
    return result

def longest_path_in_dag(in_graph_dic, out_graph_dic, source, sink):

    ordered_nodes = topological_sort(in_graph_dic, out_graph_dic, source, sink)
    ordered_nodes_without_source = ordered_nodes[1:]

    # Initialize zero graph
    griddy = {}
    for node in ordered_nodes:
        griddy[node] = 0
    
    backtrack = {}
    
    for node in ordered_nodes_without_source:
        before_nodes_data = in_graph_dic[node]
        max_weight = -float('inf')
        that_weight = 0

        # Calculate all weights for before-nodes and pick the max
        curr_weights = before_nodes_data.keys()
        for w in curr_weights:
            before_node = before_nodes_data[w] 
            curr_weight_add = griddy[before_node] + w
            if curr_weight_add > max_weight:
                max_weight = curr_weight_add
                that_weight = w
        
        # Assign largest weight sum
        griddy[node] = max_weight

        pass_node = in_graph_dic[node][that_weight]
        backtrack[node] = pass_node

    
    # Get length of the longest path
    longest_path_length = griddy[sink]
    
    # Backtrack and reverse
    path_list = [sink]
    flag = True
    while flag:
        before = backtrack[sink]
        path_list.append(before)
        sink = before
        if sink == source:
            flag = False

    path_list.reverse()
    longest_path = '->'.join(path_list)


    return griddy, longest_path_length, longest_path


if __name__ == '__main__':
    with open("rosalind_ba5d.txt") as file:
        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
        source = data_list[0]
        sink = data_list[1]

        in_graph = {}
        out_graph = {}
        all_nodes = []
        outward_nodes = []      # No outward-going nodes
        inward_nodes = []       # No inward-coming nodes

        for entry in data_list[2:]:
            first , _ = entry.split('->')
            second, weight = _.split(':')
            weight = int(weight)

            # Make all-nodes list
            all_nodes.append(first)
            all_nodes.append(second)
            outward_nodes.append(first)
            inward_nodes.append(second)

            # Make graph
            if first in out_graph.keys():
                curr = out_graph[first]
                curr[weight] = second 
            else:
                out_graph[first] = {weight:second}
            
            if second in in_graph.keys():
                curr = in_graph[second]
                curr[weight] = first
            else:
                in_graph[second] = {weight: first}

        all_nodes = set(all_nodes)
        outward_nodes = set(outward_nodes)
        inward_nodes = set(inward_nodes)

        no_outward_nodes = []
        no_inward_nodes = []
        for node in all_nodes:
            if node not in outward_nodes:
                no_outward_nodes.append(node)
            if node not in inward_nodes:
                no_inward_nodes.append(node)

        print(len(all_nodes))
        print(out_graph)
        print(in_graph)
        print(no_outward_nodes)
        print(no_inward_nodes)
        print(len(topological_sort(no_inward_nodes, no_outward_nodes, in_graph, out_graph)))

