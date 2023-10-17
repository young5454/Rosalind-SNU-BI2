import numpy as np

# Distortion(Data,Centers) = (1/n) ∑all points DataPoint in Data d(DataPoint, Centers)2.

def euclidean(point1, point2):
    # Calculate Euclidean distance between two data points
    squared = np.sum(np.square(point1 - point2))
    distance = np.sqrt(squared)
    return distance


def distortion(data_points, centers):
    # Returns the mean squared distance from each data point to its nearest center
    n = len(data_points)
    cluster_distances = []
    for point in data_points:
        curr_distances = []
        for center in centers:
            curr_d = euclidean(point, center)
            curr_distances.append(curr_d)
        cluster_d = min(curr_distances)
        cluster_distances.append(cluster_d)
    
    summed = 0
    for cluster_d in cluster_distances:
        summed += cluster_d ** 2
    
    return summed / n


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
        
        centers = data_list[:partition-1]
        data_points = data_list[partition-1:]

        distorted = distortion(data_points, centers)
        print("%.3f" % distorted)
        # print(centers)
        # print(data_points)
        # centers = farthest_first_travel(data_list, k)
        # for data_point in centers:
        #     print(' '.join(str(a) for a in data_point))