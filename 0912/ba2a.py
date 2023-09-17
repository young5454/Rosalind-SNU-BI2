from ba1g import hamming_distance
from ba2b import generate_kmers

def MotifEnumeration(dna, k, d):
    patterns = []
    all_kmers = generate_kmers(k)
    for kmer in all_kmers:
        screened = []
        for seq in dna:
            screened.append(screen_sequence(seq, kmer, d))
        if all(screened):
            patterns.append(kmer)
    patterns = set(patterns)
    return patterns


def screen_sequence(string, kmer, d):
    is_screened = False
    string_length = len(string)
    k = len(kmer)
    for i in range(string_length - k + 1):
        curr_kmer = string[i:i + k]
        if hamming_distance(curr_kmer, kmer) <= d:
            is_screened = True
    return is_screened


if __name__ == '__main__':
    with open("rosalind_ba2a.txt") as file:
        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
        k, d = data_list[0].split(' ')
        k = int(k)
        d = int(d)
        dna = data_list[1:]
        patterns = MotifEnumeration(dna, k, d)
        for d in patterns:
            print(d)