import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

# a) N - Geom(p): asteptam primul succes (nimerim stema) in incercari independente
#    P(N = n) = (1-p)^(n-1) * p,  n >= 1; E[N] = 1/p,  Var(N) = (1-p)/p^2

def joaca(p):
    N = 0
    S = 0.0
    while True:
        N += 1
        if rng.random() < p:
            S += rng.integers(1, 7) - 3
            return N, S
        else:
            S -= 0.5

# b)
N, S = joaca(0.5)
print("Un joc: N = ",N, "; S = ",S)

#c), d)
for p in [0.5, 0.3, 0.7]:
    rezultate = [joaca(p) for i in range(10000)]
    S_toate = np.array([s for n, s in rezultate])

    print("p =", p, "-> media lui S =", round(S_toate.mean(), 3))

    plt.hist(S_toate, bins=30, density=True)
    plt.title(f"Distributia lui S pentru p = {p}")
    plt.xlabel("S ($)")
    plt.show()