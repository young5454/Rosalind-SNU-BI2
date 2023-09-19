import numpy as np

def longest_common_sequence(n, m, right_matrix, down_matrix, diagonal_matrix, diagonal_with_bases_matrix):

    # Initialize zero matrix
    path_grid = np.zeros((n+1, m+1), dtype=object)
    path_grid[0, 0] = 'none'

    # Fill row and column
    for i in range(n):
        path_grid[i+1, 0] = 'down'
    for j in range(m):
        path_grid[0, j+1] = 'right'

    grid = np.zeros((n+1, m+1), dtype=int)

    # Fill row and column
    for i in range(n):
        grid[i+1, 0] = grid[i, 0] + down_matrix[i, 0]
    for j in range(m):
        grid[0, j+1] = grid[0, j] + right_matrix[0, j]

    # Fill the rest
    for i in range(n):
        for j in range(m):
            x = grid[i, j+1] + down_matrix[i, j+1]
            y = grid[i+1, j] + right_matrix[i+1, j]
            z = grid[i, j] + diagonal_matrix[i, j]
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
    longest_path = []
    while p >= 0 and q >= 0:
        direction = path_grid[p, q]
        if direction == 'down ':
            p -= 1
        elif direction == 'right':
            q -= 1
        elif direction == 'diag ':
            curr = diagonal_with_bases_matrix[p-1, q-1]
            longest_path.append(curr)
            p -= 1
            q -= 1
        else:
            break

    # Finalize common subsequence
    longest_path.reverse()
    common_subsequence = ''.join(longest_path)

    return common_subsequence


if __name__ == '__main__':
    with open('rosalind_ba5c.txt', 'r') as file:
        first_seq = file.readline().strip()
        second_seq = file.readline().strip()

        n = len(first_seq)
        m = len(second_seq)

        down_matrix = np.zeros((n, m+1), dtype=int)
        right_matrix = np.zeros((n+1, m), dtype=int)
        diagonal_matrix = np.zeros((n, m), dtype=int)
        diagonal_with_bases_matrix = np.zeros((n, m), dtype=object)

        for i in range(n):
            for j in range(m):
                if first_seq[i] == second_seq[j]:
                    diagonal_matrix[i, j] = 1
                    diagonal_with_bases_matrix[i, j] = first_seq[i]
                else:
                    diagonal_matrix[i, j] = 0

        print(longest_common_sequence(n, m, right_matrix, down_matrix, diagonal_matrix, diagonal_with_bases_matrix))