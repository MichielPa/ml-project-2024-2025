from games import *
from learning_algorithms import *
from learner import *
if __name__ == "__main__":
    
    
    """fig, axs = plt.subplots(2, 2)
    
    StagHunt().quiver(axs[0, 0])
    SubsidyGame().quiver(axs[0, 1])
    MatchingPennies().quiver(axs[1, 0])
    PrisonnersDilemma().quiver(axs[1, 1])"""
    
    
    learner = Learner(PrisonnersDilemma(), Boltzmann(0.01, 0.5, 10))
    
    learner.learn(1000000, 0.000001) 
    
    learner.plotTrace()
    
    input()