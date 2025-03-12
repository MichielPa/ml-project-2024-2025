import numpy as np
from .game import SymmetricBiMatrixGame

class StagHunt(SymmetricBiMatrixGame):
     
    def __init__(self):
        super().__init__(np.array([[1, 0],[2/3, 2/3]]), "Stag Hunt",["S", "H"])
        
    