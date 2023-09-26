import numpy as np
import sys
from collections import deque

def topological_sort(in_graph_dic, out_graph_dic, source, sink):

    # Count number of incoming nodes for each node. Source node = 0
    indegree = {source: 0}
    for node in in_graph_dic.keys():
        incoming = in_graph_dic[node]
        incoming_nodes_num = len(incoming.keys())
        indegree[node] = incoming_nodes_num
    
    print(indegree)

    # Initialize queue with source node
    q = deque()
    q.append(source)
    result = []

    # 
    while q:
        now = q.popleft()
        result.append(now)
        for g in out_graph_dic[now].values():
            if g != sink:
                indegree[g] -= 1
                if indegree[g] == 0:
                    q.append(g)
    result.append(sink)
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

        # In-graph: key = node, value = incoming nodes with weights
        # In-graph does not have source node
        in_graph_dic = {}
        for entry in data_list[2:]:
            first , _ = entry.split('->')
            second, weight = _.split(':')
            weight = int(weight)
            if second in in_graph_dic.keys():
                curr = in_graph_dic[second]
                curr[weight] = first
            else:
                in_graph_dic[second] = {weight: first}
        # Out-graph: key = node, value = outgoing nodes with weights
        # Out-graph does not have sink node
        out_graph_dic = {}
        for entry in data_list[2:]:
            first , _ = entry.split('->')
            second, weight = _.split(':')
            weight = int(weight)
            if first in out_graph_dic.keys():
                curr = out_graph_dic[first]
                curr[weight] = second
            else:
                out_graph_dic[first] = {weight: second}

    # print(in_graph_dic)
    # print(out_graph_dic)
    print(topological_sort(in_graph_dic, out_graph_dic, source, sink))
    print(longest_path_in_dag(in_graph_dic, out_graph_dic, source, sink)[0])
    print(longest_path_in_dag(in_graph_dic, out_graph_dic, source, sink)[1])
    print(longest_path_in_dag(in_graph_dic, out_graph_dic, source, sink)[2])



