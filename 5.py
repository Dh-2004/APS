import numpy as np

A = {2, 4, 6}
B = {4, 5, 6}

P_A = len(A) / 6
P_B = len(B) / 6

intersection = A & B
union = A | B

P_intersection = len(intersection) / 6
P_union = len(union) / 6

print("A =", A)
print("B =", B)
print("A ∩ B =", intersection)
print("A U B =", union)

print("\nP(A):", P_A)
print("P(B):", P_B)
print("P(A ∩ B):", P_intersection)
print("P(A U B):", P_union)
print("Therefore P(A U B) =", P_A + P_B - P_intersection)