from ba2c import calculate_prob, profile_most_probable
from ba2e import motif_to_profile_pseudocounts
import random as rand

def motifs_from_profile(profile, dna, k):
	return [profile_most_probable(seq, k, profile) for seq in dna]

def RandomizedMotifSearch(dna, k, t):
    # randomly select kmers and initialize motifs
    string_length = len(dna[0])
    best_motifs = []
    for i in range(t):
        random_num = rand.randrange(0, string_length - k + 1)
        rand_motif = dna[i][random_num:random_num + k]
        best_motifs.append(rand_motif)
    random_prob_list = motif_to_profile_pseudocounts(best_motifs)
    best_score = sum(calculate_prob(text, k, random_prob_list) for text in best_motifs)

    while True:
        curr_prob_list = motif_to_profile_pseudocounts(best_motifs)
        curr_motifs = motifs_from_profile(curr_prob_list, dna, k)
        curr_score = sum(calculate_prob(text, k, curr_prob_list) for text in curr_motifs)
        if curr_score > best_score:
            best_score = curr_score
            best_motifs = curr_motifs
        else:
            return best_score, best_motifs


if __name__ == '__main__':
    with open("rosalind_ba2f.txt") as file:
        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
        k, t = data_list[0].split(' ')
        k = int(k)
        t = int(t)
        dna = data_list[1:]

        # Initialize the best scoring motifs
        best_score = 0
        best_motifs = None

        # Repeat the radomized motif search 1000 times.
        for repeat in range(1000):
            current_score, current_motifs = RandomizedMotifSearch(dna, k, t)
            if current_score > best_score:
                best_score = current_score
                best_motifs = current_motifs
                
        for d in best_motifs:
            print(d)