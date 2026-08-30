import numpy as np
n = 6000

rolls = np.random.randint(1, 7, size=n)

for outcome in range(1, 7):
    frequency = np.sum(rolls == outcome)
    probability = frequency / n
    
    print("\n Outcome: ", outcome, "\n Frequency: ", frequency, "\nExp Probability: ", probability)