import numpy as np

stari = ["D", "M", "U"]          # dificil, mediu, usor
note = ["FB", "B", "S", "NS"]

# a)
pi = np.array([1 / 3, 1 / 3, 1 / 3])
# A[D][D] = 0: dupa un test dificil urmeaza doar mediu sau usor
A = np.array([[0.00, 0.50, 0.50],
              [0.50, 0.25, 0.25],
              [0.50, 0.25, 0.25]])
B = np.array([[0.10, 0.20, 0.40, 0.30],
              [0.15, 0.25, 0.50, 0.10],
              [0.20, 0.30, 0.40, 0.10]])

print("suma pi:", pi.sum(), " randuri A:", A.sum(1), " randuri B:", B.sum(1))

secventa = ["FB", "FB", "S", "B", "B", "S", "B", "B", "NS", "B", "B", "S"]
o = [note.index(x) for x in secventa]
T, N = len(o), len(stari)

# b)
# delta_t(j) = probabilitatea comuna maxima a unei secvente care se termina in j la t
delta = np.zeros((T, N))
psi = np.zeros((T, N), dtype=int)
delta[0] = pi * B[:, o[0]]
print()
print("b) delta_1 =", np.round(delta[0], 6))

# c)
# psi retine din ce stare s-a venit: delta spune cat de bun e traseul, psi spune care e
for t in range(1, T):
    for j in range(N):
        candidati = delta[t - 1] * A[:, j]
        psi[t, j] = np.argmax(candidati)
        delta[t, j] = candidati[psi[t, j]] * B[j, o[t]]

# d)
print()
print("d) delta_2 =", np.round(delta[1], 6))
# verificare manuala pentru delta_2(D): max(0.0333*0, 0.05*0.5, 0.0667*0.5) * 0.1
print("   verificare delta_2(D):", round(max(delta[0] * A[:, 0]) * B[0, o[1]], 6))

# e)
traseu = [int(np.argmax(delta[-1]))]
for t in range(T - 1, 0, -1):
    traseu.append(psi[t, traseu[-1]])
traseu = traseu[::-1]

print()
print("e)", [stari[s] for s in traseu])
print("   max P(x, o) =", delta[-1].max())
# La primul test exista egalitate, deci secventa care incepe cu U e la fel de buna

# f)
print()
print("f) Viterbi foloseste max, nu suma, deci compara trasee intregi, nu momente")
print("   separate. Scorul de mai sus e P(x*, o), nu P(x* | o).")
