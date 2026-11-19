import numpy as np

rng = np.random.default_rng()

N = 100000
X = rng.integers(1, 7, N)
Y = rng.integers(1, 7, N)

A = X + Y >= 10                    # suma cel putin 10
B = X % 2 == 0                     # primul zar par
C = (X % 2 == 0) | (Y % 2 == 0)    # cel putin un zar par
D = X + Y == 8
E = (X % 2 == 0) & (Y % 2 == 0)    # ambele zaruri pare

# P(A | B) se estimeaza ca frecventa lui A in interiorul conditiei
print("1. P(S >= 10 | X par)          =", round(A[B].mean(), 4), " exact", round(2 / 9, 4))
print("2. P(S >= 10 | cel putin unul par) =", round(A[C].mean(), 4), " exact", round(5 / 27, 4))
print("3. P(ambele pare | S = 8)      =", round(E[D].mean(), 4), " exact 0.6")

# 4. independenta: comparam P(A si B) cu P(A) * P(B)
print("4. P(A si B) =", round((A & B).mean(), 4),
      " vs P(A)*P(B) =", round(A.mean() * B.mean(), 4))
print("   difera, deci A si B nu sunt independente")
