import numpy as np
from game import BiMatrixGame

class StagHunt(BiMatrixGame):
     
    def __init__(self):
        super().__init__(np.ndarray([[1, 0],[2/3, 2/3]]), np.ndarray([[1, 2/3],[0, 2/3]]), ["S", "H"])
        
    