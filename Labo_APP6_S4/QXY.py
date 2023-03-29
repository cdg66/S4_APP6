import numpy as np

def convert_to_QXY(array,X,Y):
    h = array * np.power(2, Y)
    hround = np.round(h)
    return hround



def convert_from_QXY(array,X,Y):
    return array / np.power(2, Y)