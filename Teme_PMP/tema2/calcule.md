# Tema 2 – calcule teoretice

Formula folosită peste tot:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0.$$

---

# Exerciţiul 1

Spaţiul de probabilitate: $\Omega = \{1,\dots,6\}^2$, cu $|\Omega| = 36$ rezultate echiprobabile, deci $P(A) = \frac{\#A}{36}$.

Perechile cu $X + Y \ge 10$ sunt $(4,6), (5,5), (5,6), (6,4), (6,5), (6,6)$ — în total **6**.

## 1. $P(X + Y \ge 10 \mid X \text{ par})$

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{\#(A \cap B)/36}{\#B/36} = \frac{\#(A \cap B)}{\#B}$$

- $\#B$: $X \in \{2,4,6\}$ şi $Y$ oarecare $\Rightarrow 3 \cdot 6 = 18$.
- $\#(A \cap B)$: din cele 6 perechi de mai sus, cele cu $X$ par sunt $(4,6), (6,4), (6,5), (6,6) \Rightarrow 4$.

$$P(A \mid B) = \frac{4}{18} = \frac{2}{9} \approx 0.2222$$

## 2. $P(X + Y \ge 10 \mid \text{cel puţin un zar par})$

Notăm $C = \{\text{cel puţin un zar par}\}$. Trecem la complementar:

$$\#C = 36 - \#\{\text{ambele impare}\} = 36 - 3 \cdot 3 = 27$$

Din cele 6 perechi cu suma $\ge 10$, singura cu ambele impare este $(5,5)$, deci $\#(A \cap C) = 6 - 1 = 5$.

$$P(A \mid C) = \frac{5}{27} \approx 0.1852$$

## 3. $P(\text{ambele pare} \mid X + Y = 8)$

Notăm $D = \{X + Y = 8\}$ şi $E = \{\text{ambele pare}\}$.

- $\#D$: $(2,6), (3,5), (4,4), (5,3), (6,2) \Rightarrow 5$.
- $\#(E \cap D)$: $(2,6), (4,4), (6,2) \Rightarrow 3$.

$$P(E \mid D) = \frac{3}{5} = 0.6$$

## 4. Sunt $A = \{X + Y \ge 10\}$ şi $B = \{X \text{ par}\}$ independente?

Criteriul de independenţă: $P(A \cap B) = P(A) \cdot P(B)$.

$$P(A) = \frac{6}{36} = \frac{1}{6}, \qquad P(B) = \frac{18}{36} = \frac{1}{2}, \qquad P(A \cap B) = \frac{4}{36} = \frac{1}{9}$$

$$P(A) \cdot P(B) = \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{12} \ne \frac{1}{9} = P(A \cap B)$$

**Nu sunt independente.** Echivalent: $P(A \mid B) = \frac{2}{9} \ne \frac{1}{6} = P(A)$ — a şti că primul zar este par schimbă plauzibilitatea evenimentului $A$, fiindcă sumele mari cer valori mari la primul zar.

---

# Exerciţiul 2 – Filtrarea mesajelor spam

Notaţii: $S$ = mesajul este spam, $O$ = conţine „ofertă", $G$ = conţine „gratuit".

Date: $P(S) = 0.3$, $P(S^c) = 0.7$, $P(O \mid S) = 0.8$, $P(O \mid S^c) = 0.15$.

## 1. $P(S \mid O)$

Formula lui Bayes cu formula probabilităţii totale la numitor:

$$P(S \mid O) = \frac{P(O \mid S) P(S)}{P(O \mid S) P(S) + P(O \mid S^c) P(S^c)}$$

$$P(S \mid O) = \frac{0.8 \cdot 0.3}{0.8 \cdot 0.3 + 0.15 \cdot 0.7} = \frac{0.24}{0.24 + 0.105} = \frac{0.24}{0.345} \approx 0.6957$$

Priorul de 30% urcă la aproximativ **69.6%**.

## 2. $P(S \mid O \cap G)$

Date suplimentare: $P(G \mid S) = 0.6$, $P(G \mid S^c) = 0.10$.

Ipoteza de **independenţă condiţionată** a celor două cuvinte, dată clasa mesajului:

$$P(O \cap G \mid S) = P(O \mid S) P(G \mid S) = 0.8 \cdot 0.6 = 0.48$$
$$P(O \cap G \mid S^c) = P(O \mid S^c) P(G \mid S^c) = 0.15 \cdot 0.10 = 0.015$$

$$P(S \mid O \cap G) = \frac{0.48 \cdot 0.3}{0.48 \cdot 0.3 + 0.015 \cdot 0.7} = \frac{0.144}{0.144 + 0.0105} = \frac{0.144}{0.1545} \approx 0.9320$$

Al doilea cuvânt urcă posteriorul de la 69.6% la aproximativ **93.2%**.

## 3. De ce ipoteza independenţei condiţionate poate fi nerealistă

Independenţa condiţionată cere ca, în interiorul clasei spam, apariţia cuvântului „ofertă" să nu schimbe plauzibilitatea apariţiei cuvântului „gratuit". În practică cele două apar împreună mult mai des decât ar prezice produsul: „ofertă gratuită" este o formulare frecventă.

Consecinţa este că modelul tratează două indicii puternic corelate ca pe două dovezi independente şi le înmulţeşte contribuţiile. Posteriorul este astfel împins artificial spre 0 sau 1 — estimarea rămâne adesea utilă pentru ordonarea mesajelor, dar valoarea numerică a probabilităţii este prea încrezătoare.

## 4. Regulă de clasificare

Clasificăm un mesaj $x$ drept spam dacă posteriorul depăşeşte un prag:

$$\text{spam} \iff P(S \mid x) \ge t$$

Pragul $t$ nu este o constantă universală, ci depinde de costul celor două tipuri de eroare. Dacă $L_{FP}$ este costul marcării greşite a unui mesaj legitim şi $L_{FN}$ costul ratării unui spam, decizia optimă este

$$\text{spam} \iff \frac{P(S \mid x)}{1 - P(S \mid x)} \ge \frac{L_{FP}}{L_{FN}}$$

Pentru costuri egale rezultă $t = 0.5$. În practică un mesaj legitim pierdut este mult mai grav decât un spam ajuns în inbox, deci $L_{FP} \gg L_{FN}$ şi pragul se ridică, de exemplu $t = 0.95$.

Cu datele de mai sus: un mesaj care conţine doar „ofertă" are $P(S \mid O) \approx 0.70 < 0.95$, deci trece; unul care conţine ambele cuvinte are $P(S \mid O \cap G) \approx 0.93$, încă sub prag la $t = 0.95$.

---

# Exerciţiul 3 – Paradoxul lui Simpson

## 1. Rata de promovare pe program şi disciplină

| Program | Disciplina A | Disciplina B |
|---|---|---|
| Programul 1 | $81/90 = 0.900$ | $19/20 = 0.950$ |
| Programul 2 | $1/10 = 0.100$ | $16/80 = 0.200$ |

## 2. Care disciplină are rata mai mare în fiecare program

- Programul 1: $0.950 > 0.900 \Rightarrow$ **disciplina B**.
- Programul 2: $0.200 > 0.100 \Rightarrow$ **disciplina B**.

Disciplina B are rata mai mare în **ambele** programe.

## 3. Rata globală, pe discipline

$$P(\text{promovat} \mid A) = \frac{81 + 1}{90 + 10} = \frac{82}{100} = 0.82$$

$$P(\text{promovat} \mid B) = \frac{19 + 16}{20 + 80} = \frac{35}{100} = 0.35$$

Global, **disciplina A** are rata mai mare: $0.82 > 0.35$. Ordinea s-a inversat.

## 4. De ce se inversează ordinea

Cele două programe au niveluri foarte diferite: Programul 1 promovează mult (90% şi 95%), Programul 2 promovează puţin (10% şi 20%). Dar cele două discipline nu atrag studenţi în aceleaşi proporţii:

- disciplina A: 90 din 100 de studenţi vin din Programul 1 (cel puternic);
- disciplina B: 80 din 100 de studenţi vin din Programul 2 (cel slab).

Rata globală a unei discipline este o **medie ponderată** a ratelor pe programe, iar ponderile diferă masiv între discipline. Disciplina A arată bine global nu pentru că ar fi mai uşoară, ci pentru că este populată aproape exclusiv de studenţi care promovează oricum. Programul este o variabilă **confundătoare**: influenţează şi disciplina aleasă, şi rezultatul.

## 5. Formularea în termeni de probabilităţi condiţionate

Notăm $R$ = promovat, $D \in \{A, B\}$ disciplina, $Pr \in \{1, 2\}$ programul. Paradoxul se scrie:

$$P(R \mid D = A, Pr = i) < P(R \mid D = B, Pr = i), \qquad i = 1, 2$$

$$\text{dar} \qquad P(R \mid D = A) > P(R \mid D = B)$$

Legătura dintre cele două niveluri este formula probabilităţii totale:

$$P(R \mid D) = \sum_{i=1}^{2} P(R \mid D, Pr = i) \, P(Pr = i \mid D)$$

Inegalitatea se inversează pentru că ponderile $P(Pr = i \mid D)$ diferă puternic între cele două discipline:

$$P(Pr = 1 \mid A) = 0.90 \quad \text{faţă de} \quad P(Pr = 1 \mid B) = 0.20$$

**Concluzie:** marginalizarea după o variabilă confundătoare poate inversa o inegalitate valabilă în fiecare strat. Comparaţia corectă este cea condiţionată de program.
