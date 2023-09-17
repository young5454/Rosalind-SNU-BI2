from ba2c import calculate_prob, profile_most_probable
from ba2e import motif_to_profile_pseudocounts
from ba2f import motifs_from_profile
import random as rand
import copy

def GibbsSampler(dna, k, t, n):
    # randomly select kmers and initialize motifs
    string_length = len(dna[0])
    best_motifs = []
    for i in range(t):
        random_num = rand.randint(0, string_length - k)
        rand_motif = dna[i][random_num:random_num + k]
        best_motifs.append(rand_motif)
    best_prob_list = motif_to_profile_pseudocounts(best_motifs)
    best_score = sum(calculate_prob(text, k, best_prob_list) for text in best_motifs)
    
    for j in range(n):
        # curr_motifs = copy.deepcopy(best_motifs)
        rand_index = rand.randint(0, t - 1)
        # motif_to_remove = curr_motifs[i]
        # curr_motifs.remove(motif_to_remove)

        curr_motifs = []
        for index, motif in enumerate(best_motifs):
            if index != rand_index:
                curr_motifs.append(motif)
        curr_profile = motif_to_profile_pseudocounts(curr_motifs)
        new_motif = profile_most_probable(dna[rand_index], k, curr_profile)

        # one_excluded_profile = motif_to_profile_pseudocounts(curr_motifs)

        # new_motif = profile_most_probable(dna[i], k, one_excluded_profile)

        curr_motifs.insert(rand_index, new_motif)
        curr_prob_list = motif_to_profile_pseudocounts(curr_motifs)
        curr_score = sum(calculate_prob(text, k, curr_prob_list) for text in curr_motifs)

        if curr_score > best_score:
            best_score = curr_score
            best_motifs = curr_motifs

    return best_score, best_motifs

if __name__ == '__main__':
    with open("rosalind_ba2g.txt") as file:
        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
        k, t, n = data_list[0].split(' ')
        k = int(k)
        t = int(t)
        n = int(n)
        dna = data_list[1:]

        # Initialize the best scoring motifs
        best_score = 0
        best_motifs = None

        # Repeat the radomized motif search 20 times.
        for repeat in range(20):
            current_score, current_motifs = GibbsSampler(dna, k, t, n)
            if current_score > best_score:
                best_score = current_score
                best_motifs = current_motifs
                
        for d in best_motifs:
            print(d)

