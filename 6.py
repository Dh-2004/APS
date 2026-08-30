import numpy as np

n = 10000

coin = np.random.choice(['H', 'T'], size=n)
die = np.random.randint(1, 7, size=n)

A = coin == 'H'
B = die % 2 == 0

P_A = np.mean(A)
P_B = np.mean(B)

P_A_intersection_B = np.mean(A & B)

print("P(A) [Head]:", P_A)
print("P(B) [Even]:", P_B)
print("P(A ∩ B):", P_A_intersection_B)
print("P(A) × P(B):", P_A * P_B)


print("Therefore P(A ∩ B) i.e ",P_A_intersection_B, "=", P_A * P_B)