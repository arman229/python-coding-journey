import numpy as np
from typing import Any
from nptyping import NDArray, Shape, UInt64
a : NDArray[Shape["Size, Size"], Any] = np.array([[1, 2, 3],[4, 5, 6]])
b : NDArray[Shape["*, *"], Any] = np.array([[1, 2, 3],[4, 5, 6]])
print(a)
print(b)