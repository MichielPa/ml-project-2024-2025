import random
from matplotlib import pyplot as plt
from numpy import sqrt
from games import BiMatrixGame


class Policy:
    
    @classmethod
    def random(cls, actions: list[str]):
        values = [random.random() for _ in actions]
        total = sum(values)
        normalized_values = [v / total for v in values]
        return Policy({k: v for k, v in zip(actions, normalized_values)}) 
    
    def __init__(self, actions: dict[str, float]):
        self.actions = actions
        
    def play(self):
        return random.choices(list(self.actions.keys()), weights=self.actions.values())[0]

    
    def distance(self, other):
        assert len(self.actions.values()) == len(other.actions.values()), "Both policies should have the same amount of possible actions to be compared."
        return sqrt(sum([(val1 - val2)**2 for val1, val2 in zip(self.actions.values(), other.actions.values())]))

class LearningAlgorithm:

    def learn(self, action, action_opponent, reward):
        raise NotImplementedError()
    
    def copy():
        raise NotImplementedError()
    
    def reset(self, actions):
        raise NotImplementedError()
    
    def getPolicy(self):
        raise NotImplementedError()
    
    def play(self):
        return self.getPolicy().play()
    

class QLearningAlgorithm:
    
    def __init__(self, alpha, gamma):
        self.alpha = alpha
        self.gamma = gamma
        self.Q = None

    def learn(self, action, _, reward):
        # Qk +1 (xk , uk ) = Qk (xk , uk ) + αk * (rk + γ * max Qk(xk + 1, uk) − Qk(xk, uk))
        self.Q[action] = self.Q[action] + self.alpha * (reward + self.gamma * max(self.Q.values()) - self.Q[action])
    
    def reset(self, actions):
        self.Q = {a: random.random() for a in actions}
        self.Q_opponent = {a: random.random() for a in actions}
