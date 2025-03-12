import numpy as np
from .game import SymmetricBiMatrixGame

class SubsidyGame(SymmetricBiMatrixGame):
     
    def __init__(self):
        super().__init__(np.array([[12, 0],[11, 10]]), "Subsidy Game",["S_1", "S_2"])
        
    