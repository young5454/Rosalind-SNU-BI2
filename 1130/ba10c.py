import numpy as np

def viterbi(string, sigma, states, transition, emission):
    num_states = len(states)
    n = len(string)
    
    # Initialize Matrices for storing probabilities
    # |states| X |alphabets emitted, n|
    viterbi_mat = np.zeros((num_states, n))

    # Backtrack matrix holds the state index
    backtrack = np.zeros((num_states, n), dtype=int)
    
    # Initialize first column of viterbi matrix
    first_alphabet = string[0]
    for i in range(num_states):
        viterbi_mat[i, 0] = transition[0, i] * emission[i, sigma.index(first_alphabet)]
        backtrack[i, 0] = 0
    
    # Fill
    for j in range(1, n):
        curr_alphabet = string[j]
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


if __name__ == '__main__':
    with open("rosalind_ba10c.txt") as file:
        # String 
        string = file.readline().strip()
        # print(string)

        _ = file.readline().strip()

        # Sigma Σ 
        sigma = file.readline().split()
        # print(sigma)

        _ = file.readline().strip()

        # States
        states = file.readline().split()
        # print(states)

        _ = file.readline().strip()
        # print(_)

        header = file.readline().strip()
        # print(header)

        # Transition matrix 
        n = len(states)
        transition = np.zeros((n, n))
        data_list = file.read().split('\n')

        for data in data_list:
            if '-' in data:
                _index = data_list.index(data)
        # print(_index)

        transition_data = data_list[:_index]

        for i in range(len(transition_data)):
            parsed = transition_data[i].split()
            symbol = parsed[0]
            float_data = np.array([float(data) for data in parsed[1:]])
            transition[i] = float_data
        
        # print(transition)

        emission_data = data_list[_index:]
        _ = emission_data[0]
        # print(_)

        header = emission_data[1]
        # print(header)

        # Emission matrix 
        n = len(states)
        m = len(sigma)
        emission = np.zeros((n, m))

        data_list = emission_data[2:]
        for i in range(len(data_list)):
            parsed = data_list[i].split()
            symbol = parsed[0]
            float_data = np.array([float(data) for data in parsed[1:]])
            emission[i] = float_data

        # print(emission)  

        # Run Viterbi
        hidden_path = viterbi(string, sigma, states, transition, emission)
        print(hidden_path)