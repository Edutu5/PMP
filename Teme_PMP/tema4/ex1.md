# Tema 4 – Exerciţiul 1: de la independenţă condiţionată la factorizare

Trei variabile aleatoare discrete $A, B, C$ şi graful neorientat $A - B - C$. Presupunem distribuţia comună **strict pozitivă**: $P(a, b, c) > 0$ pentru orice configuraţie.

---

## a) Ce înseamnă $A \perp\!\!\!\perp C \mid B$

Prin definiţie, $A$ este independentă condiţionat de $C$, dată $B$, dacă pentru orice valori $a, b, c$:

$$P(a, c \mid b) = P(a \mid b) \cdot P(c \mid b)$$

**Forma echivalentă, mai intuitivă.** Împărţim ambii membri la $P(c \mid b)$, ceea ce este permis fiindcă distribuţia comună este strict pozitivă, deci şi $P(c \mid b) > 0$:

$$\frac{P(a, c \mid b)}{P(c \mid b)} = P(a \mid b)$$

Membrul stâng este, prin definiţia probabilităţii condiţionate, chiar $P(a \mid b, c)$. Obţinem:

$$P(a \mid b, c) = P(a \mid b)$$

**În cuvinte:** odată ce valoarea lui $B$ este cunoscută, $C$ nu mai oferă nicio informaţie suplimentară despre $A$. A adăuga cunoaşterea lui $C$ nu schimbă cu nimic ce credem despre $A$.

**Ce spune graful.** În lanţul $A - B - C$, orice drum de la $A$ la $C$ trece prin $B$. Condiţionarea pe $B$ blochează acest drum — singura cale pe care informaţia putea circula între cele două capete. Aceasta este exact proprietatea de separare din Cursul 3: $B$ separă $A$ de $C$ în graf, deci $A \perp\!\!\!\perp C \mid B$ în model.

---

## b) Independenţa implică factorizarea

**De demonstrat:** $A \perp\!\!\!\perp C \mid B$ implică existenţa unor potenţiale strict pozitive $\phi_{AB}$, $\phi_{BC}$ şi a unei constante $Z > 0$ pentru care

$$P(a, b, c) = \frac{1}{Z} \phi_{AB}(a, b) \, \phi_{BC}(b, c)$$

**Pasul 1 — pozitivitatea lui $P(b)$.** Avem nevoie de $P(b) > 0$ ca să putem împărţi la el. Prin marginalizare,

$$P(b) = \sum_{a, c} P(a, b, c) > 0$$

ca sumă de termeni strict pozitivi.

**Pasul 2 — scrierea distribuţiei comune.** Din definiţia probabilităţii condiţionate,

$$P(a, c \mid b) = \frac{P(a, b, c)}{P(b)} \quad \Longrightarrow \quad P(a, b, c) = P(a, c \mid b) \cdot P(b)$$

**Pasul 3 — aplicarea ipotezei.** Înlocuind $P(a, c \mid b) = P(a \mid b) P(c \mid b)$:

$$P(a, b, c) = P(a \mid b) \cdot P(c \mid b) \cdot P(b)$$

**Pasul 4 — identificarea potenţialelor.** Expresia este deja un produs între un factor care depinde doar de $(a, b)$ şi unul care depinde doar de $(b, c)$. Alegem:

$$\phi_{AB}(a, b) = P(a \mid b) \, P(b) = P(a, b), \qquad \phi_{BC}(b, c) = P(c \mid b) = \frac{P(b, c)}{P(b)}, \qquad Z = 1$$

**Pasul 5 — pozitivitatea potenţialelor.** Definiţia cere $\phi_{AB}, \phi_{BC} > 0$. Fiindcă $P(a, b, c) > 0$ pentru orice configuraţie, toate marginalele sunt strict pozitive:

$$P(a, b) = \sum_c P(a, b, c) > 0, \qquad P(b, c) = \sum_a P(a, b, c) > 0, \qquad P(b) > 0$$

Cum cele două potenţiale sunt construite doar din aceste marginale, ele sunt strict pozitive. De asemenea $Z = 1 > 0$.

