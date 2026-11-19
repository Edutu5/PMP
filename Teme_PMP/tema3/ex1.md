# Tema 3 – Exerciţiul 1: problema Monty Hall în pgmpy

Sursa: <https://pgmpy.org/examples/Monty_Hall.html>

## Problema

Un concurent alege una dintre trei uşi. În spatele uneia este un premiu, în spatele celorlalte două nu este nimic. Prezentatorul, **care ştie unde este premiul**, deschide una dintre uşile rămase — mereu una fără premiu — şi îi oferă concurentului şansa de a-şi schimba alegerea.

Întrebarea: este avantajos să schimbe?

Răspunsul, contraintuitiv, este **da**: schimbând, probabilitatea de câştig urcă de la 1/3 la 2/3.

## De ce funcţionează

Cheia este că prezentatorul **nu alege la întâmplare**. El ştie unde este premiul şi este obligat să deschidă o uşă fără premiu, diferită de cea aleasă de concurent. Uşa pe care o deschide nu este deci o observaţie neutră: ea poartă informaţie despre locul premiului.

Dacă prezentatorul ar deschide o uşă la întâmplare şi s-ar nimeri să fie goală, probabilităţile ar rămâne 1/2–1/2 şi schimbarea n-ar aduce niciun avantaj. Toată asimetria vine din regula după care joacă prezentatorul.

## Modelul

Trei variabile, fiecare cu stările 0, 1, 2 (numărul uşii):

| Variabilă | Semnificaţie | Părinţi |
|---|---|---|
| `C` | uşa aleasă de concurent | — |
| `P` | uşa cu premiul | — |
| `H` | uşa deschisă de prezentator | `C`, `P` |

Structura este `C → H ← P`, adică un **collider** (Cursul 2, slide 25). `C` şi `P` sunt independente în model — concurentul alege fără să ştie nimic — dar **observarea lui `H` deschide calea dintre ele**. Exact asta produce paradoxul: după ce vedem ce uşă a deschis prezentatorul, alegerea iniţială şi locul premiului devin dependente.

Distribuţia comună se factorizează după părinţi:

$$P(C, P, H) = P(C) \, P(P) \, P(H \mid C, P)$$

## Codul

```python
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([("C", "H"), ("P", "H")])

cpd_c = TabularCPD("C", 3, [[0.33], [0.33], [0.33]])
cpd_p = TabularCPD("P", 3, [[0.33], [0.33], [0.33]])

cpd_h = TabularCPD("H", 3, [[0, 0, 0, 0, 0.5, 1, 0, 1, 0.5],
                            [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5],
                            [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]],
                   evidence=["C", "P"], evidence_card=[3, 3])

model.add_cpds(cpd_c, cpd_p, cpd_h)
model.check_model()

infer = VariableElimination(model)
print(infer.query(["P"], evidence={"C": 0, "H": 2}))
```

## Explicarea codului, linie cu linie

**`DiscreteBayesianNetwork([("C", "H"), ("P", "H")])`** — construieşte DAG-ul din lista de muchii. Doar `H` are părinţi; `C` şi `P` sunt rădăcini.

**`cpd_c`, `cpd_p`** — distribuţii uniforme pe trei uşi. Nu au `evidence`, fiind variabile fără părinţi. Valoarea 0.33 este rotunjirea lui 1/3 folosită în documentaţie.

**`cpd_h`** — tabelul condiţionat $P(H \mid C, P)$, cu 3 rânduri (stările lui `H`) şi $3 \times 3 = 9$ coloane (combinaţiile părinţilor). Ordinea coloanelor, dată de `evidence=["C", "P"]`, este cea lexicografică cu **ultima variabilă variind cel mai repede**:

$$(C,P) = (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)$$

Fiecare coloană codifică regula prezentatorului:

| $(C, P)$ | Uşi permise | Coloana |
|---|---|---|
| $(0,0)$ | 1 sau 2, la întâmplare | $(0,\ 0.5,\ 0.5)$ |
| $(0,1)$ | doar 2 | $(0,\ 0,\ 1)$ |
| $(0,2)$ | doar 1 | $(0,\ 1,\ 0)$ |
| $(1,1)$ | 0 sau 2, la întâmplare | $(0.5,\ 0,\ 0.5)$ |
| $(1,2)$ | doar 0 | $(1,\ 0,\ 0)$ |
| $(2,2)$ | 0 sau 1, la întâmplare | $(0.5,\ 0.5,\ 0)$ |

Regula este simplă: prezentatorul nu deschide niciodată uşa $C$ şi nici uşa $P$. Când concurentul a nimerit premiul din prima ($C = P$), rămân două uşi goale şi alege între ele cu 0.5–0.5. Altfel, uşa este unic determinată şi primeşte probabilitate 1.

**`check_model()`** — verifică structura şi faptul că fiecare coloană a unui CPD sumează la 1.

**`VariableElimination(model)`** — motorul de inferenţă prin eliminarea variabilelor (Cursul 2, slide 59): fixează evidenţa, înmulţeşte factorii relevanţi, sumează peste variabilele ascunse, normalizează.

**`infer.query(["P"], evidence={"C": 0, "H": 2})`** — interogarea propriu-zisă: concurentul a ales uşa 0, prezentatorul a deschis uşa 2; unde este premiul?

## Rezultatul

```
+------+----------+
| P    |   phi(P) |
+======+==========+
| P(0) |   0.3333 |
| P(1) |   0.6667 |
| P(2) |   0.0000 |
+------+----------+
```

- $P(P = 2) = 0$: prezentatorul tocmai a deschis uşa 2 şi nu deschide niciodată uşa cu premiul.
- $P(P = 0) = 1/3$: alegerea iniţială îşi păstrează probabilitatea de la început.
- $P(P = 1) = 2/3$: **uşa rămasă valorează dublu**.

Concluzia: concurentul trebuie să schimbe.

## De ce 1/3 nu se schimbă

Alegerea iniţială a fost făcută fără nicio informaţie, deci avea probabilitate 1/3 de a fi corectă. Prezentatorul putea deschide o uşă goală **indiferent** de unde era premiul, deci faptul că a deschis una nu spune nimic despre uşa 0. Masa de 2/3 care era distribuită pe uşile 1 şi 2 se concentrează însă complet pe uşa 1, de vreme ce uşa 2 a fost eliminată.
