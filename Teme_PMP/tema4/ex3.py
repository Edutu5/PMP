import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pyagrum as gum

# a)
original = np.zeros((5, 5), dtype=int)
original[1:4, 1:4] = 1               # patrat alb 3x3 pe fond negru
print("Original:")
print(original)

plt.imshow(original, cmap="gray", vmin=0, vmax=1)   # vmin/vmax fixeaza 0=negru, 1=alb
plt.show()

# b)
np.random.seed(10)                   # samanta fixa, pentru reproductibilitate
inversat = np.random.rand(5, 5) < 0.1
y = np.where(inversat, 1 - original, original)
print()
print("Observat y (", inversat.sum(), "pixeli inversati):")
print(y)

fig, ax = plt.subplots(1, 2)
ax[0].imshow(original, cmap="gray", vmin=0, vmax=1)
ax[1].imshow(y, cmap="gray", vmin=0, vmax=1)
plt.show()

# c)
grila = nx.grid_2d_graph(5, 5)       # un nod pe pixel, muchii catre cei 4 vecini directi

def energie(x, lam):
    """lambda * fidelitate fata de y + netezime intre vecini"""
    return lam * np.sum((x - y) ** 2) + sum((x[a] - x[b]) ** 2 for a, b in grila.edges())

print()
print("Graf MRF:", grila.number_of_nodes(), "noduri,", grila.number_of_edges(), "muchii")
print("E(y; y) =", energie(y, 1.0), " E(original; y) =", energie(original, 1.0))

pozitii = {(i, j): (j, -i) for i, j in grila.nodes()}
nx.draw(grila, pos=pozitii, node_size=400, node_color="lightgray")
plt.show()

# d)
# Factorii in pyAgrum: 25 unari + 40 perechi, phi = exp(-energie locala)
mrf = gum.MarkovRandomField()
for (i, j) in grila.nodes():
    mrf.add(gum.LabelizedVariable("x_%d_%d" % (i, j), "", 2))

for (i, j) in grila.nodes():
    nume = "x_%d_%d" % (i, j)
    mrf.addFactor([nume])
    for v in (0, 1):
        mrf.factor({nume})[{nume: v}] = np.exp(-1.0 * (v - y[i, j]) ** 2)

for a, b in grila.edges():
    na, nb = "x_%d_%d" % a, "x_%d_%d" % b
    mrf.addFactor([na, nb])
    for va in (0, 1):
        for vb in (0, 1):
            mrf.factor({na, nb})[{na: va, nb: vb}] = np.exp(-((va - vb) ** 2))
print()
print(mrf)

# ICM: optimizam un pixel o data, pastrand restul fix (poate gasi doar un minim local)
def energie_locala(x, i, j, v, lam):
    e = lam * (v - y[i, j]) ** 2
    for vecin in grila.neighbors((i, j)):
        e += (v - x[vecin]) ** 2
    return e

def icm(lam):
    x = y.copy()                     # pornim din imaginea observata
    schimbat = True
    while schimbat:
        schimbat = False
        for (i, j) in grila.nodes():
            bun = int(np.argmin([energie_locala(x, i, j, v, lam) for v in (0, 1)]))
            if bun != x[i, j]:
                x[i, j] = bun
                schimbat = True
    return x

x_map = icm(1.0)
print()
print("MAP cu lambda = 1 (ICM):")
print(x_map)
print("E(x*; y) =", energie(x_map, 1.0), " pixeli gresiti:", int(np.sum(x_map != original)))

# e)
print()
for lam in [0.3, 1.0, 3.0]:
    x = icm(lam)
    print("lambda =", lam, " E =", round(energie(x, lam), 2),
          " pixeli gresiti:", int(np.sum(x != original)))

fig, ax = plt.subplots(1, 3)
for k, lam in enumerate([0.3, 1.0, 3.0]):
    ax[k].imshow(icm(lam), cmap="gray", vmin=0, vmax=1)
    ax[k].set_title("lambda = " + str(lam))
plt.show()

print()
print("lambda mic -> castiga netezirea: pixelul cedeaza vecinilor.")
print("lambda mare -> castiga fidelitatea: pixelul pastreaza ce s-a observat.")
