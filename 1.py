import numpy as np

n = 100
tosses = np.random.choice(['H', 'T'], size=n)

head = np.sum(tosses == 'H')
tail = np.sum(tosses == 'T')

prob_head = head / n
prob_tail = tail / n

print("Number of Heads:", head)
print("Number of Tails:", tail)
print("Experimental Probability of Head:", prob_head)
print("Experimental Probability of Tail:", prob_tail)