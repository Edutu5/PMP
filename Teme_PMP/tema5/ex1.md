# Tema 5 – Exerciţiul 1: algoritmul Forward

Model Markov ascuns cu stări $X_1, \dots, X_T$ şi observaţii $O_1, \dots, O_T$. Notăm:

$$\pi_i = P(X_1 = i), \qquad a_{ij} = P(X_{t+1} = j \mid X_t = i), \qquad b_j(o) = P(O_t = o \mid X_t = j)$$

Pentru o secvenţă de observaţii $o_1, \dots, o_T$, definim variabila **Forward**:

$$\alpha_t(j) = P(O_1 = o_1, \dots, O_t = o_t,\ X_t = j)$$

Observaţie importantă asupra definiţiei: $\alpha_t(j)$ este o probabilitate **comună** a observaţiilor de până la momentul $t$ şi a stării curente, nu o probabilitate condiţionată.

Cele două ipoteze ale modelului, folosite peste tot mai jos:

1. **Proprietatea Markov:** $P(X_t \mid X_{t-1}, X_{t-2}, \dots, O_{1:t-1}) = P(X_t \mid X_{t-1})$
2. **Ipoteza de emisie:** $P(O_t \mid X_{1:T}, O_{1:t-1}) = P(O_t \mid X_t)$

---

## a) Iniţializare

**De arătat:** $\alpha_1(j) = \pi_j \, b_j(o_1)$.

La momentul $t = 1$ definiţia devine

$$\alpha_1(j) = P(O_1 = o_1,\ X_1 = j)$$

Aplicăm regula produsului, condiţionând după starea iniţială:

$$\alpha_1(j) = P(X_1 = j) \cdot P(O_1 = o_1 \mid X_1 = j)$$

Primul factor este, prin definiţie, $\pi_j$. Al doilea este, prin ipoteza de emisie, $b_j(o_1)$ — observaţia de la momentul 1 depinde doar de starea de la momentul 1. Deci

$$\boxed{\alpha_1(j) = \pi_j \, b_j(o_1)}$$

Nu apare niciun termen de tranziţie, fiindcă la primul moment nu există o stare anterioară din care să se vină.

---

## b) Recurenţa

**De arătat:** pentru $t = 2, \dots, T$,

$$\alpha_t(j) = b_j(o_t) \sum_i \alpha_{t-1}(i) \, a_{ij}$$

**Pasul 1 — condiţionăm după starea anterioară.** Evenimentele $\{X_{t-1} = i\}$ formează o partiţie a spaţiului, deci prin formula probabilităţii totale:

$$\alpha_t(j) = P(o_{1:t},\ X_t = j) = \sum_i P(o_{1:t},\ X_{t-1} = i,\ X_t = j)$$

**Pasul 2 — separăm observaţia curentă.** Aplicăm regula produsului, desprinzând $O_t$ de restul:

$$P(o_{1:t},\ X_{t-1} = i,\ X_t = j) = P(o_t \mid o_{1:t-1},\ X_{t-1} = i,\ X_t = j) \cdot P(o_{1:t-1},\ X_{t-1} = i,\ X_t = j)$$

Prin ipoteza de emisie, primul factor se simplifică: observaţia de la momentul $t$ depinde doar de starea de la momentul $t$, deci

$$P(o_t \mid o_{1:t-1},\ X_{t-1} = i,\ X_t = j) = b_j(o_t)$$

Cum acest factor nu depinde de $i$, îl scoatem în faţa sumei:

$$\alpha_t(j) = b_j(o_t) \sum_i P(o_{1:t-1},\ X_{t-1} = i,\ X_t = j)$$

**Pasul 3 — separăm tranziţia.** Aplicăm din nou regula produsului, de data aceasta desprinzând $X_t$:

$$P(o_{1:t-1},\ X_{t-1} = i,\ X_t = j) = P(X_t = j \mid o_{1:t-1},\ X_{t-1} = i) \cdot P(o_{1:t-1},\ X_{t-1} = i)$$

Prin proprietatea Markov, starea următoare depinde doar de starea curentă, deci primul factor este $a_{ij}$. Al doilea factor este chiar definiţia lui $\alpha_{t-1}(i)$.

**Pasul 4 — concluzia.** Punând totul împreună:

$$\boxed{\alpha_t(j) = b_j(o_t) \sum_i \alpha_{t-1}(i) \, a_{ij}} \quad \blacksquare$$

**Citire intuitivă.** Pentru a ajunge în starea $j$ la momentul $t$, se poate veni din oricare stare $i$; suma adună contribuţiile tuturor acestor variante, fiecare cântărită cu probabilitatea tranziţiei. Abia la final se înmulţeşte cu probabilitatea de a observa $o_t$ din starea $j$.

---

## c) Finalizarea

**De arătat:** $P(O_1 = o_1, \dots, O_T = o_T) = \sum_j \alpha_T(j)$.

Prin definiţie,

$$\sum_j \alpha_T(j) = \sum_j P(o_{1:T},\ X_T = j)$$

Evenimentele $\{X_T = j\}$, pentru $j$ parcurgând toate stările, formează o partiţie a spaţiului: la momentul $T$ lanţul se află exact într-una dintre stări. Prin formula probabilităţii totale, suma lor marginalizează ultima stare ascunsă:

$$\sum_j P(o_{1:T},\ X_T = j) = P(o_{1:T})$$

Deci

$$\boxed{P(O_1 = o_1, \dots, O_T = o_T) = \sum_j \alpha_T(j)} \quad \blacksquare$$

---

## Observaţie asupra complexităţii

Enumerarea directă a tuturor traseelor ar cere $N^T$ termeni. Recurenţa Forward calculează, la fiecare din cei $T$ paşi, câte $N$ valori, fiecare cerând o sumă peste $N$ termeni, deci **$O(TN^2)$** operaţii.

Toată economia vine din proprietatea Markov: tot ce contează din trecut este starea curentă, aşa că traseele care ajung în aceeaşi stare pot fi agregate într-un singur număr şi nu mai trebuie urmărite separat.

**Legătura cu Viterbi.** Algoritmul Viterbi are exact aceeaşi structură, cu o singură modificare: suma $\sum_i$ este înlocuită cu maximul $\max_i$. Forward răspunde la „cât de probabilă este secvenţa observată?", adunând contribuţiile tuturor traseelor; Viterbi răspunde la „care este cel mai bun traseu?", păstrând doar cel mai bun dintre ele.
