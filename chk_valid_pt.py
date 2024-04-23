import pandas as pd
import csv
import numpy as np

df_train = pd.read_csv('valid.csv')
sorted_points = df_train.sort_values(by='z')

def find_special_points(sorted_points, z_less, z_greater):
    A = B = C = D = E = F = G = H = None
    if z_less is not None:
        points_z_less = sorted_points[sorted_points[:, 2] == z_less]
        if len(points_z_less) > 0:
            A = points_z_less[np.argmin(points_z_less[:, 0])]
            B = points_z_less[np.argmax(points_z_less[:, 0])]
            C = points_z_less[np.argmin(points_z_greater[:, 1])]  
            D = points_z_less[np.argmax(points_z_greater[:, 1])]

    if z_greater is not None:
        points_z_greater = sorted_points[sorted_points[:, 2] == z_greater]
        if len(points_z_greater) > 0:
            E = points_z_greater[np.argmin(points_z_less[:, 0])]
            F = points_z_greater[np.argmax(points_z_less[:, 0])]
            G = points_z_greater[np.argmin(points_z_greater[:, 1])]  
            H = points_z_greater[np.argmax(points_z_greater[:, 1])]  

    return A, B, C, D, E, F, G, H

def find_nearest_z(sorted_points, z):
    idx = np.searchsorted(sorted_points[:, 2], z, side='left')
    z_less = sorted_points[idx - 1, 2] if idx > 0 else None
    z_greater = sorted_points[idx, 2] if idx < len(sorted_points) else None
    return z_less, z_greater

def check_validity(sorted_points, P):
    z_less, z_greater = find_nearest_z(sorted_points, P[2])
    A, B, C, D, E, F, G, H = find_special_points(sorted_points, z_less, z_greater)
    X_min_final= min(A[0],E[0])
    X_max_final= max(B[0],F[0])
    Y_min_final= min(C[0],G[0])
    Y_max_final= max(D[0],H[0])
    if P[0]>= X_min_final and P[0]<= X_max_final and P[1]>= Y_min_final and P[1]<= Y_max_final:
        return "valid point"
    else:
        return "invalid point"