import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import betaln

a0, b0 = 2, 18       # priorul Beta(2, 18)
n, y = 50, 8         # componente testate si defecte

# a)
# Y | theta ~ Binomial(n, theta), deci P(Y=y|theta) = C(n,y) theta^y (1-theta)^(n-y)

# b)
# Priorul Beta are nucleul theta^(a-1)(1-theta)^(b-1); inmultit cu verosimilitatea,
# exponentii se aduna, deci posteriorul este Beta(a+y, b+n-y). Beta e conjugata Binomialei.
a, b = a0 + y, b0 + n - y
posterior = stats.beta(a, b)
prior = stats.beta(a0, b0)
print("b) posterior: Beta(", a, ",", b, ")")

# c)
print()
print("c) MLE =", round(y / n, 4),
      " MAP =", round((a - 1) / (a + b - 2), 4),
      " medie =", round(a / (a + b), 4))
print("   MLE foloseste doar datele; MAP si media includ si priorul, care le trage in jos")

# d)
theta = np.linspace(0, 1, 500)
plt.plot(theta, prior.pdf(theta), label="prior Beta(2, 18)")
plt.plot(theta, posterior.pdf(theta), label="posterior Beta(10, 60)")
plt.xlabel("theta")
plt.legend()
plt.show()
print()
print("d) Datele au mutat densitatea de la 0.10 spre 0.14 si au ingustat-o")

# e)
lo, hi = posterior.ppf([0.025, 0.975])     # interval central: 2.5% in fiecare coada
print()
print("e) Interval credibil central 95%: [", round(lo, 4), ",", round(hi, 4), "]")

# f)
print()
print("f) P(theta < 0.10 | y) =", round(posterior.cdf(0.10), 4))
print("   doar ~15% din masa posterioara e sub prag, deci datele nu sustin cerinta")

# g)
# P(X=0|y) = integrala (1-theta)^10 p(theta|y) dtheta = B(a, b+10) / B(a, b),
# calculata prin logaritmi ca sa evitam numere foarte mici
print()
print("g) P(X = 0 | y) =", round(np.exp(betaln(a, b + 10) - betaln(a, b)), 4))
