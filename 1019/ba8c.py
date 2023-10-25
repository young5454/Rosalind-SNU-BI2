import numpy as np
from ba8a import euclidean

# The Lloyd algorithm is one of the most popular clustering heuristics for the k-Means Clustering Problem. 
# It first chooses k arbitrary points Centers from Data as centers and then iteratively performs the following two steps:

# Centers to Clusters 
# Clusters to Centers
def get_gravity(data_points):
    n = len(data_points)
    summed = np.sum(data_points, axis=0)
    gravity = summed / n
    return gravity


def kmeans(data_points, k):
    # Initialize cluster centers
    centers = data_points[:k]

    flag = True
    previous_points = None

    while flag:
        # Reset current_points at the start of each iteration
        current_points = [[] for i in range(k)]

        # Centers to Clusters
        for point in data_points:
            curr_distances = []
            for center in centers:
                curr_d = euclidean(point, center)
                curr_distances.append(curr_d)
            cluster_d = min(curr_distances)
            cluster_index = curr_distances.index(cluster_d)
            current_points[cluster_index].append(point)

        # Check if current_points are the same as previous_points
        if current_points == previous_points:
            flag = False
        else:
            previous_points = current_points
            
        # Update centers
        new_centers = [get_gravity(cluster) for cluster in current_points]
        centers = new_centers

    return centers


if __name__ == '__main__':
    with open("rosalind_ba8c.txt") as file:
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
        
        centers = kmeans(data_list, k)
        for data_point in centers:
            print(' '.join(str(f"{a:.3f}") for a in data_point))


## 102423 수업 코드
# def distance(a, b):
#     return ((a - b) ** 2).sum() ** .5