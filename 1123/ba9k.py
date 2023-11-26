# Last-to-First mapping of a string

def last_to_first(bwt, input_index):
    first_column = sorted(bwt)
    last_column = list(bwt)

    # # Index first_column 
    # first_indexed = {}  # Structure: {char: [start, end]}
    # n = len(first_column)
    # for i in range(n):
    #     if first_column[i] not in first_indexed:
    #         # Mark the starting index 
    #         first_indexed[first_column[i]] = [i, i]
    #     else:
    #         # Update the ending index
    #         first_indexed[first_column[i]][1] = i
    
    # Index last_column
    last_indexed = {}   # Structure: {char: [all occurrences]}
    m = len(last_column)
    for j in range(m):
        if last_column[j] not in last_indexed:
            # Mark the starting index 
            last_indexed[last_column[j]] = [j]
        else:
            # Update the ending index
            curr_list = last_indexed[last_column[j]]
            curr_list.append(j)
            last_indexed[last_column[j]] = curr_list
    
    # First-last property to find symbol at first_column
    given_char = last_column[input_index]

    last_column_list = last_indexed[given_char]
    find_index = last_column_list.index(input_index) + 1

    return find_index


if __name__ == '__main__':
    with open("rosalind_ba9k.txt") as file:
        bwt = file.readline()
        input_index = int(file.readline())

        find_index = last_to_first(bwt, input_index)
        print(find_index)
