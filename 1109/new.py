# Define the delta function to calculate Hamming distance
def delta(i, k):
    if i == k:
        return 0
    else:
        return 1

# Function to perform Small Parsimony
def SmallParsimony(tree, character):
    # Initialize Tag and sk dictionaries for each node in the tree
    Tag = {}
    sk = {}

    # Initialize Tag for leaf nodes and compute sk for known characters
    for node in tree:
        if node in character:
            Tag[node] = 1
            for k in 'ATGC':
                sk[(node, k)] = 0 if character[node] == k else float('inf')
        else:
            Tag[node] = 0

    # Helper function to compute sk(v) for an internal node v
    def compute_sk(v, k):
        min_sk = float('inf')
        for i in 'ATGC':
            for j in 'ATGC':
                cost = sk[(v[0], i)] + delta(i, k) + sk[(v[1], j)] + delta(j, k)
                min_sk = min(min_sk, cost)
        return min_sk

    # Main loop to process ripe nodes
    ripe_nodes = [node for node in tree if Tag[node] == 0]
    while ripe_nodes:
        v = ripe_nodes.pop()
        Tag[v] = 1
        for k in 'ATGC':
            sk[(v, k)] = compute_sk(v, k)
        
        # Update the parent node (if any) as a ripe node
        parent = tree[v]
        if parent:
            ripe_nodes.append(parent)

    # Compute the minimum score at the root node
    root = [node for node in tree if tree[node] is None][0]
    min_score = min(sk[(root, k)] for k in 'ATGC')

    return min_score

# Example usage:
tree = {
    'Internal1': ('Leaf1', 'Internal2'),
    'Internal2': ('Leaf2', 'Leaf3'),
    'Leaf1': None,
    'Leaf2': None,
    'Leaf3': None
}

character = {
    'Leaf1': 'ATG',
    'Leaf2': 'TTG',
    'Leaf3': 'GTA'
}

min_score = SmallParsimony(tree, character)
print("Minimum Score:", min_score)
