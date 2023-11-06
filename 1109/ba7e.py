import numpy as np

# NeighborJoining(D,n)
#  if n = 2
#   T ← tree consisting of a single edge of length D1,2
#   return T
#  D' ← neighbor-joining matrix constructed from the distance matrix D
#  find elements i and j such that D'i,j is a minimum non-diagonal element of D'
#  Δ ← (TotalDistanceD(i) - TotalDistanceD(j)) /(n - 2)
#  limbLengthi ← (1/2)(Di,j + Δ)
#  limbLengthj ← (1/2)(Di,j - Δ)
#  add a new row/column m to D so that Dk,m = Dm,k = (1/2)(Dk,i + Dk,j - Di,j) for any k
#  remove rows i and j from D
#  remove columns i and j from D
#  T ← NeighborJoining(D, n - 1)
#  add two new limbs (connecting node m with leaves i and j) to the tree T
#  assign length limbLengthi to Limb(i)
#  assign length limbLengthj to Limb(j)
#  return T

def calculate_total_distance(matrix, i):
    # Calculate the row, column sum of index i
    row_i = matrix[i]

    return sum(row_i)


def neighbor_joining_matrix(matrix):
    n = len(matrix)
    nj_matrix = np.zeros(shape=(n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                nj_matrix[i, j] =  0
            else:
                new_entry = (n - 2) * matrix[i, j] \
                            - calculate_total_distance(matrix, i) \
                            - calculate_total_distance(matrix, j)
                nj_matrix[i, j] = new_entry

    return nj_matrix            


def get_delta(matrix, i, j):
    n = len(matrix)
    delta = (calculate_total_distance(matrix, i) \
             - calculate_total_distance(matrix, j)) / (n - 2)

    return delta


def neighbor_joining(matrix, n):
    # Define final tree: elements = number of nodes in initial distance matrix
    tree_dic = {k : [] for k in range(n)}
    nodes = list(tree_dic.keys())

    if len(matrix) == 1:
        return tree_dic
    
    while len(matrix) > 2:
        nj_matrix = neighbor_joining_matrix(matrix)
        n_nj = len(nj_matrix)

        # Get minimum entry from nj matrix
        min_entry = np.argmin(nj_matrix)
        i = min_entry // n_nj
        j = min_entry % n_nj

        #  Δ ← (TotalDistanceD(i) - TotalDistanceD(j)) /(n - 2)
        delta = get_delta(matrix, i, j)
        limb_i = (matrix[i, j] + delta) / 2
        limb_j = (matrix[i, j] - delta) / 2

        # New row/column m to D so that Dk,m = Dm,k = (1/2)(Dk,i + Dk,j - Di,j) for any k
        new_row = (matrix[i, :] + matrix[j, :] - matrix[i, j]) / 2
        matrix = np.insert(matrix, n, new_row, axis=0)

        new_column = np.insert(new_row, n, 0, axis=0)
        matrix = np.insert(matrix, n, new_column, axis=1)

        # D ← D with rows and columns i and j removed
        matrix = np.delete(matrix, [i, j], 0)
        matrix = np.delete(matrix, [i, j], 1)

        # New node 
        new_label = len(tree_dic.keys())
        tree_dic[new_label] = []

        # Connection info
        tree_dic[new_label].append([nodes[i], limb_i])
        tree_dic[nodes[i]].append([new_label, limb_i])

        tree_dic[new_label].append([nodes[j], limb_j])
        tree_dic[nodes[j]].append([new_label, limb_j])

        # Remove clustered nodes from node_indices
        if i < j:
            nodes.remove(nodes[j])
            nodes.remove(nodes[i])
        else:
            nodes.remove(nodes[i])
            nodes.remove(nodes[j])

        nodes.append(new_label)

        # Reduce n by 1
        n -= 1

    if len(matrix) == 2:
        # connect two remaining nodes to each other
        tree_dic[len(tree_dic) - 1].append([len(tree_dic) - 2, matrix[0, 1]])
        tree_dic[len(tree_dic) - 2].append([len(tree_dic) - 1, matrix[0, 1]])

    return tree_dic


if __name__ == '__main__':
    with open("rosalind_ba7e.txt") as file:
        # n-number of data points
        # m-dimensional space
        n = file.readline()
        n = int(n)

        # Read the text file and convert it into a NumPy ndarray
        lines = file.readlines()
        matrix = np.zeros(shape=(n, n))
        data_list = [list(map(float, line.split())) for line in lines]

        # Convert the list of lsists into a NumPy ndarray
        matrix = np.array(data_list)

        # Print tree
        tree = neighbor_joining(matrix, n)

        for key, connection in tree.items():
            for info in connection:
                node = info[0]
                weight = info[1]
                print(str(key) + '->' + str(node) + ':' + str("{:.3f}".format(weight)))


        # print(matrix)
        # print(calculate_total_distance(matrix, 2))
        # print(neighbor_joining_matrix(matrix))
        # print(np.argmin(neighbor_joining_matrix(matrix)))
        # print(get_delta(matrix, 0, 1))
        # print(neighbor_joining(matrix, n))
        # print(neighbor_joining(matrix, n))

