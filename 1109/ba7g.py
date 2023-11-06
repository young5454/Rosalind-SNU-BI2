from ba7f import small_parsimony, hamming_distance

# Small Parsimony in an Unrooted Tree Problem

if __name__ == '__main__':
    with open("rosalind_ba7g.txt") as file:
        n = file.readline()
        n = int(n)

        inners = []
        leaves = []
        
        lines = file.read().splitlines()

        # Categorize inner, leaf nodes
        first_stage = []
        for line in lines:
            starty, endy = line.split('->')
            if 'A' in endy or 'T' in endy or 'G' in endy or 'C' in endy:
                leaves.append(endy)
                first_stage.append(starty)
            else:
                inners.append(endy)
        
        # Checkmarks for processed nodes
        processed = [_ for _ in first_stage]
        curr_stage = set(first_stage)
        stages = [curr_stage]

        # Get max two nodes as connection
        int_nodes = []
        for node in inners:
            int_nodes.append(int(node))
        int_nodes = set(int_nodes)
        sorted(int_nodes)
        node1, node2 = str(list(int_nodes)[-2]), str(list(int_nodes)[-1])

        # Make new dataset for small parsimony
        new_lines = []
        for line in lines:
            starty, endy = line.split('->')
            if (starty, endy) == (node1, node2) or (starty, endy) == (node2, node1):
                pass
            else:
                if 'A' in starty or 'T' in starty or 'G' in starty or 'C' in starty:
                    pass
                elif 'A' in endy or 'T' in endy or 'G' in endy or 'C' in endy:
                    new_lines.append(line)
                    pass
                elif int(starty) < int(endy):
                    pass
                elif int(starty) > int(endy):
                    new_lines.append(line)
                    pass
        
        # Add root info
        root_to_node1 = 'root' + '->' + node1
        root_to_node2 = 'root' + '->' + node2
        new_lines.append(root_to_node1)
        new_lines.append(root_to_node2)

        # Add root to inners and modify to set
        inners.append('root')
        inners = set(inners)
        
        # print(new_lines)

        # Make full information dictionary
        full = {}
        for new_line in new_lines:
            starty, endy = new_line.split('->')
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
            if node == 'root':
                children = full[node]['children']
                c1, c2 = children
                child_seq1 = seqs[c1]
                child_seq2 = seqs[c2]
                weight = hamming_distance(child_seq1, child_seq2)
                print(child_seq1 + '->' + child_seq2 + ':' + str(weight))
                print(child_seq2 + '->' + child_seq1 + ':' + str(weight))
            else:
                inner_seq = seqs[node]
                children = full[node]['children']
                for c in children:
                    child_seq = seqs[c]
                    weight = hamming_distance(inner_seq, child_seq)
                    # ATTGCGAC->ATAGCCAC:2
                    print(inner_seq + '->' + child_seq + ':' + str(weight))
                    # Reverse
                    print(child_seq + '->' + inner_seq + ':' + str(weight))