**Pasul 6 — verificarea.**

$$\frac{1}{Z} \phi_{AB}(a, b) \, \phi_{BC}(b, c) = 1 \cdot P(a, b) \cdot \frac{P(b, c)}{P(b)} = P(a \mid b) P(b) \cdot P(c \mid b) = P(a, b, c) \quad \blacksquare$$

---

## c) Reciproca: factorizarea implică independenţa

**De demonstrat:** dacă există $\phi_{AB}, \phi_{BC} > 0$ şi $Z > 0$ cu

$$P(a, b, c) = \frac{1}{Z} \phi_{AB}(a, b) \, \phi_{BC}(b, c)$$

atunci $A \perp\!\!\!\perp C \mid B$.

**Strategia:** calculăm separat $P(a \mid b)$, $P(c \mid b)$ şi $P(a, c \mid b)$, apoi arătăm că a treia este produsul primelor două. Toate se obţin prin marginalizare, iar distribuţia fiind strict pozitivă, fiecare numitor este nenul.

**Pasul 1 — marginala lui $B$.** Sumăm după $a$ şi după $c$. Suma dublă se separă, fiindcă $\phi_{AB}$ nu depinde de $c$ şi $\phi_{BC}$ nu depinde de $a$:

$$P(b) = \sum_{a, c} \frac{1}{Z} \phi_{AB}(a, b) \phi_{BC}(b, c) = \frac{1}{Z} \underbrace{\left( \sum_a \phi_{AB}(a, b) \right)}_{f(b)} \underbrace{\left( \sum_c \phi_{BC}(b, c) \right)}_{g(b)} = \frac{1}{Z} f(b) g(b)$$

Atât $f(b)$ cât şi $g(b)$ sunt strict pozitive, fiind sume de termeni strict pozitivi.

**Pasul 2 — $P(a \mid b)$.** Sumăm doar după $c$:

$$P(a, b) = \sum_c \frac{1}{Z} \phi_{AB}(a, b) \phi_{BC}(b, c) = \frac{1}{Z} \phi_{AB}(a, b) \, g(b)$$

Împărţind la $P(b)$, se simplifică $\frac{1}{Z}$ şi $g(b)$:

$$P(a \mid b) = \frac{\frac{1}{Z} \phi_{AB}(a, b) g(b)}{\frac{1}{Z} f(b) g(b)} = \frac{\phi_{AB}(a, b)}{f(b)} \qquad (1)$$

**Pasul 3 — $P(c \mid b)$.** Simetric, sumând după $a$:

$$P(b, c) = \frac{1}{Z} \phi_{BC}(b, c) \, f(b) \quad \Longrightarrow \quad P(c \mid b) = \frac{\phi_{BC}(b, c)}{g(b)} \qquad (2)$$

**Pasul 4 — $P(a, c \mid b)$.** Împărţim distribuţia comună la $P(b)$:

$$P(a, c \mid b) = \frac{\frac{1}{Z} \phi_{AB}(a, b) \phi_{BC}(b, c)}{\frac{1}{Z} f(b) g(b)} = \frac{\phi_{AB}(a, b)}{f(b)} \cdot \frac{\phi_{BC}(b, c)}{g(b)} \qquad (3)$$

**Pasul 5 — concluzia.** Comparând $(3)$ cu $(1)$ şi $(2)$, membrul drept al relaţiei $(3)$ este exact produsul membrilor drepţi ai relaţiilor $(1)$ şi $(2)$:

$$P(a, c \mid b) = P(a \mid b) \cdot P(c \mid b) \quad \Longrightarrow \quad A \perp\!\!\!\perp C \mid B \quad \blacksquare$$

---

## Observaţie

Cele două implicaţii împreună dau echivalenţa dintre independenţa condiţionată şi factorizarea după clicile grafului — cazul particular, pe un lanţ cu trei noduri, al teoremei **Hammersley–Clifford** (Cursul 3, slide 17). Ipoteza de strictă pozitivitate este esenţială: ea este folosită la fiecare împărţire, atât în b) cât şi în c), şi fără ea teorema nu mai este adevărată în general.
