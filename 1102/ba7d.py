import numpy as np

# UPGMA(D, n)
#  Clusters ← n single-element clusters labeled 1, ... , n
#  construct a graph T with n isolated nodes labeled by single elements 1, ... , n
#  for every node v in T 
#   Age(v) ← 0
#  while there is more than one cluster 
#   find the two closest clusters Ci and Cj  
#   merge Ci and Cj into a new cluster Cnew with |Ci| + |Cj| elements
#   add a new node labeled by cluster Cnew to T
#   connect node Cnew to Ci and Cj by directed edges 
#   remove the rows and columns of D corresponding to Ci and Cj 
#   remove Ci and Cj from Clusters 
#   add a row/column to D for Cnew by computing D(Cnew, C) for each C in Clusters
#   add Cnew to Clusters 
#  root ← the node in T corresponding to the remaining cluster
#  for each edge (v, w) in T
#   length of (v, w) ← Age(v) - Age(w)
#  return T

def calculate_distance(cluster1, cluster2, distance_matrix):
    # Assume cluster is [[node1, node2, .. nodeN], num] data type
    c1 = cluster1[1]
    c2 = cluster2[1]

    total = 0
    # a and b are indices
    for a in cluster1[0]:
        for b in cluster2[0]:
            total += distance_matrix[a, b] 
    
    return total / (c1 * c2)


def upgma(n, distance_matrix, original_distance_matrix):
    # Initial clusters: [[index], num_of_nodes, weight, node_id]
    clusters = [[[i], 1, 0, i] for i in range(n)]

    # Initate final result string (tree)
    result = ''
    result2 = ''
    
    counter = n-1
    while len(clusters) > 1:
        # Find minimum item and index
        min_index = np.unravel_index(np.argmin(distance_matrix), distance_matrix.shape)
        min_i, min_j = min_index

        # Always min_i < min_j
        if min_i > min_j:
            tmp = min_i
            min_i = min_j
            min_j = tmp

        min_i_cluster = clusters[min_i]
        min_j_cluster = clusters[min_j]

        # print(min_i_cluster)
        # print(min_j_cluster)

        # Update weights
        curr_weight = distance_matrix[min_i, min_j] / 2

        # Make merged cluster c_new and append to cluster
        current_nodes = min_i_cluster[0]
        num_nodes = min_i_cluster[1]
        current_nodes.extend(min_j_cluster[0])
        num_nodes += min_j_cluster[1]

        # Counter as new node
        counter += 1
        c_new = [current_nodes, num_nodes, curr_weight, counter]
        clusters.append(c_new)

        weight_diff_i = "{:.3f}".format(c_new[2] - min_i_cluster[2])
        weight_diff_j = "{:.3f}".format(c_new[2] - min_j_cluster[2])

        checkpoints1 = str(c_new[3]) + '->' + str(min_i_cluster[3]) + ':' + str(weight_diff_i)
        checkpoints2 = str(c_new[3]) + '->' + str(min_j_cluster[3]) + ':' + str(weight_diff_j)

        # Reverse
        checkpoints3 = str(min_i_cluster[3]) + '->' + str(c_new[3]) + ':' + str(weight_diff_i)
        checkpoints4 = str(min_j_cluster[3]) + '->' + str(c_new[3]) + ':' + str(weight_diff_j)

        result2 += checkpoints1 + '\n'
        result2 += checkpoints2 + '\n'
        result2 += checkpoints3 + '\n'
        result2 += checkpoints4 + '\n'

        # # Update tree for currently merged cluster
        # checkpoints = ' '.join(str(x+1) for x in current_nodes)
        # result += checkpoints + '\n'

        # Remove Ci and Cj from clusters
        clusters.remove(min_i_cluster)
        clusters.remove(min_j_cluster)

        # Calculate average distance
        new_column = []
        for cluster in clusters:
            if cluster != c_new:
                avg_distance = calculate_distance(cluster, c_new, original_distance_matrix)
                new_column.append(avg_distance)
        new_column = np.array(new_column)

        # Delete row, columns and append the new_column
        distance_matrix = np.delete(distance_matrix, [min_i, min_j], axis=1)
        distance_matrix = np.delete(distance_matrix, [min_i, min_j], axis=0)
        # Append the new column and row
        distance_matrix = np.concatenate((distance_matrix, new_column[:, np.newaxis]), axis=1)

        new_column_with_inf = np.append(new_column, np.inf)
        distance_matrix = np.concatenate((distance_matrix, new_column_with_inf[np.newaxis, :]), axis=0)

    return result2


if __name__ == '__main__':
    with open("rosalind_ba7d.txt") as file:
        # n
        n = file.readline()
        n = int(n)

        # Initiate n x n matrix
        data_list = []
        distance_matrix = np.zeros((n, n))
        distance_dic = {}

        for line in file:
            cleaned_line = line.strip()
            data_point = cleaned_line.split()
            float_data = [int(data) for data in data_point]
            data_list.append(float_data)
        
        for i in range(n):
            distance_matrix[i, :] = np.array(data_list[i])
        
        # Change diagonal 0 -> inf
        for i in range(n):
            distance_matrix[i, i] = np.inf

        print(upgma(n, distance_matrix, distance_matrix))