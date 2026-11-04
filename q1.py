#generate 10k random sample and 
#compute mean,median and mode (with numpy and without numpy)
#compare the results 

import numpy as np

n=10000
data = np.random.rand(n)

mean1=np.mean(data)
median1=np.median(data)
mode1=np.argmax(np.bincount(data.astype(int)))

mean2=sum(data)/len(data)
median2=sorted(data)[len(data)//2]
mode2=max(set(data), key=data.count)

print('Values with numpy:')
print('Mean:', mean1)
print('Median:', median1)
print('Mode:', mode1)

print('Values without numpy:')
print('Mean:', mean2)
print('Median:', median2)
print('Mode:', mode2)

