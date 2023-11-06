import numpy as np

# SmallParsimony(T, Character)
#  for each node v in tree T
#         Tag(v) ← 0
#   if v is a leaf
#    Tag(v) ← 1
#    for each symbol k in the alphabet
#     if Character(v) = k
#      sk(v) ← 0
#     else
#      sk(v) ← ∞
#  while there exist ripe nodes in T
#   v ← a ripe node in T
#   Tag(v) ← 1
#   for each symbol k in the alphabet
#       sk(v) ← minimum over all symbols i {si(Daughter(v))+δi,k} + minimum over all symbols j {sj(Son(v))+δj,k}
#    return minimum over all symbols k {sk(v)}

def delta(i, k):
    if i == k:
        return 0
    else:
        return 1


def hamming_distance(seq1, seq2):
    count = 0
    length = len(seq1)
    for i in range(length):
        if seq1[i] != seq2[i]:
            count += 1
    return count


def small_parsimony(n, seqs, inner, leaves, full, index):
    num_nodes = len(full)

    nucleotides = 'ATGC'

    # Initialize for every index iteration
    tag = {node : 0 for node in full.keys()}
    record = {node: [['X', 'X'] for _ in range(4)] for node in full.keys()}
    score = {node: [np.inf, np.inf, np.inf, np.inf] for node in full.keys()}

    # Initialize ripe set
    ripe = set()
    for inner_node in inner:
        children = full[inner_node]['children']
        for child in children:
            if child in leaves:
                ripe.add(inner_node)

    for leaf in leaves:
        char = leaf[index]
        base_index = nucleotides.index(char)
        score[leaf][base_index] = 0

    # print(score)

    while len(ripe) > 0:
        # Get inner node
        inner_node = ripe.pop()

        # Change tag info
        tag[inner_node] = 1

        for base in range(4):
            # Get daughter and son - inner nodes always have two children
            daughter = full[inner_node]['children'][0]
            son = full[inner_node]['children'][1]

            # Min over all symbols i {si(Daughter(v))+δi,k} + minimum over all symbols j {sj(Son(v))+δj,k}
            d_list, s_list = [], []
            for a in range(4):
                # Daughter
                curr_d = delta(a, base) + score[daughter][a]
                d_list.append(curr_d)

                # Son
                curr_s = delta(a, base) + score[son][a]
                s_list.append(curr_s)
            
            # Get index that has min value
            min_d = np.argmin(d_list)
            min_s = np.argmin(s_list)

            # Change index number to base and save
            min_d_base = nucleotides[min_d]
            min_s_base = nucleotides[min_s]

            # A:0, T:1, G:2, C:3
            record[inner_node][base] = [min_d_base, min_s_base]
            score[inner_node][base] = d_list[min_d] + s_list[min_s]

            # Add parent of current ripe nodes to ripe
            # Every children of the internal node has to be tag = 1
            for new_inner in inner:
                if inner_node in full[new_inner]['children']:
                    if all(tag[node] for node in full[new_inner]['children']):
                        ripe.add(new_inner)
    ####
    # Backtracking from root
    root = inner_node
    base_index = np.argmin(score[root])
    this_base = nucleotides[base_index]

    # Concatenate sequence
    seqs[root] += this_base

    # Root score = total hamming distance
    root_score = score[root][base_index]

    # Function to perform recursive backtracking
    def backtrack(node, index):
        if full[node]['children'] is not None:
            daughter, son = full[node]['children']

            if (daughter not in leaves) and (son not in leaves):
                d_base, s_base = record[node][index]
                
                d_index = nucleotides.index(d_base)
                s_index = nucleotides.index(s_base)
                
                seqs[daughter] += d_base
                seqs[son] += s_base
                
                backtrack(daughter, d_index)
                backtrack(son, s_index)

    backtrack(root, base_index)

    return root_score

    
if __name__ == '__main__':
    with open("rosalind_ba7f.txt") as file:
        n = file.readline()
        n = int(n)

        # Read the text file
        lines = file.read().splitlines()
        inners = []
        leaves = []

        # Categorize inner, leaf nodes
        for line in lines:
            starty, endy = line.split('->')
            inners.append(starty)
            if 'A' in endy or 'T' in endy or 'G' in endy or 'C' in endy:
                leaves.append(endy)
        
        inners = set(inners)
        # print(inners)
        # print(leaves)

        # Make full information dictionary
        full = {}
        for line in lines:
            starty, endy = line.split('->')
            if starty not in full.keys():
                info = {'leaf': 0, 'children': [endy]}
                full[starty] = info
                if endy in leaves:
                    leaf_info = {'leaf': 1, 'children': None}
                    full[endy] = leaf_info
            else:
                full[starty]['children'].append(endy)
                if endy in leaves:
                    leaf_info = {'leaf': 1, 'children': None}
                    full[endy] = leaf_info
        # print(full)

        # Initialize sequence dictionary
        seqs = {}
        for node in full.keys():
            if node in leaves:
                seqs[node] = node
            else:
                seqs[node] = ''
        
        # Length of each sequence
        m = len(leaves[0])

        # Iteratively run small parsimony for all characters
        total = 0
        for i in range(m):
            curr_root_score = small_parsimony(n, seqs, inners, leaves, full, i)
            total += curr_root_score
        # print(seqs)

        # Print output
        print(total)
        for node in inners:
            inner_seq = seqs[node]
            children = full[node]['children']
            for c in children:
                child_seq = seqs[c]
                weight = hamming_distance(inner_seq, child_seq)
                # ATTGCGAC->ATAGCCAC:2
                print(inner_seq + '->' + child_seq + ':' + str(weight))
                # Reverse
                print(child_seq + '->' + inner_seq + ':' + str(weight))

            
            




