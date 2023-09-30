import numpy as np

def edit_distance(seq1, seq2, n, m, sigma):

    # Initialize zero matrix
    grid = np.zeros((n+1, m+1), dtype=int)

    # Fill row and column
    for i in range(n):
        grid[i+1, 0] = -(i+1) * 5
    for j in range(m):
        grid[0, j+1] = -(j+1) * 5

    for i in range(n):
        for j in range(m):
            seq1_base = seq1[i]
            seq2_base = seq2[j]
            if seq1_base == seq2_base:
                x = grid[i, j+1] - sigma
                y = grid[i+1, j] - sigma
                z = grid[i, j]
                maxyz = max(x, y, z)
            else:
                x = grid[i, j+1] - sigma
                y = grid[i+1, j] - sigma
                z = grid[i, j] - 1
                maxyz = max(x, y, z)
            grid[i+1, j+1] = maxyz

    max_score = grid[n, m]

    return max_score, grid


if __name__ == '__main__':
    with open('rosalind_ba5g.txt', 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()

        n = len(seq1)
        m = len(seq2)
        sigma = 1

        print(-edit_distance(seq1, seq2, n, m, sigma)[0])
        # print(edit_distance(seq1, seq2, n, m, sigma)[1])