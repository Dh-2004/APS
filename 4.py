import numpy as np
n = 10000

rolls = np.random.randint(1, 7, size=n)

A = rolls == 1
B = rolls == 6

P_A = np.mean(A)
P_B = np.mean(B)

P_A_U_B = np.mean(A | B)

print("P(A):", P_A)
print("P(B):", P_B)
print("P(A) + P(B):", P_A + P_B)
print("P(A U B):", P_A_U_B)
print("Therefore: P(A)+(B) = P(A U B) = ",P_A_U_B)