import numpy as np
from itertools import product

# From ba10a
def hidden_path_prob(path, states, transition):
    # Calculate initial probability
    init_prob = 1 / len(states)

    prob = init_prob

    for i in range(len(path)-1):
        two = path[i:i+2]
        before, after = two[0], two[1]

        # States to index
        before_index = states.index(before)
        after_index = states.index(after)

        # Get transition probability
        curr_trans_prob = transition[before_index, after_index]
        prob *= curr_trans_prob
    
    return prob


# From ba10b
def outcome_prob(text, path, states, sigma, emission):
    prob = 1

    for i in range(len(path)):
        hidden_state = path[i]
        string_alphabet = text[i]

        # States and alphabets to index
        state_index = states.index(hidden_state)
        alphabet_index = sigma.index(string_alphabet)

        # Get emission probability
        curr_prob = emission[state_index, alphabet_index]
        prob *= curr_prob
    
    return prob


def all_possible_paths(k, states):
    # Generate all possible combinations of length k from states
    all_combinations = list(product(states, repeat=k))

    return all_combinations


def calculate_joint(text, path, states, sigma, transition, emission):
    # Pr(x, pi) = Pr(x | pi) X Pr(pi)
    pr_cond = outcome_prob(text, path, states, sigma, emission)
    pr_path = hidden_path_prob(path, states, transition)

    return pr_cond * pr_path


def soft_decoding(text, sigma, states, transition, emission):
    num_states = len(states)
    n = len(text)
    
    # Initialize Matrices for storing probabilities
    # |states| X |alphabets emitted, n|
    state_prob = np.zeros((num_states, n))


    all_paths = all_possible_paths(n, states)
    divsor = 0
    for curr_path in all_paths:
        joint = calculate_joint(text, curr_path, states, sigma, transition, emission)
        divsor += joint
    
    for i in range(n):
        # All paths pi with pi = k
        for j in range(len(states)):
            curr = states[j]
            picked_paths = []
            for p in all_paths:
                if p[i] == curr:
                    picked_paths.append(p)
            num = 0
            for curr_path in picked_paths:
                joint = calculate_joint(text, curr_path, states, sigma, transition, emission)
                num += joint
            state_prob[j, i] = num / divsor
            
    return state_prob


if __name__ == '__main__':
    with open("rosalind_ba10j.txt") as file:
        # Text
        text = file.readline().strip()

        _ = file.readline().strip()
        
        # Sigma
        sigma = file.readline().split()

        _ = file.readline().strip()

        # States
        states = file.readline().split()

        _ = file.readline().strip()

        # Transition matrix 
        header = file.readline().strip()
        n = len(states)
        transition = np.zeros((n, n))
        data_list = file.read().split('\n')

        for data in data_list:
            if '-' in data:
                _index = data_list.index(data)

        transition_data = data_list[:_index]

        for i in range(len(transition_data)):
            parsed = transition_data[i].split()
            symbol = parsed[0]
            float_data = np.array([float(data) for data in parsed[1:]])
            transition[i] = float_data
        
        # Emission matrix 
        emission_data = data_list[_index:]
        _ = emission_data[0]
        header = emission_data[1]
        n = len(states)
        m = len(sigma)
        emission = np.zeros((n, m))

        data_list = emission_data[2:]
        for i in range(len(data_list)):
            parsed = data_list[i].split()
            symbol = parsed[0]
            float_data = np.array([float(data) for data in parsed[1:]])
            emission[i] = float_data

        # Compute soft decoding probabilities
        state_prob = soft_decoding(text, sigma, states, transition, emission)
        state_prob = np.transpose(state_prob)

        header = ' '.join(states)
        print(header)
        for i in range(len(text)):
            row = list(state_prob[i])
            string_row = [str(x) for x in row]
            print(' '.join(string_row))