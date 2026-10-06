import numpy as np
import matplotlib.pyplot as plt
import arviz as az

rng = np.random.default_rng()

lam = np.array([3, 6, 4])
p = lam / lam.sum()

frizer = rng.choice(3, size=10000, p=p)
X = rng.exponential(scale=1 / lam[frizer])

print("Media lui X =", round(X.mean(), 4))
print("Deviatia standard =", round(X.std(), 4))

grila, densitate, _ = az.kde(X)
plt.plot(grila, densitate)
plt.title("Densitatea timpului de servire X")
plt.xlabel("timp (ore)")
plt.show()