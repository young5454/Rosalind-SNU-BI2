import numpy as np
from operator import add

# blosum62 as a nested dictionary data structure
blosum62 = {
    'A': {'A': 4,  'C': 0,  'D': -2, 'E': -1, 'F': -2, 'G': 0,  'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': -2, 'P': -1, 'Q': -1, 'R': -1, 'S': 1,  'T': 0,  'V': 0,  'W': -3, 'Y': -2},
    'C': {'A': 0,  'C': 9,  'D': -3, 'E': -4, 'F': -2, 'G': -3, 'H': -3, 'I': -1, 'K': -3, 'L': -1, 'M': -1, 'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -1, 'T': -1, 'V': -1, 'W': -2, 'Y': -2},
    'D': {'A': -2, 'C': -3, 'D': 6,  'E': 2,  'F': -3, 'G': -1, 'H': -1, 'I': -3, 'K': -1, 'L': -4, 'M': -3, 'N': 1,  'P': -1, 'Q': 0,  'R': -2, 'S': 0,  'T': -1, 'V': -3, 'W': -4, 'Y': -3},
    'E': {'A': -1, 'C': -4, 'D': 2,  'E': 5,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 1,  'L': -3, 'M': -2, 'N': 0,  'P': -1, 'Q': 2,  'R': 0,  'S': 0,  'T': -1, 'V': -2, 'W': -3, 'Y': -2},
    'F': {'A': -2, 'C': -2, 'D': -3, 'E': -3, 'F': 6,  'G': -3, 'H': -1, 'I': 0,  'K': -3, 'L': 0,  'M': 0,  'N': -3, 'P': -4, 'Q': -3, 'R': -3, 'S': -2, 'T': -2, 'V': -1, 'W': 1,  'Y': 3},
    'G': {'A': 0,  'C': -3, 'D': -1, 'E': -2, 'F': -3, 'G': 6,  'H': -2, 'I': -4, 'K': -2, 'L': -4, 'M': -3, 'N': 0,  'P': -2, 'Q': -2, 'R': -2, 'S': 0,  'T': -2, 'V': -3, 'W': -2, 'Y': -3},
    'H': {'A': -2, 'C': -3, 'D': -1, 'E': 0,  'F': -1, 'G': -2, 'H': 8,  'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': 1,  'P': -2, 'Q': 0,  'R': 0,  'S': -1, 'T': -2, 'V': -3, 'W': -2, 'Y': 2},
    'I': {'A': -1, 'C': -1, 'D': -3, 'E': -3, 'F': 0,  'G': -4, 'H': -3, 'I': 4,  'K': -3, 'L': 2,  'M': 1,  'N': -3, 'P': -3, 'Q': -3, 'R': -3, 'S': -2, 'T': -1, 'V': 3,  'W': -3, 'Y': -1},
    'K': {'A': -1, 'C': -3, 'D': -1, 'E': 1,  'F': -3, 'G': -2, 'H': -1, 'I': -3, 'K': 5,  'L': -2, 'M': -1, 'N': 0,  'P': -1, 'Q': 1,  'R': 2,  'S': 0,  'T': -1, 'V': -2, 'W': -3, 'Y': -2},
    'L': {'A': -1, 'C': -1, 'D': -4, 'E': -3, 'F': 0,  'G': -4, 'H': -3, 'I': 2,  'K': -2, 'L': 4,  'M': 2,  'N': -3, 'P': -3, 'Q': -2, 'R': -2, 'S': -2, 'T': -1, 'V': 1,  'W': -2, 'Y': -1},
    'M': {'A': -1, 'C': -1, 'D': -3, 'E': -2, 'F': 0,  'G': -3, 'H': -2, 'I': 1,  'K': -1, 'L': 2,  'M': 5,  'N': -2, 'P': -2, 'Q': 0,  'R': -1,  'S': -1, 'T': -1, 'V': 1,  'W': -1, 'Y': -1},
    'N': {'A': -2, 'C': -3, 'D': 1,  'E': 0,  'F': -3, 'G': 0,  'H': 1,  'I': -3, 'K': 0,  'L': -3, 'M': -2, 'N': 6,  'P': -2, 'Q': 0,  'R': 0,  'S': 1,  'T': 0,  'V': -3, 'W': -4, 'Y': -2},
    'P': {'A': -1, 'C': -3, 'D': -1, 'E': -1, 'F': -4, 'G': -2, 'H': -2, 'I': -3, 'K': -1, 'L': -3, 'M': -2, 'N': -2, 'P': 7,  'Q': -1, 'R': -2, 'S': -1, 'T': -1, 'V': -2, 'W': -4, 'Y': -3},
    'Q': {'A': -1, 'C': -3, 'D': 0,  'E': 2,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 1,  'L': -2, 'M': 0,  'N': 0,  'P': -1, 'Q': 5,  'R': 1,  'S': 0,  'T': -1, 'V': -2, 'W': -2, 'Y': -1},
    'R': {'A': -1, 'C': -3, 'D': -2, 'E': 0,  'F': -3, 'G': -2, 'H': 0,  'I': -3, 'K': 2,  'L': -2, 'M': -1,  'N': 0,  'P': -2, 'Q': 1,  'R': 5,  'S': -1, 'T': -1, 'V': -3, 'W': -3, 'Y': -2},
    'S': {'A': 1,  'C': -1, 'D': 0,  'E': 0,  'F': -2, 'G': 0,  'H': -1, 'I': -2, 'K': 0,  'L': -2, 'M': -1, 'N': 1,  'P': -1, 'Q': 0,  'R': -1, 'S': 4,  'T': 1,  'V': -2, 'W': -3, 'Y': -2},
    'T': {'A': 0,  'C': -1, 'D': -1, 'E': -1, 'F': -2, 'G': -2, 'H': -2, 'I': -1, 'K': -1, 'L': -1, 'M': -1, 'N': 0,  'P': -1, 'Q': -1, 'R': -1, 'S': 1,  'T': 5,  'V': 0,  'W': -2, 'Y': -2},
    'V': {'A': 0,  'C': -1, 'D': -3, 'E': -2, 'F': -1, 'G': -3, 'H': -3, 'I': 3,  'K': -2, 'L': 1,  'M': 1,  'N': -3, 'P': -2, 'Q': -2, 'R': -3, 'S': -2, 'T': 0,  'V': 4,  'W': -3, 'Y': -1},
    'W': {'A': -3, 'C': -2, 'D': -4, 'E': -3, 'F': 1,  'G': -2, 'H': -2, 'I': -3, 'K': -3, 'L': -2, 'M': -1, 'N': -4, 'P': -4, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': -3, 'W': 11, 'Y': 2},
    'Y': {'A': -2, 'C': -2, 'D': -3, 'E': -2, 'F': 3,  'G': -3, 'H': 2,  'I': -1, 'K': -2, 'L': -1, 'M': -1, 'N': -2, 'P': -3, 'Q': -1, 'R': -2, 'S': -2, 'T': -2, 'V': -1, 'W': 2,  'Y': 7}
}


def middle_column_score(seq1, seq2, n, m, sigma):

    # Initialize the score columns.
    two_column = np.zeros((n+1, 2), dtype=int)
    two_column[0, 1] = -sigma
    path_grid = ['none'] * (n+1)

    # Fill column with increasing sigma
    for i in range(n):
        two_column[i+1, 0] = -(i+1) * sigma

    middle_node = int(m / 2 + 1)
    # print(middle_node)
    for j in range(1, middle_node):
        for i in range(n+1):
            if i == 0:
                two_column[i, 1] = -j * sigma
            else:
                seq1_base = seq1[i-1]
                seq2_base = seq2[j-1]
                score_x = two_column[i-1, 1] - sigma
                score_y = two_column[i, 0] - sigma
                score_z = two_column[i-1, 0] + blosum62[seq1_base][seq2_base]
                maxyz = max(score_x, score_y, score_z)

                two_column[i, 1] = maxyz

                if maxyz == score_x:
                    path_grid[i] = 'down '
                elif maxyz == score_y:
                    path_grid[i] = 'right'
                else:
                    path_grid[i] = 'diag'
        
        # Duplicate previous column if not the last column
        if j != m / 2:
            tmp = two_column[:, 1]
            two_column = np.column_stack((tmp, tmp))
        
    middle_column = two_column[:, 1]

    return middle_column, path_grid

def middle_column_odd(seq1, seq2, n, m, sigma):

    # Initialize the score columns.
    two_column = np.zeros((n+1, 2), dtype=int)
    two_column[0, 1] = -sigma
    path_grid = ['none'] * (n+1)

    # Fill column with increasing sigma
    for i in range(n):
        two_column[i+1, 0] = -(i+1) * sigma

    middle_node = int(m / 2 + 1)
    # print(middle_node)
    for j in range(1, middle_node+1):
        for i in range(n+1):
            if i == 0:
                two_column[i, 1] = -j * sigma
            else:
                seq1_base = seq1[i-1]
                seq2_base = seq2[j-1]
                score_x = two_column[i-1, 1] - sigma
                score_y = two_column[i, 0] - sigma
                score_z = two_column[i-1, 0] + blosum62[seq1_base][seq2_base]
                maxyz = max(score_x, score_y, score_z)

                two_column[i, 1] = maxyz

                if maxyz == score_x:
                    path_grid[i] = 'down '
                elif maxyz == score_y:
                    path_grid[i] = 'right'
                else:
                    path_grid[i] = 'diag'
        
        # Duplicate previous column if not the last column
        if j != m / 2:
            tmp = two_column[:, 1]
            two_column = np.column_stack((tmp, tmp))
        
    middle_column = two_column[:, 1]

    return middle_column, path_grid


def get_middle(seq1, seq2, n, m, sigma):

    middle_column, from_source = middle_column_score(seq1, seq2, n, m, sigma)
    middle_column = list(middle_column)

    seq1_reverse = seq1[::-1]
    seq2_reverse = seq2[::-1]

    if m % 2 == 0:
        reverse_middle_column, to_sink = middle_column_score(seq1_reverse, seq2_reverse, n, m, sigma)
        reverse_middle_column = list(reverse_middle_column)
    else:
        reverse_middle_column, to_sink = middle_column_odd(seq1_reverse, seq2_reverse, n, m, sigma)
        reverse_middle_column = list(reverse_middle_column)

    # Reverse to_sink paths
    reverse_middle_column.reverse()
    to_sink.reverse()

    # Find maximum score and its index
    re = list(map(add, middle_column, reverse_middle_column))
    max_re = max(re)
    max_index = re.index(max_re)
    half = m // 2
    direction = to_sink[max_index]

    if direction == 'down ':
        coordinates = ((max_index, half), (max_index+1, half))
    elif direction == 'right':
        coordinates = ((max_index, half), (max_index, half+1))
    else:
        coordinates = ((max_index, half), (max_index+1, half+1))
        
    return coordinates

def global_alignment(seq1, seq2, n, m, sigma):

    # Initialize zero matrix
    path_grid = np.zeros((n+1, m+1), dtype=object)
    path_grid[0, 0] = 'none'

    # Fill row and column
    for i in range(n):
        path_grid[i+1, 0] = 'down '
    for j in range(m):  
        path_grid[0, j+1] = 'right'

    grid = np.zeros((n+1, m+1), dtype=int)

    # Fill 
    # Fill row and column
    for i in range(n):
        grid[i+1, 0] = -(i+1) * sigma
    for j in range(m):
        grid[0, j+1] = -(j+1) * sigma

    for i in range(n):
        for j in range(m):
            seq1_base = seq1[i]
            seq2_base = seq2[j]
            penalty = blosum62[seq1_base][seq2_base]

            x = grid[i, j+1] - sigma
            y = grid[i+1, j] - sigma
            z = grid[i, j] + penalty
            maxyz = max(x, y, z)
            if maxyz == x:
                path_grid[i+1, j+1] = 'down '
            elif maxyz == y:
                path_grid[i+1, j+1] = 'right'
            else:
                path_grid[i+1, j+1] = 'diag '
            grid[i+1, j+1] = maxyz


    # Longest path
    p = n
    q = m
    dir_list = []
    coord_list = []
    while p >= 0 and q >= 0:
        direction = path_grid[p, q]
        if direction == 'down ':
            p -= 1
            dir_list.append(direction)
            coord_list.append((p, q))
        elif direction == 'right':
            q -= 1
            dir_list.append(direction)
            coord_list.append((p, q))
        elif direction == 'diag ':
            p -= 1
            q -= 1
            dir_list.append(direction)
            coord_list.append((p, q))
        else:
            break

    # Finalize common subsequence
    max_score = grid[n, m]
    dir_list.reverse()
    coord_list.reverse()

    return max_score, dir_list, coord_list, path_grid, grid


if __name__ == '__main__':
    with open('rosalind_ba5k.txt', 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()

        n = len(seq1)
        m = len(seq2)

        sigma = 5

        print(get_middle(seq1, seq2, n, m, sigma))