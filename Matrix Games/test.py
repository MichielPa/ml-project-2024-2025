from games import *

if __name__ == "__main__":
    
    
    fig, axs = plt.subplots(2, 2)
    
    StagHunt().quiver(axs[0, 0])
    SubsidyGame().quiver(axs[0, 1])
    MatchingPennies().quiver(axs[1, 0])
    PrisonnersDilemma().quiver(axs[1, 1])


    plt.show()