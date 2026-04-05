import numpy as np
from numpy.typing import NDArray
from typing import List


class Solution:
    def forward(self, x: NDArray[np.float64], w: List[NDArray[np.float64]], b: List[NDArray[np.float64]]) -> NDArray[np.float64]:
        # x: 1D input array
        # weights: list of 2D weight matrices
        # biases: list of 1D bias vectors
        # Apply ReLU after each hidden layer, no activation on output layer
        # return np.round(your_answer, 5)
        pass

        for layer in range(len(b)-1):
            z = x@w[layer] + b[layer]
            output = np.maximum(0,z)
        
        final = output@w[-1]+ b[-1]

        return np.round(final, 5)


