import numpy as np

# HierarchicalClustering(D, n)
#  Clusters ← n single-element clusters labeled 1, ... , n
#  construct a graph T with n isolated nodes labeled by single elements 1, ... , n
#  while there is more than one cluster 
#   find the two closest clusters Ci and Cj 
#   merge Ci and Cj into a new cluster Cnew with |Ci| + |Cj| elements
#   add a new node labeled by cluster Cnew to T
#   connect node Cnew to Ci and Cj by directed edges
#   remove the rows and columns of D corresponding to Ci and Cj
#   remove Ci and Cj from Clusters
#   add a row/column to D for Cnew by computing D(Cnew, C) for each C in Clusters
#   add Cnew to Clusters 
#     assign root in T as a node with no incoming edges
#     return T

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


def hierarchical_clustering(n, distance_matrix, original_distance_matrix):
    # Initial clusters: [[index], num_of_nodes]
    clusters = [[[i], 1] for i in range(n)]
    result = ''
    
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

        # Make merged cluster c_new and append to cluster
        current_nodes = min_i_cluster[0]
        num_nodes = min_i_cluster[1]
        current_nodes.extend(min_j_cluster[0])

        checkpoints = ' '.join(str(x+1) for x in current_nodes)
        result += checkpoints + '\n'


        num_nodes += min_j_cluster[1]
        c_new = [current_nodes, num_nodes]
        clusters.append(c_new)

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

        # print(clusters)
        # print(distance_matrix)

    return result


if __name__ == '__main__':
    with open("rosalind_ba8e.txt") as file:
        # n
        n = file.readline()
        n = int(n)

        # Initiate n x n matrix
        data_list = []
        distance_matrix = np.zeros((n, n))
        distance_dic = {}

        for line in file:
            cleaned_line = line.strip()
            data_point = cleaned_line.split(' ')
            float_data = [float(data) for data in data_point]
            data_list.append(float_data)
        
        for i in range(n):
            distance_matrix[i, :] = np.array(data_list[i])
        
        # Change diagonal 0 -> inf
        for i in range(n):
            distance_matrix[i, i] = np.inf

        print(hierarchical_clustering(n, distance_matrix, distance_matrix))