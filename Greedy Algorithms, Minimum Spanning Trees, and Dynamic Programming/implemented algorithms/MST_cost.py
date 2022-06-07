from math import inf

def get_min(distance_list, l):
    
    min_dist = inf
    
    for k in range(l):
        temp_dist = distance_list[k][1]
        if  temp_dist < min_dist:
            min_dist = temp_dist
            min_index = distance_list[k][2]
            del_index = k
    
    distance_list.pop(del_index)
    return min_dist, min_index

def min_distance(points, n):
    
    distance = 0.0
    
    visited_points = []
    not_visited_points = [x for x in range(n)]
    distance_list = []
    min_index = 0
    
    while len(visited_points) != (n - 1):
        
        i = min_index
        visited_points.append(i)
        not_visited_points.remove(i)
    
        for j in not_visited_points:
             dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**(1/2)    
             distance_list.append([i,dist,j])  # add distance between nodes i and j
    
        min_dist, min_index = get_min(distance_list, len(distance_list))
        
        while min_index in visited_points:
	     min_dist, min_index = get_min(distance_list, len(distance_list))
        
        distance += min_dist
    
    return distance
    

