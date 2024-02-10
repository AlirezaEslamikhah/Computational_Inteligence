### euclidean distance 

import numpy as np
point_x = [1,0,0,0]
point_unit =  [0.1, 0.2, 0.3, 0.9]

def euclidean_distance(point_x, point_unit):
    distance = 0
    for i in range(4):
        distance += ( point_unit[i] - point_x[i])**2
        # print (point_unit[i] -  point_x[i])
    return np.sqrt(distance)

# 
#print(euclidean_distance(point_x, point_unit))
print("the distance between point_x and point_unit is: ", euclidean_distance(point_x, point_unit))


# update weights 
import numpy as np

def update_weights(current_weight, target_vector, alpha):
    current_weight = np.array(current_weight)
    target_vector = np.array(target_vector)
    
    new_weight = current_weight + alpha * (target_vector - current_weight)
    
    return new_weight.tolist()

# Example usage:
current_weight = [0.1, 0.2, 0.3, 0.9]
target_vector = point_x
alpha = 0.5

new_weight = update_weights(current_weight, target_vector, alpha)
print(f"The updated weight is {new_weight}")
