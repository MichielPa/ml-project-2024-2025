from .learning_algorithm import Policy, QLearningAlgorithm

class EpsilonGreedy(QLearningAlgorithm):
    
    def __init__(self, alpha, gamma, epsilon):
        self.epsilon = epsilon
        super().__init__(alpha, gamma)
        
    def copy(self):
        return EpsilonGreedy(self.alpha, self.gamma, self.epsilon)
    
    def getPolicy(self):
        max_val = max(self.Q.values())
        best = list(filter(lambda x: self.Q[x] == max_val, self.Q))
        other = list(filter(lambda x: x not in best, self.Q))
        
        # print({b: (1-self.epsilon)/len(best) for b in best} | {o: self.epsilon/len(other) for o in other})
        
        return Policy(
            {b: (1-self.epsilon)/len(best) for b in best} | {o: self.epsilon/len(other) for o in other}
        )