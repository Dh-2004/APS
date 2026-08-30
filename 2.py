import numpy as np
trial_sizes = [10, 100, 1000, 10000]


for n in trial_sizes:
    toss = np.random.choice(['H', 'T'], size=n)
    
    head = np.sum(toss == 'H')
    tail = np.sum(toss == 'T')
    
    p_head = head / n
    p_tail = tail / n
    
    print("\nNumber of trials:", n)
    print("Heads:", head)
    print("Tails:", tail)
    print("P(Head):", p_head)
    print("P(Tail):", p_tail)