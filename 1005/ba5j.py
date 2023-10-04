import numpy as np

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


def affine_gap_alignment(seq1, seq2, n, m, gap_opening, gap_extension):

    # Initialize three zero matrices
    lower_grid = np.zeros((n+1, m+1), dtype=int)    # Insertions
    middle_grid = np.zeros((n+1, m+1), dtype=int)   # Matches/mismatches
    upper_grid = np.zeros((n+1, m+1), dtype=int)    # Deletions

    lower_path_grid = np.zeros((n+1, m+1), dtype=object)
    middle_path_grid = np.zeros((n+1, m+1), dtype=object)
    upper_path_grid = np.zeros((n+1, m+1), dtype=object)
    lower_path_grid[0, 0] = 'none'
    middle_path_grid[0, 0] = 'none'
    upper_path_grid[0, 0] = 'none'

    # test

    # # Fill row and column
    # for i in range(n):
    #     path_grid[i+1, 0] = 'down '
    # for j in range(m):  
    #     path_grid[0, j+1] = 'right'

    # Fill 
    # Fill row and column for all three matrices
    for i in range(n):
        lower_grid[i+1, 0] = -gap_opening - i * gap_extension
        upper_grid[i+1, 0] = -100000
        middle_grid[i+1, 0] = -gap_opening - i * gap_extension

    for j in range(m):
        lower_grid[0, j+1] = -100000
        upper_grid[0, j+1] = -gap_opening - j * gap_extension
        middle_grid[0, j+1] = -gap_opening - j * gap_extension

    for i in range(n):
        for j in range(m):
            seq1_base = seq1[i]
            seq2_base = seq2[j]
            score = blosum62[seq1_base][seq2_base]

            lower_x = lower_grid[i, j+1] - gap_extension
            lower_y = middle_grid[i, j+1] - gap_opening
            curr_lower = max(lower_x, lower_y)
            lower_grid[i+1, j+1] = curr_lower
            # Gap opening case
            if curr_lower == lower_y:
                lower_path_grid[i+1, j+1] = 'middle'

            upper_x = upper_grid[i+1, j] - gap_extension
            upper_y = middle_grid[i+1, j] - gap_opening
            curr_upper = max(upper_x, upper_y)
            upper_grid[i+1, j+1] = curr_upper
            # Gap opening case
            if curr_upper == upper_y:
                upper_path_grid[i+1, j+1] = 'middle'

            middle_x = lower_grid[i+1, j+1]
            middle_y = middle_grid[i, j] + score
            middle_z = upper_grid[i+1, j+1]
            middle_maxyz = max(middle_x, middle_y, middle_z)
            middle_grid[i+1, j+1] = middle_maxyz

            if middle_maxyz == middle_x:
                middle_path_grid[i+1, j+1] = 'lower'
            elif middle_maxyz == middle_y:
                middle_path_grid[i+1, j+1] = 'middle'
            else:
                middle_path_grid[i+1, j+1] = 'upper'

    # Longest path
    p = n
    q = m
    longest_path_seq1 = []
    longest_path_seq2 = []
    level = 'middle'
    while p >= 0 and q >= 0:
        direction = middle_path_grid[p, q]
        if level == 'lower':
            if lower_path_grid[p, q] == 'middle':
                level = 'middle'
            p -= 1
            longest_path_seq1.append(seq1[p])
            longest_path_seq2.append('-')
        elif level == 'upper':
            if upper_path_grid[p, q] == 'middle':
                level = 'middle'
            q -= 1
            longest_path_seq1.append('-')
            longest_path_seq2.append(seq2[q])
        elif level == 'middle':
            if direction == 'middle':
                p -= 1
                q -= 1
                longest_path_seq1.append(seq1[p])
                longest_path_seq2.append(seq2[q])
            else:
                level = direction
        else:
            break

    # Finalize common subsequence
    longest_path_seq1.reverse()
    longest_path_seq2.reverse()
    aligned_sequence1 = ''.join(longest_path_seq1)
    aligned_sequence2 = ''.join(longest_path_seq2)
    max_score = middle_grid[n, m]

    return max_score, aligned_sequence1, aligned_sequence2


if __name__ == '__main__':
    with open('rosalind_ba5j.txt', 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()

        n = len(seq1)
        m = len(seq2)

        gap_opening = 11
        gap_extension = 1

        print(affine_gap_alignment(seq1, seq2, n, m, gap_opening, gap_extension)[0])
        print(affine_gap_alignment(seq1, seq2, n, m, gap_opening, gap_extension)[1])
        print(affine_gap_alignment(seq1, seq2, n, m, gap_opening, gap_extension)[2])