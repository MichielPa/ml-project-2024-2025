import numpy as np
from .game import SymmetricBiMatrixGame

class PrisonnersDilemma(SymmetricBiMatrixGame):
     
    def __init__(self):
        super().__init__(np.array([[-2, -10],[-1, -5]]), "Prisonner's Dilemma", ["C", "D"])
        
    