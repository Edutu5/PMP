import networkx as nx
import matplotlib.pyplot as plt
import pyagrum as gum
from pyagrum.markov_random_field import ShaferShenoyMRFInference

statii = ["S1", "S2", "S3", "S4", "S5"]
muchii = [("S1", "S2"), ("S2", "S3"), ("S2", "S4"), ("S4", "S5")]
stari = ["Soare", "Ploaie", "Nori"]

# a)
graf = nx.Graph()                    # graf neorientat: muchiile nu au sens
graf.add_nodes_from(statii)
graf.add_edges_from(muchii)

for s in statii:
    print("N(" + s + ") =", sorted(graf.neighbors(s)))
print("Arbore (conex si fara cicluri):", nx.is_tree(graf))

pozitii = nx.circular_layout(graf)
nx.draw(graf, pos=pozitii, with_labels=True, node_size=2000, alpha=0.5)
plt.show()

# b)
p = {"Soare": 0.5, "Ploaie": 0.3, "Nori": 0.2}
# Psi nu e simetric, deci fixam conventia: prima cheie = prima statie a muchiei
Psi = {"Soare":  {"Soare": 0.7, "Ploaie": 0.2, "Nori": 0.1},
       "Ploaie": {"Soare": 0.2, "Ploaie": 0.6, "Nori": 0.2},
       "Nori":   {"Soare": 0.1, "Ploaie": 0.3, "Nori": 0.6}}

mrf = gum.MarkovRandomField()
for s in statii:
    mrf.add(gum.LabelizedVariable(s, "", stari))

for s in statii:                     # cate un factor unar pe statie
    mrf.addFactor([s])
    for v in stari:
        mrf.factor({s})[{s: v}] = p[v]

for i, j in muchii:                  # cate un factor pereche pe muchie
    mrf.addFactor([i, j])
    for vi in stari:
        for vj in stari:
            mrf.factor({i, j})[{i: vi, j: vj}] = Psi[vi][vj]

print()
print(mrf)

# c)
print()
print("P(s1..sn) = (1/Z) * prod_i phi_i(si) * prod_(i,j) phi_ij(si,sj)")
nx.draw(graf, pos=pozitii, with_labels=True, node_size=2000, alpha=0.5)
plt.show()

# d)
evidenta = {"S1": "Ploaie", "S5": "Nori"}

ie = ShaferShenoyMRFInference(mrf)
ie.setEvidence(evidenta)
ie.makeInference()

posterior = ie.posterior("S3")       # sumeaza peste celelalte statii neobservate
print()
print("d) Evidenta:", evidenta)
print(posterior)
best = posterior.argmax()
print("MAP marginal la S3:", stari[best[0][0]["S3"]], round(best[1], 4))

# e)
neobservate = ["S2", "S3", "S4"]

ie2 = ShaferShenoyMRFInference(mrf)
ie2.setEvidence(evidenta)
ie2.addJointTarget(set(neobservate))
ie2.makeInference()

comun = ie2.jointPosterior(set(neobservate))     # posteriorul celor trei impreuna
amax = comun.argmax()
map_comun = {s: stari[amax[0][0][s]] for s in neobservate}
maxime = {s: stari[ie2.posterior(s).argmax()[0][0][s]] for s in neobservate}

print()
print("e) MAP comun:        ", map_comun, round(amax[1], 4))
print("   maxime marginale: ", maxime, round(comun[maxime], 4))
print("   Nu coincid: suma si maximul nu comuta.")
