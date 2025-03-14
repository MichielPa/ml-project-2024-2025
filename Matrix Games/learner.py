from matplotlib import pyplot as plt
from learning_algorithms import Policy, LearningAlgorithm
from games import BiMatrixGame

class Learner:
    
    def __init__(self, game: BiMatrixGame, player1: LearningAlgorithm, player2: LearningAlgorithm = None):
        self.game = game
        self.player1 = player1
        if player2 is None:
            self.player2 = player1.copy()
        else:
            self.player2 = player2
        self.reset()
        
    def reset(self):
        self.player1.reset(self.game.action_names)
        self.player2.reset(self.game.action_names)
        self.trace = []
            
    def learn(self, maxIterations=50, minChange=0.05) -> Policy:
        self.reset()
        while len(self.trace) < maxIterations:
            policy1 = self.player1.getPolicy()
            policy2 = self.player2.getPolicy()
            
            self.trace.append((policy1, policy2))
            
            action1 = policy1.play()
            action2 = policy2.play()
            
            reward1, reward2 = self.game.getReward(action1, action2)
            
            print(reward1, reward2)
            
            self.player1.learn(action1, action2, reward1)
            self.player2.learn(action2, action1, reward2)
            
            print(self.player1.getPolicy().actions)
    
            if len(self.trace) >= 2 and self.trace[-1][0].distance(self.trace[-2][0]) < minChange:
                break
            
        self.trace.append((self.player1.getPolicy(), self.player2.getPolicy()))
    
    def plotTrace(self, ax=None):
        if ax is None:
            fig, ax = plt.subplots()
            show_plot = True
        else:
            show_plot = False
            
        self.game.quiver(ax)
        
        x = [p1.actions[self.game.action_names[0]] for (p1, _) in self.trace]
        y = [p2.actions[self.game.action_names[0]] for (_, p2) in self.trace]
        
        # Plot the trace
        plt.plot(x, y, marker='o', linestyle='-', color='b', label='Trace Path')

        # Adding arrows to indicate direction
        for i in range(len(x)-1):
            plt.annotate("", xy=(x[i+1], y[i+1]), xytext=(x[i], y[i]),
                        arrowprops=dict(arrowstyle="->", color='r'))
        
        if show_plot:
            fig.show()
