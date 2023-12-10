import numpy as np
from ba10h import count_emission, count_transition

def new_soft_decoding(text, sigma, states, transition, emission):
    n = len(text)
    num_states = len(states)

    # Initialize Matrices for storing probabilities
    # |states| X |alphabets emitted, n|
    state_response = np.zeros((num_states, n))

    # |states| X |states| X n-1
    edge_response = np.zeros((num_states, num_states, n-1))

    forward = np.zeros((n, num_states))
    backward = np.zeros((n, num_states))

    # Initialize forward matrix
    for k in range(num_states):
        forward[0, k] = emission[k, sigma.index(text[0])] / num_states
    # Fill
    for i in range(1, n):
        for j in range(num_states):
            summed = 0
            for k in range(num_states):
                summed += forward[i-1, k] * transition[k, j] * emission[j, sigma.index(text[i])]
            forward[i, j] = summed
    
    # Initialize backward matrix
    for k in range(num_states):
        backward[n-1, k] = 1
    # Fill
    for i in range(n-2, -1, -1):
        for j in range(num_states):
            summed = 0
            for k in range(num_states):
                summed += backward[i+1, k] * transition[j, k] * emission[k, sigma.index(text[i+1])]
            backward[i, j] = summed
    
    divisor = sum(forward[n-1])

    # State response
    for i in range(n):
        for j in range(num_states):
            state_response[j, i] = forward[i, j] * backward[i, j] / divisor
    
    # Edge response
    for s1 in range(num_states):
        for s2 in range(num_states):
            for i in range(n-1):
                edge_response[s1, s2, i] = forward[i, s1] * transition[s1, s2] * emission[s2, sigma.index(text[i+1])] * backward[i+1, s2] / divisor
    
    # print('After soft decoding')
    # print(state_response)
    # print(edge_response)
    
    return state_response, edge_response

    
def estimate_params_v2(state_response, edge_response, sigma, states):
    """
    Parmameter estimation for responsibility matrices 
    """
    # Transition
    num_of_states = len(states)

    # Initialize transition matrix
    transition = np.zeros((num_of_states, num_of_states))

    # Fill with edge response
    for i in range(num_of_states):
        for j in range(num_of_states):
            value = edge_response[i, j]
            # Sum up the array
            summed = np.sum(value)
            transition[i, j] = summed
    
    # 0 case
    for i in range(num_of_states):
        row = transition[i]
        if np.sum(row) == 0:
            prob = 1 / num_of_states
            for j in num_of_states:
                transition[i, j] = prob
        else:
            transition[i] = row / np.sum(row)

    # Emission
    n = len(sigma)

    # Initialize emission matrix
    emission = np.zeros((num_of_states, n))

    # Fill with state response
    for i in range(num_of_states):
        # Iterate all text length
        for j in range(len(text)):
            emission[i, sigma.index(text[j])] += state_response[i, j]
    
    # 0 case
    for i in range(num_of_states):
        row = emission[i]
        if np.sum(row) == 0:
            prob = 1 / n
            for j in n:
                emission[i, j] = prob
        else:
            emission[i] = row / np.sum(row)
    
    # print('After estimation')
    # print(transition)
    # print(emission)

    return transition, emission


def baum_welch(transition, emission, text, sigma, states, iter):
    count = 0
    while count < iter:
        # Get responsibility matrices
        state_response, edge_response = new_soft_decoding(text, sigma, states, transition, emission)

        # Get new transition, emission matrices
        transition, emission = estimate_params_v2(state_response, edge_response, sigma, states)
        
        count += 1
    
    return transition, emission


if __name__ == '__main__':
    with open("rosalind_ba10k.txt") as file:
        # Iteration
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

        ### Run Baum-Welch learning
        final_transition, final_emission = baum_welch(transition, emission, text, sigma, states, iter)

        # Transition: format output
        header = ' ' + ' '.join(states)
        print(header)
        for i in range(len(states)):
            row = list(final_transition[i])
            string_row = [str(x) for x in row]
            print(states[i] + ' ' + ' '.join(string_row))
        
        print('--------')

        # Emission: format output
        header = ' ' + ' '.join(sigma)
        print(header)
        for i in range(len(states)):
            row = list(final_emission[i])
            string_row = [str(x) for x in row]
            print(states[i] + ' ' + ' '.join(string_row))
