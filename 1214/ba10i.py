# Viterbi Learning
import numpy as np
from ba10h import count_transition, count_emission, estimate_params

# From ba10c
def viterbi(text, sigma, states, transition, emission):
    num_states = len(states)
    n = len(text)
    
    # Initialize Matrices for storing probabilities
    # |states| X |alphabets emitted, n|
    viterbi_mat = np.zeros((num_states, n))

    # Backtrack matrix holds the state index
    backtrack = np.zeros((num_states, n), dtype=int)
    
    # Initialize first column of viterbi matrix
    first_alphabet = text[0]
    for i in range(num_states):
        viterbi_mat[i, 0] = transition[0, i] * emission[i, sigma.index(first_alphabet)]
        backtrack[i, 0] = 0
    
    # Fill
    for j in range(1, n):
        curr_alphabet = text[j]
        for i in range(num_states):
            # Find the maximum probability
            max_prob = -1
            max_state = -1
            
            for i_prev in range(num_states):
                prob = viterbi_mat[i_prev, j - 1] * transition[i_prev, i] * emission[i, sigma.index(curr_alphabet)]
                if prob > max_prob:
                    max_prob = prob
                    max_state = i_prev
                    
            viterbi_mat[i, j] = max_prob
            backtrack[i, j] = max_state
    
    # Bakctrack to find the most likely path
    path_list = []
    max_prob_last_state = np.argmax(viterbi_mat[:, n - 1])
    path_list.append(max_prob_last_state)
    
    for t in range(n):
        max_prob_last_state = backtrack[max_prob_last_state, n-t-1]
        path_list.insert(0, max_prob_last_state)
    
    # print(path_list)

    # Path into hidden path
    hidden_path = ''
    for index in path_list[1:]:
        hidden_path += states[index] 

    return hidden_path


def viterbi_learning(text, sigma, states, transition, emission, iter):
    count = 0
    while count < iter:
        # Decoding problem
        hidden_path = viterbi(text, sigma, states, transition, emission)

        # HMM parameter estimation
        transition, emission = estimate_params(text, hidden_path, sigma, states)

        count += 1
    
    return transition, emission


if __name__ == '__main__':
    with open("rosalind_ba10i.txt") as file:
        # Interation
        iter = int(file.readline().strip())

        _ = file.readline().strip()

        # Text
        text = file.readline().strip()

        _ = file.readline().strip()
        
        # Sigma
        sigma = file.readline().split()

        _ = file.readline().strip()

        # States
        states = file.readline().split()

        _ = file.readline().strip()

        # Initial transition matrix 
        header = file.readline().strip()
        n = len(states)
        init_transition = np.zeros((n, n))
        data_list = file.read().split('\n')

        for data in data_list:
            if '-' in data:
                _index = data_list.index(data)

        transition_data = data_list[:_index]

        for i in range(len(transition_data)):
            parsed = transition_data[i].split()
            symbol = parsed[0]
            float_data = np.array([float(data) for data in parsed[1:]])
            init_transition[i] = float_data
        
        # Initial emission matrix 
        emission_data = data_list[_index:]
        _ = emission_data[0]
        header = emission_data[1]
        n = len(states)
        m = len(sigma)
        init_emission = np.zeros((n, m))

        data_list = emission_data[2:]
        for i in range(len(data_list)):
            parsed = data_list[i].split()
            symbol = parsed[0]
            float_data = np.array([float(data) for data in parsed[1:]])
            init_emission[i] = float_data
        
        ### Run viterbi learning
        transition, emission = viterbi_learning(text, sigma, states, init_transition, init_emission, iter)

        # Transition: format output
        header = ' ' + ' '.join(states)
        print(header)
        for i in range(len(states)):
            row = list(transition[i])
            string_row = [str(x) for x in row]
            print(states[i] + ' ' + ' '.join(string_row))
        
        print('--------')

        # Emission: format output
        header = ' ' + ' '.join(sigma)
        print(header)
        for i in range(len(states)):
            row = list(emission[i])
            string_row = [str(x) for x in row]
            print(states[i] + ' ' + ' '.join(string_row))


    
