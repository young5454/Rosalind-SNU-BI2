# Estimate the Parameters of an HMM
import numpy as np

def count_transition(l, k, path, states):
    """
    Number of transitions from state l to k in 'path'
    """

    pair = l + k
    counted = 0
    # Sliding window to count pairs
    for i in range(len(path) - 1):
        if path[i: i+2] == pair:
            counted += 1

    # All transitions
    l_count = path.count(l)

    # 0 count case
    if l_count == 0:
        prob = 1 / len(states)
        return prob

    if path[-1] == l:
        all_transition = l_count - 1
    else:
        all_transition = l_count
    
    prob = counted / all_transition

    return prob


def count_emission(k, b, text, path, sigma):
    """
    Number of times symbol 'b' is emitted when 'path' is in state 'k'
    """
    counted = 0
    for i in range(len(text)):
        if text[i] == b and path[i] == k:
            counted += 1
    
    # All visits to state k
    k_counted = path.count(k)

    # 0 count case
    if k_counted == 0:
        prob = 1 / len(sigma)
        return prob
    
    prob = counted / k_counted

    return prob


def estimate_params(text, path, sigma, states):
    # Transition
    num_of_states = len(states)

    # Initialize transition matrix
    transition = np.zeros((num_of_states, num_of_states))
    for i in range(num_of_states):
        for j in range(num_of_states):
            state1, state2 = states[i], states[j]
            prob = count_transition(state1, state2, path, states)
            transition[i, j] = prob
    
    # Emission
    num_of_sigma = len(sigma)

    # Initialize emission matrix
    emission = np.zeros((num_of_states, num_of_sigma))
    for i in range(num_of_states):
        for j in range(num_of_sigma):
            state = states[i]
            symbol = sigma[j]
            prob = count_emission(state, symbol, text, path, sigma)
            emission[i, j] = prob

    return transition, emission


if __name__ == '__main__':
    with open("rosalind_ba10h.txt") as file:
        # Text
        text = file.readline().strip()

        _ = file.readline().strip()
        
        # Sigma
        sigma = file.readline().split()

        _ = file.readline().strip()

        # Path 
        path = file.readline().strip()

        _ = file.readline().strip()

        # States
        states = file.readline().split()

        # print(text)
        # print(sigma)
        # print(path)
        # print(states)

        transition, emission = estimate_params(text, path, sigma, states)

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
