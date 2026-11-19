# Tema 4 – Laboratorul 5

**Reţele Markov: independenţă, predicţie şi restaurarea imaginilor**

**Obiectiv.** La finalul temei, veţi putea interpreta independenţe condiţionate într-un graf neorientat, construi un model Markov discret, defini potenţiale şi calcula configuraţii de probabilitate maximă (MAP).

## Exerciţiul 1. De la independenţă condiţionată la factorizare

Considerăm trei variabile aleatoare discrete `A, B, C` şi graful neorientat `A – B – C`. Presupunem că distribuţia comună este **strict pozitivă** pentru toate configuraţiile posibile.

a) Explicaţi, în cuvintele voastre, ce înseamnă `A ⊥ C | B`. Ce informaţie suplimentară despre `A` mai oferă `C` atunci când cunoaştem `B`?

b) Pornind de la formula probabilităţii condiţionate, demonstraţi că `A ⊥ C | B` implică existenţa unor potenţiale strict pozitive `φ_AB` şi `φ_BC` şi a unei constante `Z > 0` pentru care

```
P(a, b, c) = (1/Z) · φ_AB(a, b) · φ_BC(b, c)
```

*Indiciu:* folosiţi `P(a, b, c) = P(a | b) P(c | b) P(b)`.

c) Demonstraţi şi reciproca, pornind de la factorizarea de mai sus. *Indiciu:* calculaţi `P(a, c | b)` şi verificaţi dacă este produsul lui `P(a | b)` şi `P(c | b)`.

**Predare:** o demonstraţie scurtă, în LaTeX/Markdown sau ca fotografie lizibilă. Nu este necesar cod Python.

## Exerciţiul 2. Putem prezice vremea la o staţie fără observaţii?

O regiune conţine `n` staţii meteo `S₁, …, Sₙ`. Fiecare variabilă are trei stări: *Soare*, *Ploaie*, *Nori*. Staţiile vecine tind să aibă vreme asemănătoare.

**Date de intrare:** alegeţi `n` (recomandat 4–6), o listă de muchii care formează un **arbore** şi probabilităţile iniţiale `pᵢ(s) > 0`, cu `Σₛ pᵢ(s) = 1` (puteţi folosi, pentru toate staţiile, 0.5, 0.3, 0.2). Pentru fiecare muchie folosiţi acelaşi potenţial pereche, cu rândurile şi coloanele în ordinea Soare, Ploaie, Nori:

```
Ψ = [[0.7, 0.2, 0.1],
     [0.2, 0.6, 0.2],
     [0.1, 0.3, 0.6]]
```

**Atenţie:** `Ψ` este un *potenţial*, nu trebuie interpretat ca matrice de probabilităţi condiţionate. Nici nu este necesar să fie simetric, deşi factorul unei muchii neorientate trebuie evaluat cu o ordine fixată a argumentelor.

a) Desenaţi graful ales şi identificaţi vecinii fiecărei staţii. Verificaţi că nu conţine cicluri.

b) Construiţi un model Markov discret în `pyAgrum` (sau `pgmpy`). Adăugaţi câte un factor unar `φᵢ(s) = pᵢ(s)` pentru fiecare staţie şi un factor pereche `φᵢⱼ(sᵢ, sⱼ) = Ψ_{sᵢ,sⱼ}` pentru fiecare muchie (alegeţi şi păstraţi aceeaşi ordine a variabilelor în factor).

c) Afişaţi graful modelului şi scrieţi formula distribuţiei comune:

```
P(s₁, …, sₙ) = (1/Z) · Πᵢ φᵢ(sᵢ) · Π_{(i,j)∈E} φᵢⱼ(sᵢ, sⱼ)
```

d) Consideraţi că la una sau două staţii vremea este cunoscută. Calculaţi distribuţia marginală la o staţie neobservată şi indicaţi starea cea mai probabilă la acea staţie (*MAP marginal*).

e) Determinaţi separat *configuraţia comună MAP* a tuturor staţiilor neobservate, condiţionat de observaţiile disponibile. Comparaţi-o cu alegerea separată a maximelor marginale: coincid întotdeauna?

