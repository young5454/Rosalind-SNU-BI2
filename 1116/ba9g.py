# Construct the Suffix Array of a String

def make_suffixes(seq):
    # Make a list cotaining all suffixes of seq
    suffixes = []
    n = len(seq)
    for i in range(n):
        suffixes.append(seq[i:])

    return suffixes


def generate_suffix_array(seq):
    # Suffix list
    suffixes = make_suffixes(seq)

    # Create list containing the starting positions of the suffixes
    # Suffix array of indices
    suffix_array = list(range(len(seq)))
    # print(starting_positions)

    # Sorting
    suffix_array.sort(key=lambda x: suffixes[x])

    # String list
    # suffix_array = [str(s) for s in suffix_array ]

    return suffix_array


if __name__ == '__main__':
    with open("rosalind_ba9g.txt") as file:
        seq = file.readline()

        suffix_array = generate_suffix_array(seq)

        # Print results
        result = ', '.join(suffix_array)
        print(result)


