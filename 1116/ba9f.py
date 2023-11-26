# Shortest Non-Shared Substring Problem

from ba9d import create_kmers

def is_contained(seq, pattern):
    if pattern in seq:
        return True
    else:
        return False
    

def non_shared(seq1, seq2):
    # Create kmers from seq1
    n = len(seq1)
    for k in range(1, n):
        curr_kmers = create_kmers(seq1, k)
        for kmer in curr_kmers:
            if is_contained(seq2, kmer) == False:
                return kmer


if __name__ == '__main__':
    with open("rosalind_ba9f.txt") as file:
        seq1, seq2 = file.read().splitlines()

        print(non_shared(seq1, seq2))