import numpy as np
from ba7a import dijkstra_with_path
from ba7b import limblength

# AdditivePhylogeny(D, n)
#     if n = 2
#         return the tree consisting of a single edge of length D1,2
#     limbLength ← Limb(D, n)
#     for j ← 1 to n - 1
#         Dj,n ← Dj,n - limbLength
#         Dn,j ← Dj,n
#     (i,n,k) ← three leaves such that Di,k = Di,n + Dn,k
#     x ← Di,n
#     remove row n and column n from D
#     T ← AdditivePhylogeny(D, n - 1)
#     v ← the (potentially new) node in T at distance x from i on the path between i and k
#     add leaf n back to T by creating a limb (v, n) of length limbLength
#     return T

# This code doesn't work :(

def three_leaves(matrix, n, curr):
    # (i,n,k) ← three leaves such that Di,k = Di,n + Dn,k
    limb_length_of_curr = limblength(matrix, curr, n)

    if curr > 0:
        i = curr - 1
    else:
        i = curr + 1

    # Find k
    index = None
    for k in range(n):
        if i != k and k != curr:
            d_ic = matrix[i, curr]
            d_ik = matrix[i, k]
            d_ck = matrix[curr, k]
            this_limb = (d_ic + d_ck - d_ik) // 2
            if this_limb == limb_length_of_curr:
                index = (i, k)

    # Return i and k that satisfies the rule
    return index[0], index[1]


def additive_phylogeny(matrix, n):
    if n == 2:
        return {0: {1: matrix[0, 1]}, 1: {0: matrix[0, 1]}}
    
    # Calculate limb length for the last row (n - 1) of the matrix
    limb_length = limblength(matrix, n - 1, n)
    
    # Adjust the matrix
    for k in range(n - 1):
        matrix[k, n - 1] -= limb_length
        matrix[n - 1, k] -= limb_length

    i, k = three_leaves(matrix, n, n-1)
    print(i, k)
    
    # Calculate x value
    x = matrix[i, n - 1]
    
    # Create a trimmed matrix
    trimmed_matrix = np.delete(np.delete(matrix, n - 1, axis=0), n - 1, axis=1)
    print(trimmed_matrix)
    
    tree = additive_phylogeny(trimmed_matrix, n - 1)
    print(tree)

    # Find node and attach branch
    path = dijkstra_with_path(tree, i, k)
    print(path)

    v = None
    for node in path:
        if tree[i][node] == x:
            v = node
            break
        elif tree[i][node] > x:
            v = str(n)
            tree[v] = {node: limb_length}
            tree[node][v] = limb_length
            tree[i][node] -= x
            tree[node][i] -= x
            break
    
    return tree


if __name__ == '__main__':
    with open("rosalind_ba7c.txt") as file:
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
        
        print(additive_phylogeny(distance_matrix, n))
