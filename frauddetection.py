import numpy as np

p=0.04
n=50
hours=20000

bino=np.random.binomial(n=n,p=p,size=hours)

mean_flagged = np.mean(bino)

variance_flagged = np.var(bino)



print("Mean =", mean_flagged)
print("Variance =", variance_flagged)
