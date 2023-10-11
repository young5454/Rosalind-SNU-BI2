from ba5k import global_alignment, get_middle

# Pseudocode
#     LinearSpaceAlignment(top, bottom, left, right)
#         if left = right
#             return alignment formed by bottom − top vertical edges
#         if top = bottom
#             return alignment formed by right − left horizontal edges
#         middle ← ⌊(left + right)/2⌋
#         midNode ← MiddleNode(top, bottom, left, right)
#         midEdge ← MiddleEdge(top, bottom, left, right)
#         LinearSpaceAlignment(top, midNode, left, middle)
#         output midEdge
#         if midEdge = "→" or midEdge = "↘"
#             middle ← middle + 1
#         if midEdge = "↓" or midEdge ="↘"
#             midNode ← midNode + 1
#         LinearSpaceAlignment(midNode, bottom, middle, right)

    
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


def linear_space_alignment(seq1, seq2, sigma, top, bottom, left, right):

    if left == right:
        seq1_trimmed = seq1[top:bottom]
        alignment = '-' * (bottom - top)
        return seq1_trimmed, alignment
    
    elif top == bottom:
        seq2_trimmed = seq2[left:right]
        alignment = '-' * (right - left)
        return alignment, seq2_trimmed
    
    # elif bottom - top == 1:
    #     # One-square case
    #     last_seq1 = seq1[top:top+1]
    #     seq2_trimmed = seq2[left:right]
    #     _, seq1_alignment, seq2_alignment = global_alignment(last_seq1, seq2_trimmed, 1, len(seq2), sigma)
    #     return seq1_alignment, seq2_alignment
    
    # elif right - left == 1:
    #     # One-square case
    #     seq1_trimmed = seq1[top:bottom]
    #     last_seq2 = seq2[left:left+1]
    #     _, seq1_alignment, seq2_alignment = global_alignment(seq1_trimmed, last_seq2, len(seq1), 1, sigma)
    #     return seq1_alignment, seq2_alignment

    elif bottom - top == 1 or right - left == 1:
        new_seq1 = seq1[top:bottom]
        new_seq2 = seq2[left:right]
        return global_alignment(new_seq1, new_seq2, len(new_seq1), len(new_seq2), sigma)[1:]

    
    else:
        middle = (left+right) // 2
        seq1_trimmed = seq1[top:bottom]
        seq2_trimmed = seq2[left:right]
        midnode, nextnode = get_middle(seq1_trimmed, seq2_trimmed, len(seq1_trimmed), len(seq2_trimmed), sigma)
        
        new_midnode_x = midnode[0] + top
        new_midnode_y = midnode[1] + left
        new_nextnode_x = nextnode[0] + top
        new_nextnode_y = nextnode[1] + left

        midnode = (new_midnode_x, new_midnode_y)
        nextnode = (new_nextnode_x, new_nextnode_y)

        # Add the middle edge alignment to finish
        x_gap = nextnode[1] - midnode[1]
        y_gap = nextnode[0] - midnode[0]

        # ↓ case
        if y_gap == 1 and x_gap == 0:
            seq1_ = seq1[midnode[0]]
            seq2_ = '-'
        # → case
        elif y_gap == 0 and x_gap == 1:
            seq1_ = '-'
            seq2_ = seq2[midnode[1]]
        # ↘ case
        elif y_gap == 1 and x_gap == 1:
            seq1_ = seq1[midnode[0]]
            seq2_ = seq2[midnode[1]]
        
        area_A = linear_space_alignment(seq1, seq2, sigma, top, midnode[0], left, midnode[1])
        area_B = linear_space_alignment(seq1, seq2, sigma, nextnode[0], bottom, nextnode[1], right)
        # current = [['-', seq1[midnode[0] % len(seq1)]][nextnode[0] - midnode[0]], ['-', seq2[midnode[1] % len(seq2)]][nextnode[1] - midnode[1]]]

        seq1_alignment = area_A[0] + seq1_ + area_B[0]
        seq2_alignment = area_A[1] + seq2_ + area_B[1]

        return seq1_alignment, seq2_alignment


def calculate_blosum62_score(seq1_alignment, seq2_alignment, sigma):
    score = 0
    for i in range(len(seq1_alignment)):
        seq1_base = seq1_alignment[i]
        seq2_base = seq2_alignment[i]
        if seq1_base == '-' or seq2_base == '-':
            score -= sigma
        else:
            score += blosum62[seq1_base][seq2_base]
    return score


if __name__ == '__main__':
    with open('rosalind_ba5l.txt', 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()

        n = len(seq1)
        m = len(seq2)

        sigma = 5

        # print(global_alignment(seq1, seq2, n, m, sigma)[0])
        # print(global_alignment(seq1, seq2, n, m, sigma)[1])
        # print(global_alignment(seq1, seq2, n, m, sigma)[2])

        seq1_alignment, seq2_alignment = linear_space_alignment(seq1, seq2, sigma, 0, n, 0, m)
        print(calculate_blosum62_score(seq1_alignment, seq2_alignment, sigma))
        print(seq1_alignment)
        print(seq2_alignment)


        