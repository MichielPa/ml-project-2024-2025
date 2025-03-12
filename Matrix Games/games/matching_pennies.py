import numpy as np
from .game import BiMatrixGame

class MatchingPennies(BiMatrixGame):
     
    def __init__(self):
        super().__init__(np.array([[0, 1],[1, 0]]), np.array([[1, 0],[0, 1]]), "Matching Pennies", ["H", "T"])
        
    