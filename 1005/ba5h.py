import numpy as np
from numpy import unravel_index

def fitting_alignment(seq1, seq2, n, m, sigma):

    # Initialize zero matrix
    path_grid = np.zeros((n+1, m+1), dtype=object)
    path_grid[0, 0] = 'none'

    # Fill row and column
    for i in range(n):
        path_grid[i+1, 0] = 'down '
    for j in range(m):  
        path_grid[0, j+1] = 'right'

    grid = np.zeros((n+1, m+1), dtype=int)

    for i in range(n):
        for j in range(m):
            seq1_base = seq1[i]
            seq2_base = seq2[j]
            if seq1_base == seq2_base:
                # Matches are +1
                x = grid[i, j+1] - sigma
                y = grid[i+1, j] - sigma
                z = grid[i, j] + 1
                maxyz = max(x, y, z)
                if maxyz == x:
                    path_grid[i+1, j+1] = 'down '
                elif maxyz == y:
                    path_grid[i+1, j+1] = 'right'
                elif maxyz == z:
                    path_grid[i+1, j+1] = 'diag '
            else:
                # Mismatches and indels are -1
                x = grid[i, j+1] - sigma
                y = grid[i+1, j] - sigma
                z = grid[i, j] - 1
                maxyz = max(x, y, z)
                if maxyz == x:
                    path_grid[i+1, j+1] = 'down '
                elif maxyz == y:
                    path_grid[i+1, j+1] = 'right'
                elif maxyz == z:
                    path_grid[i+1, j+1] = 'diag '
            grid[i+1, j+1] = maxyz
    
    # Get the position of the highest scoring cell in the matrix and the high score
    # The max_score should always happen at the end alignment of the shorter sequence
    row_list = []
    for column in range(n):
        row_list.append(grid[column, m])
    max_score = max(row_list)

    # Get the starting point as the first max_score index which is larger than length of seq2
    for k in range(m, n):
        if row_list[k] == max_score:
             i = k
             break

    # Get the index of the max_score
    seq1 = seq1[:i]
    seq2 = seq2[:m]

    # Longest path
    p = len(seq1)
    q = len(seq2)
    longest_path_seq1 = []
    longest_path_seq2 = []

    while p * q != 0:
        direction = path_grid[p, q]
        if direction == 'down ':
            p -= 1
            longest_path_seq1.append(seq1[p])
            longest_path_seq2.append('-')
        elif direction == 'right':
            q -= 1
            longest_path_seq1.append('-')
            longest_path_seq2.append(seq2[q])
        elif direction == 'diag ':
            p -= 1
            q -= 1
            longest_path_seq1.append(seq1[p])
            longest_path_seq2.append(seq2[q])
        else:
            break

    # Finalize common subsequence
    longest_path_seq1.reverse()
    longest_path_seq2.reverse()
    aligned_sequence1 = ''.join(longest_path_seq1)
    aligned_sequence2 = ''.join(longest_path_seq2)

    return max_score, aligned_sequence1, aligned_sequence2


if __name__ == '__main__':
    with open('rosalind_ba5h.txt', 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()

        n = len(seq1)
        m = len(seq2)
        sigma = 1

        print(fitting_alignment(seq1, seq2, n, m, sigma)[0])
        print(fitting_alignment(seq1, seq2, n, m, sigma)[1])
        print(fitting_alignment(seq1, seq2, n, m, sigma)[2])