# Tema 3 – Laboratorul 4

**Reţele Bayesiene**

## Exerciţiul 1

În documentaţia pgmpy (<https://pgmpy.org/examples/Monty_Hall.html>) găsiţi formularea şi implementarea celebrei probleme Monty Hall. Cerinţa acestui exerciţiu este să explicaţi problema şi codul din implementare.

## Exerciţiul 2

Un medic doreşte să determine probabilitatea ca un pacient să aibă o anumită boală pulmonară (B), având în vedere simptomele observate. Există trei variabile observabile care pot indica prezenţa bolii: tuse (T), dificultate de respiraţie (D), radiografie anormală (X). Toate acestea sunt variabile binare.

De asemenea, ştim că:

- Dacă pacientul are boala (B), există o probabilitate ridicată să aibă tuse şi să apară anomalii la radiografie.
- Dificultatea de respiraţie (D) este dependentă atât de prezenţa bolii pulmonare (B), cât şi de prezenţa tusei (T).

Datele de probabilitate condiţionată sunt următoarele:

1. Probabilitatea apriori pentru boala pulmonară: `P(B = 1) = 0.1`, `P(B = 0) = 0.9`
2. Tuse (T) condiţionată de boală (B): `P(T = 1 | B = 1) = 0.8`, `P(T = 1 | B = 0) = 0.3`
3. Radiografie anormală (X) condiţionată de boală (B): `P(X = 1 | B = 1) = 0.9`, `P(X = 1 | B = 0) = 0.1`
4. Dificultate de respiraţie (D) condiţionată de boală (B) şi tuse (T):
   `P(D = 1 | B = 1, T = 1) = 0.9`, `P(D = 1 | B = 1, T = 0) = 0.4`,
   `P(D = 1 | B = 0, T = 1) = 0.5`, `P(D = 1 | B = 0, T = 0) = 0.1`

a) Definiţi modelul probabilist, folosind `pgmpy`, care să descrie contextul de mai sus.

b) Medicul observă că pacientul are tuse şi dificultăţi de respiraţie. Determinaţi probabilitatea ca pacientul să aibă boala pulmonară.

c) Ulterior se descoperă (cu alte mijloace) că pacientul nu avea boala pulmonară. Care este probabilitatea ca radiografia să fi fost anormală?

d) Calculaţi cele 2 probabilităţi folosind regula lui Bayes şi încărcaţi calculul fie în Markdown/LaTeX, fie ca foto la foaia de lucru (indicaţie: puteţi să vă folosiţi de independenţele condiţionate rezultate din modelul de reţea bayesiană).

## Exerciţiul 3

Un joc între doi jucători, J₀ şi J₁, se desfăşoară în felul următor:

- se aruncă mai întâi cu o monedă (normală) pentru a decide cine începe: J₀ sau J₁;
- în prima rundă, jucătorul desemnat aruncă cu propriul zar; fie `n` numărul obţinut;
- în a doua rundă, celălalt jucător aruncă cu moneda proprie de `2n` ori; fie `m` numărul de steme obţinute.

Jucătorul din prima rundă câştigă dacă `n ≥ m`, în caz contrar câştigând jucătorul din a doua rundă. Mai ştim că jucătorul J₁ este necinstit, el aducând o monedă măsluită, cu probabilitatea de obţinere a stemei egală cu 4/7. În schimb, moneda jucătorului J₀ este normală, iar cele două zaruri sunt şi ele normale.

a) Estimaţi care dintre cei doi jucători are şansele cele mai mari de câştig, simulând un joc de 10000 de ori.

b) Folosind `pgmpy`, definiţi o reţea Bayesiană care să descrie contextul de mai sus.

c) Folosind modelul de mai sus, determinaţi cine e cel mai probabil să fi început jocul, ştiind că în a doua rundă s-a obţinut o singură stemă.

---

## Conţinutul folderului

| Fişier | Conţinut |
|---|---|
| `ex1.md` | exerciţiul 1 – explicarea problemei Monty Hall şi a codului pgmpy |
| `ex2.py` | exerciţiul 2, subpunctele a) – c) |
| `ex2_calcule.md` | exerciţiul 2, subpunctul d) – calculul cu regula lui Bayes |
| `ex3.py` | exerciţiul 3, subpunctele a) – c) |

## Rezultate

**Exerciţiul 2:** `P(B = 1 | T = 1, D = 1) ≈ 0.3478`; `P(X = 1 | B = 0, T = 1, D = 1) = 0.1`.

**Exerciţiul 3:** J₁ câştigă în aproximativ 57.7% dintre jocuri; `P(S | M = 1)` dă 0.4529 pentru J₀ şi 0.5471 pentru J₁, deci cel mai probabil a început J₁.
