#generate 10k random variable and compute variance,std evaluation,iqr,range
#with built and without numpy and compare the results


import random
import numpy as np

# Generate 10,000 random numbers
random.seed(42)
data = [random.randint(1, 1000) for i in range(10000)]

print("Number of elements:", len(data))
print("First 10 values:", data[:10])

# Mean
mean = sum(data) / len(data)

# Variance (Population variance)
variance = sum((x - mean) ** 2 for x in data) / len(data)

# Standard Deviation
std = variance ** 0.5

# Sort data
sorted_data = sorted(data)

# Range
data_range = max(data) - min(data)

# IQR
n = len(sorted_data)

Q1 = sorted_data[n // 4]
Q3 = sorted_data[(3 * n) // 4]

IQR = Q3 - Q1

print("WITHOUT NUMPY")
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std)
print("Range:", data_range)
print("IQR:", IQR)

# Convert list into NumPy array
arr = np.array(data)

# Mean
np_mean = np.mean(arr)

# Variance
np_variance = np.var(arr)

# Standard Deviation
np_std = np.std(arr)

# Range
np_range = np.max(arr) - np.min(arr)

# IQR
Q1 = np.percentile(arr, 25)
Q3 = np.percentile(arr, 75)

np_IQR = Q3 - Q1

print("WITH NUMPY")
print("Mean:", np_mean)
print("Variance:", np_variance)
print("Standard Deviation:", np_std)
print("Range:", np_range)
print("IQR:", np_IQR)

print("COMPARISON")

print("Mean:", mean, np_mean)
print("Variance:", variance, np_variance)
print("Standard Deviation:", std, np_std)
print("Range:", data_range, np_range)
print("IQR:", IQR, np_IQR)