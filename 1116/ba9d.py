# Longest Repeat Problem

def create_kmers(seq, k):
    kmers = []
    n = len(seq)

    for i in range(n-k+1):
        kmer = seq[i : i+k]
        kmers.append(kmer)

    return kmers


def find_first_repeat(listy):
    # Return the first found repeat in a list listy
    seen = set()
    for item in listy:
        if item in seen:
            return item
        seen.add(item)

    return None


def screen_repeats(seq):
    n = len(seq)

    # # Initialize k
    # k = len(seq)

    for i in range(1, n):
        k = n - i

        curr_kmers = create_kmers(seq, k)

        # Check for repeats
        repeat = find_first_repeat(curr_kmers)
        if repeat is not None:
            return repeat

        
if __name__ == '__main__':
    with open("rosalind_ba9d.txt") as file:
        seq = file.readline()
        print(screen_repeats(seq))


# listy = create_kmers('ATATCGTTTTATCGTT', 4)
# print(listy)
# print(find_first_repeat(listy))

# print(screen_repeats('ATATCGTTTTATCGTT'))

