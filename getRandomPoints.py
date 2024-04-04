import numpy as np


def get_random_points(I, alpha):

    h,w = I.shape[:2]
    points = []
    for j in range(alpha):
        y = int(np.clip(np.random.normal(h/2.,h/5.),0,h-1))
        x = int(np.clip(np.random.normal(w/2.,w/5.),0,w-1))
        point = (x,y)
        points.append(point)

    # -----fill in your implementation here --------


    # ----------------------------------------------
    points=np.array(points)

    return points