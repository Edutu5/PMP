import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

a0, b0 = 2, 8

n1, y1 = 20, 5
a1, b1 = a0 + y1, b0 + n1 - y1
prior = stats.beta(a0, b0)
post1 = stats.beta(a1, b1)

print("Posterior dupa primul lot: Beta(", a1, ",", b1, ")")
print("Media =", round(a1 / (a1 + b1), 4))

theta = np.linspace(0, 1, 500)
plt.plot(theta, prior.pdf(theta), label="a priori Beta(2, 8)")
plt.plot(theta, post1.pdf(theta), label="a posteriori Beta(7, 23)")
plt.xlabel("theta")
plt.legend()
plt.savefig("subiect3_a.png", dpi=110, bbox_inches="tight")
plt.show()

n2, y2 = 15, 3
a2, b2 = a1 + y2, b1 + n2 - y2
post2 = stats.beta(a2, b2)

print()
print("Posterior dupa ambele loturi: Beta(", a2, ",", b2, ")")
print("Media =", round(a2 / (a2 + b2), 4), " deviatia =", round(post2.std(), 4))

a3, b3 = a0 + y2, b0 + n2 - y2
post3 = stats.beta(a3, b3)

print()
print("Posterior numai din al doilea lot: Beta(", a3, ",", b3, ")")
print("Media =", round(a3 / (a3 + b3), 4), " deviatia =", round(post3.std(), 4))