def hamming_distance(seq1, seq2):
    count = 0
    length = len(seq1)
    for i in range(length):
        if seq1[i] != seq2[i]:
            count += 1
    return count

if __name__ == '__main__':
    with open("rosalind_ba1g.txt") as file:
        first = file.readline().strip('\n')
        second = file.readline().strip('\n')
    print(hamming_distance(first, second))