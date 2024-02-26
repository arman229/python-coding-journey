from nptyping import NDArray
import numpy as np

def elements_in_array(arr1: NDArray, arr2: NDArray) -> NDArray:
    return np.in1d(arr1, arr2)