# Tema 6 – Laboratorul 7

**Inferenţă Bayesiană şi simulare probabilistică**

**Obiectiv.** Veţi aplica actualizarea Bayesiană pentru un parametru necunoscut şi veţi utiliza simulări Monte Carlo pentru a evalua performanţa unui sistem de servire.

## Exerciţiul 1. Controlul calităţii într-o fabrică (inferenţă Bayesiană)

O fabrică produce componente electronice, dintre care unele pot fi defecte. Notăm cu `θ` probabilitatea ca o componentă aleasă aleatoriu să fie defectă. Presupunem că rezultatele testelor sunt independente condiţionat de `θ`.

Din experienţa anterioară, alegem distribuţia a priori `θ ~ Beta(2, 18)`. Dintre `n = 50` de componente testate, `y = 8` sunt defecte.

a) **Modelul probabilistic.** Scrieţi distribuţia lui `Y | θ`, unde `Y` este numărul de componente defecte din cele 50 testate, şi funcţia de verosimilitate `P(Y = y | θ)`.

b) **Actualizarea Bayesiană.** Folosind formula lui Bayes, determinaţi distribuţia a posteriori a lui `θ`. Justificaţi matematic rezultatul, folosind conjugarea Beta–Binomial.

c) **Estimarea parametrului.** Calculaţi estimatorul de maximă verosimilitate (MLE), estimatorul MAP şi media a posteriori. Comparaţi valorile şi explicaţi diferenţele.

d) **Vizualizare.** Reprezentaţi pe acelaşi grafic densităţile a priori şi a posteriori. Explicaţi cum au modificat datele informaţia despre rata de defectare.

e) **Incertitudine.** Determinaţi numeric un interval credibil central de 95% pentru `θ`, folosind `scipy.stats.beta`. Interpretaţi rezultatul.

f) **Decizie practică.** Fabrica doreşte ca rata de defectare să fie sub 10%. Calculaţi probabilitatea a posteriori `P(θ < 0.10 | Y = 8)` şi discutaţi în ce măsură datele susţin această cerinţă.

g) **Predicţie Bayesiană.** Se testează încă 10 componente produse în aceleaşi condiţii. Calculaţi probabilitatea predictivă ca niciuna să nu fie defectă. *Indiciu:* dacă `X` este numărul de componente defecte din noul eşantion, folosiţi

```
P(X = 0 | Y = 8) = ∫₀¹ (1 − θ)¹⁰ p(θ | Y = 8) dθ
```

*Indicaţie.* Puteţi utiliza numpy, scipy.stats şi matplotlib. Prezentaţi formulele şi interpretarea, nu doar valorile obţinute din biblioteci.

## Exerciţiul 2. Deschiderea unui restaurant fast-food (simulare Monte Carlo)

Doriţi să deschideţi o nouă locaţie fast-food. Clienţii sosesc conform unui *proces Poisson* cu intensitatea `λ = 20` clienţi/oră. Timpul necesar pentru plasarea şi plata unei comenzi este exponenţial cu media de 2 minute, iar timpul de preparare este exponenţial cu media de `α` minute.

**Ipoteze de modelare:** există o singură casă şi o singură staţie de gătit; fiecare funcţionează în ordinea sosirii comenzilor (FIFO). Un client trece mai întâi pe la casă, apoi comanda sa intră în coada staţiei de gătit. Timpii de servire sunt independenţi între ei şi de sosiri. La începutul orei, sistemul este gol. Pentru clienţii sosiţi în intervalul `[0, 60]` minute, urmărim servirea lor completă, chiar dacă aceasta se termină după minutul 60.

a) Construiţi în Python o simulare a unei ore: generaţi momentele sosirilor, timpii de plată şi timpii de preparare; calculaţi pentru fiecare client momentul la care primeşte mâncarea. Explicaţi cum trataţi cele două cozi.

b) Estimaţi prin simulări repetate probabilitatea ca *fiecare* client sosit în ora respectivă să primească mâncarea în cel mult 15 minute de la sosire. Determinaţi aproximativ cea mai mare valoare a lui `α` pentru care probabilitatea este de cel puţin 95%.

c) Pentru valoarea lui `α` obţinută, estimaţi timpul mediu dintre sosirea unui client şi primirea mâncării. Raportaţi separat, dacă doriţi, timpul mediu petrecut efectiv în aşteptare (fără servire).

d) Precizaţi numărul de simulări, sămânţa aleatoare şi metoda de căutare a lui `α`. Discutaţi pe scurt de ce estimările se pot modifica de la o rulare la alta.

*Indicaţie.* Pentru simulare sunt suficiente numpy şi, opţional, scipy.stats. Atenţie: condiţia de 95% se referă la *toţi clienţii dintr-o oră*, nu la un client ales aleatoriu.

---

## Conţinutul folderului

| Fişier | Conţinut |
|---|---|
| `ex1.py` | exerciţiul 1, subpunctele a) – g) |
| `ex2.py` | exerciţiul 2, subpunctele a) – d) |

## Rezultate

### Exerciţiul 1

Posteriorul este **Beta(10, 60)**, prin conjugare: `α → α + y = 2 + 8`, `β → β + n − y = 18 + 42`.

| Mărime | Valoare |
|---|---|
| MLE | 0.1600 |
| MAP | 0.1324 |
| Media a posteriori | 0.1429 |
| Interval credibil central 95% | [0.0717, 0.2332] |
| `P(θ < 0.10 \| Y = 8)` | 0.1484 |
| `P(X = 0 \| Y = 8)` | 0.2360 |

Doar aproximativ 15% din masa posterioară se află sub pragul de 10%, deci datele **nu** susţin cerinţa fabricii.

### Exerciţiul 2

| `α` (minute) | `P(toţi clienţii sub 15 min)` |
|---|---|
| 0.00 | 0.807 |
| 0.25 | 0.801 |
| 0.50 | 0.785 |
| 0.75 | 0.770 |
| 1.00 | 0.736 |
| 1.50 | 0.628 |
| 2.00 | 0.449 |

**Nu există `α` care să asigure 95%.** Probabilitatea este descrescătoare în `α`, iar valoarea ei maximă, atinsă în limita `α → 0` (preparare instantanee), este de aproximativ **0.81**.

Cauza este **casa de marcat**, nu staţia de gătit. Timpul mediu între sosiri este `60/20 = 3` minute, iar timpul mediu de plată este 2 minute, deci gradul de încărcare al casei este `ρ = 2/3`. Într-o oră cu aproximativ 20 de clienţi, cel puţin unul depăşeşte 15 minute în aproape o oră din cinci, oricât de repede s-ar găti.

Timpii medii de la sosire până la primirea mâncării:

| `α` | Timp total | Din care aşteptare pură |
|---|---|---|
| 0.5 | 5.50 min | 2.97 min |
| 1.0 | 6.11 min | 3.12 min |
| 1.5 | 7.20 min | 3.70 min |
| 2.0 | 8.94 min | 4.96 min |

**Parametri de rulare:** 20.000 de simulări pentru fiecare valoare a lui `α` (2.000 pentru timpii medii de la c), sămânţă `42`, căutare prin baleierea unei grile de valori. Eroarea Monte Carlo pentru probabilităţi este sub 0.003.
