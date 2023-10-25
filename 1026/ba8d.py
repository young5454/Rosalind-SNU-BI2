import numpy as np
import math

def euclidean(point1, point2):
    # Calculate Euclidean distance between two data points
    return ((point1 - point2) ** 2).sum() ** .5


def hidden_matrix(data_points, centers, beta):
    # Calculates the hidden matrix for every center update
    n = len(data_points)
    k = len(centers)
    hidden_matrix = np.zeros((k, n))

    for i in range(k):
        for j in range(n):
            dist = euclidean(centers[i], data_points[j])
            force = math.exp(-beta * dist)
            hidden_matrix[i, j] = force

    # Normalize the hidden_matrix column-wise
    column_sums = hidden_matrix.sum(axis=0)
    hidden_matrix /= column_sums
    
    return hidden_matrix


def update_centers(data_points, centers, hidden_matrix):
    # Update centers using hidden matrix
    m = len(data_points[0])
    k = len(centers)

    new_centers = []

    for i in range(k):
        center_element = []
        for j in range(m):
            # Row of the HiddenMatrix 
            hidden_row = hidden_matrix[i, :]
            hidden_row_sum = np.sum(hidden_row)

            # j th coordinate of data
            data_column = np.array([d[j] for d in data_points])
            dotted = np.dot(hidden_row, data_column) / hidden_row_sum
            center_element.append(dotted)
        new_centers.append(np.array(center_element))
    
    return new_centers


def soft_kmeans(data_points, centers, steps, beta):
    # Main code
    counter = 0
    while counter < steps:
        # E-step
        hm = hidden_matrix(data_points, centers, beta)
        # M-step
        new_centers = update_centers(data_points, centers, hm)
        centers = new_centers
        counter += 1
    
    return centers


if __name__ == '__main__':
    with open("rosalind_ba8d.txt") as file:
        # n-number of data points
        # m-dimensional space
        k, m = file.readline().split(' ')
        k = int(k)
        m = int(m)

        # Stiffness parameter beta
        beta = file.readline()
        beta = float(beta)

        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_point = cleaned_line.split(' ')
            float_data = np.array([float(data) for data in data_point])
            data_list.append(float_data)

        # Initiate centers
        centers = data_list[:k]
        # Size of steps
        steps = 100
        
        # Soft k-means clustering
        final_centers = soft_kmeans(data_list, centers, steps, beta)

        # Print results in 3-decimal places
        for data_point in final_centers:
            print(' '.join(str(f"{a:.3f}") for a in data_point))
