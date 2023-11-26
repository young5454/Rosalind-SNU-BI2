# Suffix tree of a string problem

def add_suffix_to_tree(tree, suffix):
    current_node = tree

    for char in suffix:
        if char not in current_node:
            current_node[char] = {}
        current_node = current_node[char]


def construct_suffix_tree(text):
    suffix_tree = {}

    for i in range(len(text)):
        add_suffix_to_tree(suffix_tree, text[i:])

    return suffix_tree


def find_leaves(tree, nodes = [], keys = []):
    for char, subtree in tree.items():
        next_tree = tree[char]
        if len(next_tree) <= 1:
            nodes.append([char, next_tree])
        else:
            keys.append(char)
            find_leaves(next_tree)

    return nodes, keys


def complete_string(leaf, curr_string=""):
    index = leaf[0]
    dict = leaf[1]

    while dict != {}:
        curr_key = list(dict.keys())[0]
        curr_string += curr_key
        dict = dict[curr_key]
    
    curr_string = index + curr_string

    return curr_string


if __name__ == '__main__':
    with open("rosalind_ba9c.txt") as file:
        string = file.readline()

        # Suffix tree 
        tree = construct_suffix_tree(string)

        # Get leaves
        leaves, inners = find_leaves(tree)

        # Print all edges
        for leaf in leaves:
            print(complete_string(leaf))
        for i in inners:
            print(i)  
