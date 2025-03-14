from numpy import exp
from .learning_algorithm import Policy, QLearningAlgorithm

class Boltzmann(QLearningAlgorithm):
    
    def __init__(self, alpha, gamma, t):
        self.t = t
        super().__init__(alpha, gamma)
    
    def copy(self):
        return Boltzmann(self.alpha, self.gamma, self.t)

    
    def getPolicy(self):
        
        terms = {a: exp(self.Q[a]) / self.t for a in self.Q.keys()}
        tot = sum(terms.values())
        
        return Policy({a: terms[a]/tot for a in self.Q.keys()})