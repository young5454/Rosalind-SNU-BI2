import numpy as np

def profile_to_prob(profile_list):
    """ profile_list is in format of (ACGT X probability)
        fix this to (k X probability of ACGT)
    """
    k = len(profile_list[0])
    parse_list = []
    for item in profile_list:
        item_list = item.split(' ')
        int_item_list = [eval(i) for i in item_list]
        parse_list.append(int_item_list)
        prob_list = np.array(parse_list).T
    
    return prob_list


def calculate_prob(kmer, k, prob_list):
    prob = 1
    for i in range(k):
        curr_base = kmer[i]
        if curr_base == 'A':
            curr_prob = prob_list[i][0]
        elif curr_base == 'C':
            curr_prob = prob_list[i][1]
        elif curr_base == 'G':
            curr_prob = prob_list[i][2]
        elif curr_base == 'T':
            curr_prob = prob_list[i][3]
        prob = prob * curr_prob
    return prob


def profile_most_probable(text, k, prob_list):
    best_prob = -1
    best_kmer = ''
    text_length = len(text)
    for i in range(text_length - k + 1):
        curr_kmer = text[i:i + k]
        curr_total_prob = calculate_prob(curr_kmer, k, prob_list)
        if curr_total_prob > best_prob:
            best_prob = curr_total_prob
            best_kmer = curr_kmer
    return best_kmer


if __name__ == '__main__':
    with open(".rosalind_ba2c.txt") as file:
        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_list.append(cleaned_line)
        text = data_list[0]
        k = int(data_list[1])
        profile_list = data_list[2:]
        prob_list = profile_to_prob(profile_list)
        print(profile_most_probable(text, k, prob_list))