**Indiciu tehnic:** în `pyAgrum` folosiţi un `MarkovRandomField`, factori unari/pereche şi mecanismul de inferenţă compatibil cu versiunea instalată. Pentru `n ≤ 6`, puteţi verifica rezultatele şi prin enumerarea tuturor celor `3ⁿ` configuraţii.

## Exerciţiul 3. Restaurarea unei imagini binare cu un MRF

Dorim să reconstruim o imagine binară mică, afectată de zgomot. Fiecare pixel are valoarea 0 (negru) sau 1 (alb). Vom utiliza o reţea Markov pe o grilă `5 × 5`, în care fiecare pixel este conectat numai cu vecinii săi direcţi (sus, jos, stânga, dreapta).

a) Construiţi o imagine binară `5 × 5` cu un model simplu (de exemplu, un pătrat alb pe fond negru). Afişaţi matricea şi imaginea.

b) Modificaţi aleatoriu aproximativ 10% dintre pixeli, inversând `0 ↔ 1`. Notaţi imaginea observată cu `y` şi afişaţi-o alături de imaginea originală. Folosiţi o sămânţă aleatoare fixă pentru reproductibilitate.

c) Modelaţi pixelii necunoscuţi prin variabile binare `xᵢ`. Construiţi graful MRF şi definiţi energia

```
E(x; y) = λ · Σᵢ (xᵢ − yᵢ)² + Σ_{(i,j)∈E} (xᵢ − xⱼ)²,    λ > 0
```

Explicaţi rolul fiecărui termen şi scrieţi potenţialele unare `φᵢ(xᵢ) = e^{−λ(xᵢ−yᵢ)²}` şi pereche `φᵢⱼ(xᵢ, xⱼ) = e^{−(xᵢ−xⱼ)²}`.

d) Folosind `pyAgrum` sau `pgmpy`, construiţi factorii şi determinaţi o configuraţie MAP, adică o imagine `x*` care minimizează `E(x; y)`. Pentru grila `5 × 5`, inferenţa exactă poate fi costisitoare; este permisă şi o metodă aproximativă (de exemplu, ICM), dacă explicaţi algoritmul folosit.

e) Repetaţi pentru cel puţin trei valori ale lui `λ` (de exemplu, 0.3, 1, 3). Afişaţi imaginile obţinute şi comparaţi numărul de pixeli reconstruiţi greşit faţă de original. Explicaţi de ce un `λ` mic favorizează netezirea, iar unul mare fidelitatea faţă de observaţie.

**Indiciu:** nu confundaţi energia `E(x; y)` cu probabilitatea: `P(x | y) ∝ e^{−E(x;y)}`. Dacă folosiţi ICM, precizaţi că acesta poate găsi un minim local, nu neapărat MAP global.

---

## Conţinutul folderului

| Fişier | Conţinut |
|---|---|
| `ex1.md` | exerciţiul 1 – demonstraţia, subpunctele a) – c) |
| `ex2.py` | exerciţiul 2, subpunctele a) – e) |
| `ex3.py` | exerciţiul 3, subpunctele a) – e) |

## Rezultate

**Exerciţiul 2.** Graful ales este un arbore cu 5 noduri şi 4 muchii. Cu evidenţa `S1 = Ploaie`, `S5 = Nori`: marginala la `S3` este (0.4651, 0.3922, 0.1426), deci MAP marginal *Soare*. Configuraţia MAP comună a staţiilor `S2, S3, S4` este (*Soare, Soare, Soare*) cu `P = 0.1621`, în timp ce maximele marginale luate separat dau (*Ploaie, Soare, Ploaie*) cu `P = 0.0857`. **Nu coincid** — suma şi maximul nu comută.

**Exerciţiul 3.** Graful MRF are 25 de noduri şi 40 de muchii; modelul are 210 parametri. Zgomotul inversează 3 pixeli. ICM converge în 2 treceri.

| λ | `E(x*; y)` | Pixeli greşiţi |
|---|---|---|
| 0.3 | 12.9 | 0 |
| 1 | 15.0 | 0 |
| 3 | 17.0 | 2 |

**Observaţie privind ArviZ/pyAgrum.** Codul a fost rulat cu `pyagrum 3.3.2` şi `pgmpy 1.1.2`.
