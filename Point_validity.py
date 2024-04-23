import numpy as np 
import pandas as pd 
import csv

Segreggated_points = []
df_train = pd.read_csv('valid.csv')
points = df_train.to_numpy()

list_all =[]
z_old = 0
z_same = []

for i in range(0,len(points)):

    z_value = points[i][2]
    values_corresponding_to_same_Z = []
    
    if i == 0:
        pass
    if z_value == z_old:
        pass
    else:
        values_corresponding_to_same_Z = []
        z_same.append(z_value)
        for count in range(len(points)):
            if points[count][2] == z_value:
                values_corresponding_to_same_Z.append(points[count])
                z_old = z_value

    if values_corresponding_to_same_Z == []:
        pass
    else:
        Segreggated_points.append(values_corresponding_to_same_Z)

def closest(check_list, Z):
     
    check_list = np.asarray(check_list)
    idx = (np.abs(check_list - Z)).argmin()
    
    return idx

def point_check(Points):

    '''Points -> List of points which should be verified if they are valid'''

    Valid_points = []
    check_list = z_same
    
    for count in range(len(Points)):
        norm = np.linalg.norm([Points[count][0],Points[count][1],0])
        Z_value = round(Points[count][2])
        
        index = closest(check_list,Z_value)
        # if Z_value >= 0:
        #     index = Z_value + 200 - 1
        # else:
        #     index = -Z_value - 1  

        plane = Segreggated_points[index]
        I_C = np.linalg.norm([plane[0][0],plane[0][1],0])
        O_C = np.linalg.norm([plane[-1][0],plane[-1][1],0])

        if norm >= I_C and norm <= O_C:
            Valid_points.append(Points[count])
        else:
            pass

    return Valid_points