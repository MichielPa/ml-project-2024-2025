

import numpy as np
import matplotlib.pyplot as plt

class BiMatrixGame:
    
    def __init__(self, player1_rewards: np.ndarray, player2_rewards: np.ndarray, action_names = None):
        self.player1_rewards = player1_rewards
        self.player2_rewards = player2_rewards
        assert self.player1_rewards.shape == self.player2_rewards.shape, "Reward matrices should have the same shape."
        assert self.player1_rewards.shape[0] == self.player1_rewards.shape[1], "Reward matrices should be square as players have the same available actions."
        
        if action_names is None:
            self.action_names = [f"Action {i + 1}" for i in self.player1_rewards.shape[0]]
        else:
            self.action_names = action_names
            
        assert len(self.action_names) == self.player1_rewards.shape[0]
        
    
    def _replicator_equation(self, X, Y):
        
        dx = np.zeros
        
        for i in X:
            for j in Y:
                ...
                
    def quiver(self):
        n = 10
        X, Y = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, n))
        
        print(X)
        
        #dx = X * (self.player1_rewards)
        
        # fig, ax = plt.subplots([X, Y])
        
        
    
class StagHunt(BiMatrixGame):
    
    
    def __init__(self):
        super().__init__(np.ndarray([[1, 0],[2/3, 2/3]]), np.ndarray([[1, 2/3],[0, 2/3]]), ["S", "H"])
        
        
