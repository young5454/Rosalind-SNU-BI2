if __name__ == '__main__':
    with open("rosalind_ba8b.txt") as file:
        # k-number of data points
        # m-dimensional space
        k, m = file.readline().split(' ')
        k = int(k)
        m = int(m)

        counter = 0
        data_list = []
        for line in file:
            counter += 1
            cleaned_line = line.strip()
            if '-' in cleaned_line:
                partition = counter
            else:
                data_point = cleaned_line.split(' ')
                float_data = np.array([float(data) for data in data_point])
                data_list.append(float_data)