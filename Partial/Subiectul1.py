import numpy as np
from hmmlearn import hmm

culori = ["red", "green", "blue"]

pi = np.array([0.25, 0.25, 0.25, 0.25])

B = np.array([[0.7, 0.2, 0.1],
              [0.2, 0.6, 0.2],
              [0.1, 0.3, 0.6],
              [0.5, 0.2, 0.3]])

secventa = ["red", "green", "blue", "blue", "red"]
o = np.array([[culori.index(x)] for x in secventa])

def viterbi(A):
    model = hmm.CategoricalHMM(n_components=4)
    model.startprob_ = pi
    model.transmat_ = A
    model.emissionprob_ = B
    logprob, traseu = model.decode(o, algorithm="viterbi")
    return [int(s) + 1 for s in traseu], np.exp(logprob)

A = np.array([[0.2, 0.4, 0.0, 0.4],
              [0.4, 0.2, 0.4, 0.0],
              [0.0, 0.4, 0.2, 0.4],
              [0.4, 0.0, 0.4, 0.2]])

traseu_a, p_a = viterbi(A)
print("Secventa de camere:", traseu_a)
print("P(camere, observatii) =", p_a)

A2 = np.array([[0.0, 0.5, 0.0, 0.5],
               [0.5, 0.0, 0.5, 0.0],
               [0.0, 0.5, 0.0, 0.5],
               [0.5, 0.0, 0.5, 0.0]])

traseu_b, p_b = viterbi(A2)
print()
print("Secventa de camere:", traseu_b)
print("P(camere, observatii) =", p_b)
print()
print("Identice:", traseu_a == traseu_b)
print("Raport probabilitati:", round(p_b / p_a, 4))