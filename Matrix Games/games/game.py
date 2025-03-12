

import numpy as np
import matplotlib.pyplot as plt

class BiMatrixGame:
    
    def __init__(self, player1_rewards: np.ndarray, player2_rewards: np.ndarray, name: str,  action_names: list[str] = None):
        self.player1_rewards = player1_rewards
        self.player2_rewards = player2_rewards
        assert self.player1_rewards.shape == self.player2_rewards.shape, "Reward matrices should have the same shape."
        assert self.player1_rewards.shape[0] == self.player1_rewards.shape[1], "Reward matrices should be square as players have the same available actions."
        
        self.name = name
        
        if action_names is None:
            self.action_names = [f"Action {i + 1}" for i in range(self.player1_rewards.shape[0])]
        else:
            self.action_names = action_names
            
        assert len(self.action_names) == self.player1_rewards.shape[0]
        
    
    def _replicator_equation(self, x, A, y, i):
        return x[i] * (((A @ y)[i]) - np.transpose(x) @ A @ y)
            
    def _replicator_equation_grid(self, X, Y, n):    
        
        DX = np.zeros_like(X)
        DY = np.zeros_like(X)
        
        for i in range(n):
            for j in range(n):
                p1 = np.array([X[i, j], 1 - X[i, j]]).transpose()
                p2 = np.array([Y[i, j], 1 - Y[i, j]]).transpose()
                DX[i, j] = self._replicator_equation(p1, self.player1_rewards, p2, 0)
                DY[i, j] = self._replicator_equation(p2, self.player2_rewards, p1, 0)
        
        return DX, DY
                
    def quiver(self, ax = None):
        
        if ax is None:
            fig, ax = plt.subplots()
            show_plot = True
        else:
            show_plot = False

        n = 15
        x = np.linspace(0, 1, n)
        y = np.linspace(0, 1, n)
        X, Y = np.meshgrid(x, y)
        
        DX, DY = self._replicator_equation_grid(X, Y, n)
        
        ax.quiver(X, Y, DX, DY)
        
        ax.set_title(self.name)
        ax.set_xlabel(f"Probability of player 1 playing {self.action_names[0]}")
        ax.set_ylabel(f"Probability of player 2 playing {self.action_names[0]}")
        
        if show_plot:
            fig.show()
    

class SymmetricBiMatrixGame(BiMatrixGame):
    
    def __init__(self, rewards: np.ndarray, name: str, action_names=None):
        super().__init__(rewards, rewards, name, action_names)
