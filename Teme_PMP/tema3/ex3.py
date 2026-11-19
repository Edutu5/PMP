import numpy as np
from scipy.stats import binom
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

rng = np.random.default_rng()

P_J0 = 0.5        # moneda lui J0 este normala
P_J1 = 4 / 7      # moneda lui J1 este masluita

# a)
castiguri = [0, 0]
for _ in range(10000):
    incepe = rng.integers(0, 2)
    n = rng.integers(1, 7)                       # zarul jucatorului din prima runda
    celalalt = 1 - incepe
    p = P_J1 if celalalt == 1 else P_J0
    m = rng.binomial(2 * n, p)                   # steme in 2n aruncari
    castigator = incepe if n >= m else celalalt  # primul castiga daca n >= m
    castiguri[castigator] += 1

print("a) J0:", castiguri[0] / 10000, " J1:", castiguri[1] / 10000)

# b)
# S = cine incepe, N = zarul, M = numarul de steme. M depinde de N (cate aruncari)
# si de S (a cui moneda se foloseste).
model = DiscreteBayesianNetwork([("S", "M"), ("N", "M")])

cpd_s = TabularCPD("S", 2, [[0.5], [0.5]])
cpd_n = TabularCPD("N", 6, [[1 / 6]] * 6)

# P(M | S, N) este binomiala; coloanele in ordinea (S,N) = (0,1)..(0,6), (1,1)..(1,6)
coloane = [binom.pmf(np.arange(13), 2 * n, P_J1 if s == 0 else P_J0)
           for s in (0, 1) for n in range(1, 7)]
cpd_m = TabularCPD("M", 13, np.array(coloane).T, evidence=["S", "N"], evidence_card=[2, 6])

model.add_cpds(cpd_s, cpd_n, cpd_m)
print()
print("b) Model valid:", model.check_model())

# c)
print()
print("c) P(S | M=1):")
print(VariableElimination(model).query(["S"], evidence={"M": 1}))
