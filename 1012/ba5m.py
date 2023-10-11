import numpy as np

def triple_alignment(seq1, seq2, seq3, n, m, l):

    # Initialize zero cubes
    path_cube = np.zeros(((n+1), (m+1), (l+1)), dtype=object)
    path_cube[0, 0, 0] = 'none'

    # 7 cases
    # all same: 'diag'
    # seq1 = seq2 != seq3: 'off1'
    # seq1 != seq2 = seq3: 'off2'
    # seq1 = seq3 != seq3: 'off3'
    # seq1 != seq2 != seq3: 'off4', 'off5', 'off6'

    # Fill row and column
    for i in range(n):
        path_cube[i+1, 0, 0] = 'off1'
    for j in range(m):
        path_cube[0, j+1, 0] = 'off2'
    for k in range(l):
        path_cube[0, 0, k+1] = 'off3'
    for i in range(n):
        for j in range(m):
            path_cube[i+1, j+1, 0] = 'off4'
    for i in range(n):
        for k in range(l):
            path_cube[i+1, 0, k+1] = 'off5'
    for j in range(m):
        for k in range(l):
            path_cube[0, j+1, k+1] = 'off6'

    cube = np.zeros(((n+1), (m+1), (l+1)), dtype=int)

    # Fill
    for i in range(n):
        for j in range(m):
            for k in range(l):
                seq1_base = seq1[i]
                seq2_base = seq2[j]
                seq3_base = seq3[k]
                
                x1 = cube[i, j+1, k+1] - 0
                x2 = cube[i+1, j, k+1] - 0
                x3 = cube[i+1, j+1, k] - 0

                x4 = cube[i, j, k+1] - 0
                x5 = cube[i, j+1, k] - 0
                x6 = cube[i+1, j, k] - 0
                # x2 = cube[i, j+1, k] - 0
                # x3 = cube[i, j, k+1] - 0

                # x4 = cube[i+1, j+1, k] - 0
                # x5 = cube[i+1, j, k+1] - 0
                # x6 = cube[i, j+1, k+1] - 0
        
                # x1 = cube[i+1, j, k] - 0
                # x2 = cube[i, j+1, k] - 0
                # x3 = cube[i, j, k+1] - 0

                # x4 = cube[i+1, j+1, k] - 0
                # x5 = cube[i+1, j, k+1] - 0
                # x6 = cube[i, j+1, k+1] - 0

                if seq1_base == seq2_base == seq3_base:
                    x7 = cube[i, j, k] + 1
                else:
                    x7 = cube[i, j, k]

                maxxx = max(x1, x2, x3, x4, x5, x6, x7)

                if maxxx == x1:
                    path_cube[i+1, j+1, k+1] = 'off1'
                elif maxxx == x2:
                    path_cube[i+1, j+1, k+1] = 'off2'
                elif maxxx == x3:
                    path_cube[i+1, j+1, k+1] = 'off3'
                elif maxxx == x4:
                    path_cube[i+1, j+1, k+1] = 'off4'
                elif maxxx == x5:
                    path_cube[i+1, j+1, k+1] = 'off5'
                elif maxxx == x6:
                    path_cube[i+1, j+1, k+1] = 'off6'
                else:
                    path_cube[i+1, j+1, k+1] = 'diag'
                cube[i+1, j+1, k+1] = maxxx

    # Longest path
    p = n
    q = m
    r = l
    longest_path_seq1 = []
    longest_path_seq2 = []
    longest_path_seq3 = []

    while p >= 0 and q >= 0 and r >= 0:
        direction = path_cube[p, q, r]
        if direction == 'off1':
            p -= 1
            longest_path_seq1.append(seq1[p])
            longest_path_seq2.append('-')
            longest_path_seq3.append('-')
        elif direction == 'off2':
            q -= 1
            longest_path_seq1.append('-')
            longest_path_seq2.append(seq2[q])
            longest_path_seq3.append('-')
        elif direction == 'off3':
            r -= 1
            longest_path_seq1.append('-')
            longest_path_seq2.append('-')
            longest_path_seq3.append(seq3[r])
        elif direction == 'off4':
            p -= 1
            q -= 1
            longest_path_seq1.append(seq1[p])
            longest_path_seq2.append(seq2[q])
            longest_path_seq3.append('-')
        elif direction == 'off5':
            p -= 1
            r -= 1
            longest_path_seq1.append(seq1[p])
            longest_path_seq2.append('-')
            longest_path_seq3.append(seq3[r])
        elif direction == 'off6':
            q -= 1
            r -= 1
            longest_path_seq1.append('-')
            longest_path_seq2.append(seq2[q])
            longest_path_seq3.append(seq3[r])
        elif direction == 'diag':
            p -= 1
            q -= 1
            r -= 1
            longest_path_seq1.append(seq1[p])
            longest_path_seq2.append(seq2[q])
            longest_path_seq3.append(seq3[r])
        else:
            break
    
    print(p, q, r)
    # Finalize common subsequence
    longest_path_seq1.reverse()
    longest_path_seq2.reverse()
    longest_path_seq3.reverse()
    aligned_sequence1 = ''.join(longest_path_seq1)
    aligned_sequence2 = ''.join(longest_path_seq2)
    aligned_sequence3 = ''.join(longest_path_seq3)
    max_score = cube[n, m, l]

    # for i in range(n):
    #     for j in range(m):
    #         seq1_base = seq1[i]
    #         seq2_base = seq2[j]
    #         penalty = blosum62[seq1_base][seq2_base]

    #         x = grid[i, j+1] - 5
    #         y = grid[i+1, j] - 5
    #         z = grid[i, j] + penalty
    #         maxyz = max(x, y, z)
    #         if maxyz == x:
    #             path_grid[i+1, j+1] = 'down '
    #         elif maxyz == y:
    #             path_grid[i+1, j+1] = 'right'
    #         else:
    #             path_grid[i+1, j+1] = 'diag '
    #         grid[i+1, j+1] = maxyz

    # # Longest path
    # p = n
    # q = m
    # longest_path_seq1 = []
    # longest_path_seq2 = []
    # while p >= 0 and q >= 0:
    #     direction = path_grid[p, q]
    #     if direction == 'down ':
    #         p -= 1
    #         longest_path_seq1.append(seq1[p])
    #         longest_path_seq2.append('-')
    #     elif direction == 'right':
    #         q -= 1
    #         longest_path_seq1.append('-')
    #         longest_path_seq2.append(seq2[q])
    #     elif direction == 'diag ':
    #         p -= 1
    #         q -= 1
    #         longest_path_seq1.append(seq1[p])
    #         longest_path_seq2.append(seq2[q])
    #     else:
    #         break

    # # Finalize common subsequence
    # longest_path_seq1.reverse()
    # longest_path_seq2.reverse()
    # aligned_sequence1 = ''.join(longest_path_seq1)
    # aligned_sequence2 = ''.join(longest_path_seq2)
    # max_score = grid[n, m]

    return max_score, aligned_sequence1, aligned_sequence2, aligned_sequence3, path_cube


if __name__ == '__main__':
    with open('rosalind_ba5m.txt', 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()
        seq3 = file.readline().strip()

        n = len(seq1)
        m = len(seq2)
        l = len(seq3)

        # print(triple_alignment(seq1, seq2, n, m, l)[0])
        # print(triple_alignment(seq1, seq2, n, m, l)[1])
        # print(triple_alignment(seq1, seq2, n, m, l)[2])
        triples = triple_alignment(seq1, seq2, seq3, n, m, l)
        print(triples[0])
        print(triples[1])
        print(triples[2])
        print(triples[3])
        # print(triples[4])
        