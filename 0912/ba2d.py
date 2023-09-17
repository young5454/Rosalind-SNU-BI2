from ba2c import calculate_prob, profile_most_probable
import numpy as np

def motif_to_profile(motifs):
    t = len(motifs)
    k = len(motifs[0])
    total_nucleotides = []
    for i in range(k):
        curr_nucleotides = [0, 0, 0, 0]
        for motif in motifs:
            if motif[i] == 'A':
                curr_nucleotides[0] += 1
            elif motif[i] == 'C':
                curr_nucleotides[1] += 1
            elif motif[i] == 'G':
                curr_nucleotides[2] += 1
            elif motif[i] == 'T':
                curr_nucleotides[3] += 1
        curr_nucleotides = [x / t for x in curr_nucleotides]
        total_nucleotides.append(curr_nucleotides)
    return np.array(total_nucleotides)


def GreedyMotifSearch(dna, k, t):
    best_motifs = [text[0:k] for text in dna]
    best_prob_list = motif_to_profile(best_motifs)
    best_score = sum(calculate_prob(text, k, best_prob_list) for text in best_motifs)
    # print(best_score)
    # print(best_motifs)
    first_string = dna[0]
    text_length = len(first_string)

    for i in range(text_length - k + 1):
        kmer = first_string[i:i + k]
        motif_1 = kmer
        kmer_list = [motif_1]
        for j in range(2, t + 1):
            next_string = dna[j - 1]
            curr_prob_list = motif_to_profile(kmer_list)
            curr_most_prob_kmer = profile_most_probable(next_string, k, curr_prob_list)
            kmer_list.append(curr_most_prob_kmer)
        # print(kmer_list)
        score = sum(calculate_prob(text, k, curr_prob_list) for text in kmer_list)
        if score > best_score:
            best_score = score
            best_motifs = kmer_list

    return best_motifs


if __name__ == '__main__':
    with open("rosalind_ba2d.txt") as file:
        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
        k, t = data_list[0].split(' ')
        k = int(k)
        t = int(t)
        dna = data_list[1:]
        plits = GreedyMotifSearch(dna, k, t)
        for d in plits:
            print(d)