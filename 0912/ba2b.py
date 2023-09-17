from ba1g import hamming_distance

def min_hd(pattern, text):
    text_length = len(text)
    k = len(pattern)
    hd_list = []

    for i in range(text_length - k + 1):
            kmer = text[i: i + k]
            curr_hd = hamming_distance(pattern, kmer)
            hd_list.append(curr_hd)

    return min(hd_list)

def sum_hd(pattern, dna):
    total = 0
    for string in dna:
        curr = min_hd(pattern, string)
        total += curr
    return total

def generate_kmers(k):
    nucleotides = ['A', 'T', 'G', 'C']
    kmers = []

    if k == 0:
        return kmers

    # Recursive case: Generate kmers of length k-1 and append each nucleotide to them.
    shorter_kmers = generate_kmers(k - 1)
    if not shorter_kmers:
        return nucleotides  # If k is 1, return single nucleotides.

    for kmer in shorter_kmers:
        for nt in nucleotides:
            kmers.append(kmer + nt)

    return kmers

if __name__ == '__main__':
    data_list = []
    with open("rosalind_ba2b.txt") as file:
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
    k = int(data_list[0])
    dna = data_list[1:]
    all_kmers = generate_kmers(k)

    median_string = ''
    curr = float('inf')
    for kmer in all_kmers:
        curr_sum_hd = sum_hd(kmer, dna)
        if curr_sum_hd < curr:
            median_string = kmer
            curr = curr_sum_hd

    print(median_string)





