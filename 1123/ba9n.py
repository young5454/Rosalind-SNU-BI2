from ba9m import better_bwmatching
from ba9i import cyclic_rotations, get_bwt
from ba9m import count_last_column

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


def find_all_occurrences(bwt, pattern, suffix_array):
    first_column = sorted(bwt)

    first_occurrences = {}
    for i in range(len(first_column)):
        if first_column[i] not in first_occurrences:
            # Mark the starting index
            first_occurrences[first_column[i]] = i

    last_column = list(bwt)

    # Initialize top, bottom
    top = 0
    bottom = len(last_column) - 1

    while top <= bottom:
        if pattern != '':
            n = len(pattern)
            symbol = pattern[-1]
            pattern = pattern[:n-1]

            # # Find symbol at the first_column
            # found = []
            # for i in range(top, bottom+1):
            #     if last_column[i] == symbol:
            #         found.append(i)
            
            # if len(found) == 0:
            #     return 0
            
            # # Update top, bottom
            # top_index = found[0]
            # bottom_index = found[-1]

            new_top = first_occurrences[symbol] + count_last_column(symbol, top, last_column)
            new_bottom = first_occurrences[symbol] + count_last_column(symbol, bottom, last_column)

            top = new_top 
            bottom = new_bottom

        else:
            return top, bottom , suffix_array[top: bottom]


if __name__ == '__main__':
    with open("rosalind_ba9n.txt") as file:
        data_list = file.read().split()
        seq = data_list[0] + '$'
        patterns = data_list[1:]
        # seq = "panamabananas$"
        # patterns = ['nas']

        # Get bwt transform
        cycles = cyclic_rotations(seq)
        bwt = get_bwt(cycles)

        # for c in cycles:
        #     print(c)
        # print()
        # print(bwt)

        # Make suffix array
        suffix_array = generate_suffix_array(seq)
        # print(suffix_array)

        results = []
        for pattern in patterns:
            t, b, count_list = find_all_occurrences(bwt, pattern, suffix_array)

            if count_list != None:
                results += count_list

        # Sort and print results
        results.sort()
        results = [str(a) for a in results]
        print(len(results))
        print(' '.join(results))


# seq = "AATCGGGTTCAATCGGGGT"
# seq = seq + "$"
# pattern = "TATAT"


# cycles = cyclic_rotations(seq)
# bwt = get_bwt(cycles)
# suffix_array = generate_suffix_array(seq)

# print(bwt)
# print(suffix_array)

# print(better_bwmatching(bwt, pattern, suffix_array))

