import numpy as np

# FarthestFirstTraversal(Data, k) 
#  Centers ← the set consisting of a single randomly chosen point from Data
#   while |Centers| < k
#    DataPoint ← the point in Data maximizing d(DataPoint, Centers) 
#    add DataPoint to Centers 
#  return Centers 

def euclidean(point1, point2):
    # Calculate Euclidean distance between two data points
    squared = np.sum(np.square(point1 - point2))
    distance = np.sqrt(squared)
    return distance


def get_closest_center_d(data_points, centers):
    # Returns the distance to the closest center point
    cluster_distances = []
    for point in data_points:
        curr_distances = []
        for center in centers:
            curr_d = euclidean(point, center)
            curr_distances.append(curr_d)
        cluster_d = min(curr_distances)
        cluster_distances.append(cluster_d)
    max_d = max(cluster_distances)

    max_index = cluster_distances.index(max_d)

    return max_d, max_index


def farthest_first_travel(data_list, k):
    rand_data = data_list[0]
    centers = [rand_data]

    while len(centers) < k:
        max_d, new_center_index = get_closest_center_d(data_list, centers)
        new_center = data_list[new_center_index]
        centers.append(new_center)

    return centers


if __name__ == '__main__':
    with open("rosalind_ba8a.txt") as file:
        # k-number of data points
        # m-dimensional space
        k, m = file.readline().split(' ')
        k = int(k)
        m = int(m)

        data_list = []
        for line in file:
            cleaned_line = line.strip()
            data_point = cleaned_line.split(' ')
            float_data = np.array([float(data) for data in data_point])
            data_list.append(float_data)
        
        # print(data_list)
        centers = farthest_first_travel(data_list, k)
        for data_point in centers:
            print(' '.join(str(a) for a in data_point))