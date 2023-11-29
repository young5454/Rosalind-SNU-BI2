import numpy as np

def hidden_path_prob(hidden_path, states, transition):
    # Calculate initial probability
    init_prob = 1 / len(states)

    prob = init_prob

    for i in range(len(hidden_path)-1):
        two = hidden_path[i:i+2]
        before, after = two[0], two[1]

        # States to index
        before_index = states.index(before)
        after_index = states.index(after)

        # Get transition probability
        curr_trans_prob = transition[before_index, after_index]
        prob *= curr_trans_prob
    
    return prob
        


if __name__ == '__main__':
    with open("rosalind_ba10a.txt") as file:
        # Hidden path
        hidden_path = file.readline().strip()
        # print(hidden_path)

        _ = file.readline().strip()
        # print(_)

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

        for i in range(len(data_list)):
            parsed = data_list[i].split()
            symbol = parsed[0]
            float_data = np.array([float(data) for data in parsed[1:]])
            transition[i] = float_data

        # print(transition)

        print(hidden_path_prob(hidden_path, states, transition))