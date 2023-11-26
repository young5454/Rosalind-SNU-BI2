# BWMATCHING(FirstColumn, LastColumn, Pattern, LastToFirst)
#     top ← 0
#     bottom ← |LastColumn| − 1
#     while top ≤ bottom
#         if Pattern is nonempty
#             symbol ← last letter in Pattern
#             remove last letter from Pattern
#             if positions from top to bottom in LastColumn contain an occurrence of symbol
#                 topIndex ← first position of symbol among positions from top to bottom in LastColumn
#                 bottomIndex ← last position of symbol among positions from top to bottom in LastColumn
#                 top ← LastToFirst(topIndex)
#                 bottom ← LastToFirst(bottomIndex)
#             else
#                 return 0
#         else
#             return bottom − top + 1

from ba9k import last_to_first

def count_last_column(symbol, i, last_column):
    first_i = last_column[:i]
    c = first_i.count(symbol)

    return c


def better_bwmatching(bwt, pattern):
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
            return bottom - top


if __name__ == '__main__':
    with open("rosalind_ba9m.txt") as file:
        bwt = file.readline().strip()
        patterns = file.readline().split()

        results = []
        for pattern in patterns:
            count = better_bwmatching(bwt, pattern)
            if count == None:
                results.append(str(0))
            else:
                results.append(str(count))
        
        print(' '.join(results))


