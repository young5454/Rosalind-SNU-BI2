import numpy as np

def outcome_prob(hidden_path, string, states, sigma, emission):
    prob = 1

    for i in range(len(hidden_path)):
        hidden_state = hidden_path[i]
        string_alphabet = string[i]

        # States and alphabets to index
        state_index = states.index(hidden_state)
        alphabet_index = sigma.index(string_alphabet)

        # Get emission probability
        curr_prob = emission[state_index, alphabet_index]
        prob *= curr_prob
    
    return prob


if __name__ == '__main__':
    with open("rosalind_ba10b.txt") as file:
        # String 
        string = file.readline().strip()
        # print(string)

        _ = file.readline().strip()

        # Sigma Σ 
        sigma = file.readline().split()
        # print(sigma)

        _ = file.readline().strip()

        # Hidden path
        hidden_path = file.readline().strip()
        # print(hidden_path)

        _ = file.readline().strip()

        # States
        states = file.readline().split()
        # print(states)

        _ = file.readline().strip()
        # print(_)

        header = file.readline().strip()
        # print(header)

        # Emission matrix 
        n = len(states)
        m = len(sigma)
        emission = np.zeros((n, m))

        data_list = file.read().split('\n')
        for i in range(len(data_list)):
            parsed = data_list[i].split()
            symbol = parsed[0]
            float_data = np.array([float(data) for data in parsed[1:]])
            emission[i] = float_data
        
        # print(emission)

        print(outcome_prob(hidden_path, string, states, sigma, emission))