from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# a)
# B influenteaza tusea T si radiografia X; dificultatea D depinde de B si de T
model = DiscreteBayesianNetwork([("B", "T"), ("B", "X"), ("B", "D"), ("T", "D")])

cpd_b = TabularCPD("B", 2, [[0.9], [0.1]])
cpd_t = TabularCPD("T", 2, [[0.7, 0.2],
                            [0.3, 0.8]], evidence=["B"], evidence_card=[2])
cpd_x = TabularCPD("X", 2, [[0.9, 0.1],
                            [0.1, 0.9]], evidence=["B"], evidence_card=[2])
# coloanele in ordinea (B,T) = (0,0), (0,1), (1,0), (1,1)
cpd_d = TabularCPD("D", 2, [[0.9, 0.5, 0.6, 0.1],
                            [0.1, 0.5, 0.4, 0.9]],
                   evidence=["B", "T"], evidence_card=[2, 2])

model.add_cpds(cpd_b, cpd_t, cpd_x, cpd_d)
print("Model valid:", model.check_model())

infer = VariableElimination(model)

# b)
print()
print("b) P(B | T=1, D=1):")
print(infer.query(["B"], evidence={"T": 1, "D": 1}))

# c)
# X este independenta de T si D conditionat de B, deci cele doua simptome nu mai conteaza
print()
print("c) P(X | B=0, T=1, D=1):")
print(infer.query(["X"], evidence={"B": 0, "T": 1, "D": 1}))
