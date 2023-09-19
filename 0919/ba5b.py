import numpy as np

def longest_path(n, m, right_matrix, down_matrix):
    # Initialize zero matrix
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
            maxy = max(x, y)
            grid[i+1, j+1] = maxy
    # Longest path
    max_path = grid[n, m]

    return max_path


if __name__ == '__main__':
    with open('rosalind_ba5b.txt', 'r') as file:
        # Parse n and m
        n, m = map(int, file.readline().split())

        # Initialize matrix 1 and 2
        down_matrix = np.empty((n, m+1), dtype=int)
        right_matrix = np.empty((n+1, m), dtype=int)

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

        print(longest_path(n, m, right_matrix, down_matrix))

