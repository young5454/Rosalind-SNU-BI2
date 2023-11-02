import numpy as np

# LimbLength(i) is equal to the minimum value of 
# (D_i,k + D_i,j - D_j,k) / 2 over all leaves j and k

def limblength(matrix, i, n):
    limb_length = np.inf

    for j in range(n):
        for k in range(n):
            if j != i and k != i:
                d_ik = matrix[i, k]
                d_ij = matrix[i, j]
                d_jk = matrix[j, k]

                cal = (d_ik + d_ij - d_jk) / 2
                if cal < limb_length:
                    limb_length = cal

    # limb_length into integer
    limb_length = int(limb_length)
    
    return limb_length


if __name__ == '__main__':
    with open("rosalind_ba7b.txt") as file:
        # n-number of data points
        # m-dimensional space
        n = file.readline()
        j = file.readline()
        n = int(n)
        j = int(j)

        # Read the text file and convert it into a NumPy ndarray
        lines = file.readlines()
        data_list = [list(map(int, line.split())) for line in lines]

        # Convert the list of lists into a NumPy ndarray
        matrix = np.array(data_list)

        # print(n)
        # print(j)
        # print(matrix)

        print(limblength(matrix, j, n))