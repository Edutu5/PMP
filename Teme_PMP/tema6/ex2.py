import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 20.0     # clienti pe ora
ORA = 60.0        # minute
PLATA = 2.0       # media timpului de plata, minute
PRAG = 15.0
NR_SIMULARI = 20000
SAMANTA = 42

# a)
def simuleaza(alpha, rng):
    """Intoarce timpii totali (sosire -> primirea mancarii) pentru o ora."""
    n = rng.poisson(LAMBDA)                  # proces Poisson: intai cate sosiri,
    if n == 0:
        return np.array([])
    sosiri = np.sort(rng.uniform(0, ORA, n))  # apoi pozitiile lor, uniforme pe [0, 60]
    plata = rng.exponential(PLATA, n)
    gatit = rng.exponential(alpha, n)

    # Doua cozi FIFO in serie: casa si statia de gatit lucreaza in paralel, dar fiecare
    # serveste in ordinea sosirii, deci retinem doar cand se elibereaza fiecare.
    primire = np.zeros(n)
    liber_casa = liber_gatit = 0.0
    for i in range(n):
        liber_casa = max(sosiri[i], liber_casa) + plata[i]
        liber_gatit = max(liber_casa, liber_gatit) + gatit[i]
        primire[i] = liber_gatit
    return primire - sosiri

rng = np.random.default_rng(SAMANTA)
print("a) O ora cu alpha = 1:", np.round(simuleaza(1.0, rng)[:5], 2), "... (primii 5)")

# b)
def probabilitate(alpha, rng):
    """P(toti clientii din ora primesc mancarea in cel mult 15 minute)"""
    reusite = 0
    for _ in range(NR_SIMULARI):
        t = simuleaza(alpha, rng)
        if t.size == 0 or t.max() <= PRAG:
            reusite += 1
    return reusite / NR_SIMULARI

alphas = [0.0, 0.5, 1.0, 1.5, 2.0]
rng = np.random.default_rng(SAMANTA)
probabilitati = [probabilitate(a, rng) for a in alphas]

print()
print("b) alpha -> P(toti sub 15 min):")
for a, p in zip(alphas, probabilitati):
    print("  ", a, "->", round(p, 4))
print("   Chiar si la alpha = 0 ramane ~0.81, deci NU exista alpha care sa dea 95%.")
print("   Gatul de sticla e casa: sosiri la 3 min, plata 2 min, incarcare 2/3.")

plt.plot(alphas, probabilitati, marker="o")
plt.axhline(0.95, linestyle="--", color="red")
plt.xlabel("alpha (minute)")
plt.ylabel("P(toti sub 15 min)")
plt.show()

# c)
# Cerinta b) nu are solutie, deci raportam timpii pentru cateva valori ale lui alpha
print()
print("c) alpha -> timp mediu de la sosire la primirea mancarii:")
rng = np.random.default_rng(SAMANTA)
for a in [0.5, 1.0, 1.5, 2.0]:
    medii = [simuleaza(a, rng).mean() for _ in range(2000)]
    print("  ", a, "->", round(np.mean(medii), 2), "min")

# d)
print()
print("d) Simulari:", NR_SIMULARI, "pe valoare de alpha; samanta:", SAMANTA, ";")
print("   cautare prin baleierea unei grile (probabilitatea e descrescatoare in alpha).")
print("   Estimarile variaza intre rulari: eroarea Monte Carlo e ~sqrt(p(1-p)/N) < 0.004.")
