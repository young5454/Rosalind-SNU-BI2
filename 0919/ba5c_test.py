import numpy as np

def longest_path_with_diagonal(n, m, right_matrix, down_matrix, diagonal_matrix):
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

    # Longest path score
    max_path_score = grid[n, m]

    # Longest path
    p = n
    q = m
    longest_path = []
    while p >= 0 and q >= 0:
        direction = path_grid[p, q]
        if direction == 'down ':
            curr = down_matrix[p-1, q]
            longest_path.append(curr)
            p -= 1
        elif direction == 'right':
            curr = right_matrix[p, q-1]
            longest_path.append(curr)
            q -= 1
        elif direction == 'diag ':
            curr = diagonal_matrix[p-1, q-1]
            longest_path.append(curr)
            p -= 1
            q -= 1
        else:
            break

    return max_path_score, grid, path_grid, longest_path

if __name__ == '__main__':
    with open('rosalind_ba5c_test.txt', 'r') as file:
        # Parse n and m
        n, m = map(int, file.readline().split())

        # Initialize matrix 1 and 2
        down_matrix = np.empty((n, m+1), dtype=int)
        right_matrix = np.empty((n+1, m), dtype=int)
        diagonal_matrix = np.empty((n, m), dtype=int)

        # First matrix
        for i in range(n):
            row = list(map(int, file.readline().split()))
            down_matrix[i, :] = row

        # Skip the '-'
        file.readline()

        # Second matrix
        for j in range(n+1):
            row = list(map(int, file.readline().split()))
            right_matrix[j, :] = row

        # Skip the '-'
        file.readline()

        # Third matrix
        for k in range(n):
            row = list(map(int, file.readline().split()))
            diagonal_matrix[k, :] = row

        print(longest_path_with_diagonal(n, m, right_matrix, down_matrix, diagonal_matrix)[0])
        print(longest_path_with_diagonal(n, m, right_matrix, down_matrix, diagonal_matrix)[1])
        print(longest_path_with_diagonal(n, m, right_matrix, down_matrix, diagonal_matrix)[2])
        print(longest_path_with_diagonal(n, m, right_matrix, down_matrix, diagonal_matrix)[3])