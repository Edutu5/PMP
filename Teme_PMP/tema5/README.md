# Tema 5 – Laboratorul 5

**Modele Markov ascunse (HMM)**

> *Observaţie:* antetul fişierului PDF al enunţului este „Tema 4 – Laboratorul 5"; numerotarea folosită aici urmează numele fişierului, `tema_5.pdf`.

**Obiectiv.** La finalul temei, veţi putea explica algoritmul Forward şi implementa algoritmul Viterbi pentru identificarea celei mai probabile secvenţe de stări ascunse, pornind de la o secvenţă de observaţii.

## Exerciţiul 1. Cum calculăm probabilitatea unei secvenţe de observaţii? (Forward)

Considerăm un model Markov ascuns cu stări ascunse `X₁, …, X_T` şi observaţii `O₁, …, O_T`. Notăm prin `πᵢ = P(X₁ = i)` distribuţia iniţială, prin `aᵢⱼ = P(X_{t+1} = j | X_t = i)` probabilităţile de tranziţie şi prin `bⱼ(o) = P(O_t = o | X_t = j)` probabilităţile de emisie.

Pentru o secvenţă de observaţii `o₁, …, o_T`, definim variabila Forward

```
α_t(j) = P(O₁ = o₁, …, O_t = o_t, X_t = j)
```

a) **Iniţializare.** Explicaţi de ce `α₁(j) = πⱼ bⱼ(o₁)`.

b) **Recurenţă.** Folosind formula probabilităţii totale şi proprietatea Markov, demonstraţi că

```
α_t(j) = bⱼ(o_t) · Σᵢ α_{t−1}(i) aᵢⱼ,    t = 2, …, T
```

*Indiciu:* condiţionaţi după starea ascunsă `X_{t−1}` şi separaţi probabilitatea observaţiei curente.

c) **Finalizare.** Arătaţi că probabilitatea întregii secvenţe observate este

```
P(O₁ = o₁, …, O_T = o_T) = Σⱼ α_T(j)
```

*De predat:* o demonstraţie scurtă, în LaTeX/Markdown sau o fotografie lizibilă. Nu este necesar cod Python.

## Exerciţiul 2. Putem deduce dificultatea testelor din notele obţinute? (Viterbi)

Reluaţi exerciţiul de la laborator, de data aceasta implementând direct algoritmul Viterbi descris în cursul 4.

a) **Definirea modelului.** Scrieţi distribuţia iniţială `π`, matricea de tranziţie `A` (rânduri şi coloane în ordinea D, M, U) şi matricea de emisie `B` (coloane în ordinea FB, B, S, NS). Verificaţi că fiecare rând din `A` şi `B` are suma 1.

b) **Iniţializarea Viterbi.** Definiţi `δ_t(j)` drept probabilitatea comună maximă a unei secvenţe de stări care se termină în `j` la momentul `t`, împreună cu observaţiile până la `t`. Calculaţi `δ₁(j) = πⱼ bⱼ(o₁)` pentru fiecare stare `j`.

c) **Implementarea recurenţei.** Implementaţi în Python, fără a apela o funcţie Viterbi gata construită,

```
δ_t(j) = bⱼ(o_t) · maxᵢ (δ_{t−1}(i) aᵢⱼ),    ψ_t(j) = argmaxᵢ (δ_{t−1}(i) aᵢⱼ)
```

Explicaţi pe scurt rolul lui `ψ_t(j)`. *Indiciu:* folosiţi două tabele, unul pentru scoruri şi unul pentru indicii stărilor precedente.

d) **Verificare intermediară.** Afişaţi valorile `δ₁` şi `δ₂` (după primele două note FB). Verificaţi manual cel puţin un calcul din `δ₂`.

e) **Reconstrucţia traseului.** Alegeţi starea finală cu scor maxim şi reconstituiţi, în ordine inversă, întreaga secvenţă de 12 dificultăţi folosind `ψ`. Afişaţi secvenţa rezultată şi valoarea `max P(x₁, …, x₁₂, o₁, …, o₁₂)`.

f) **Interpretare.** Explicaţi de ce Viterbi caută cea mai probabilă *secvenţă completă* de dificultăţi, nu neapărat cea mai probabilă dificultate separat la fiecare test. Precizaţi că scorul de la punctul e) este o probabilitate *comună*, nu probabilitatea condiţionată a traseului dat fiind şirul notelor.

**Opţional.** Calculaţi probabilitatea secvenţei de note prin Forward şi determinaţi `P(x* | o) = P(x*, o) / P(o)`. Comparaţi implementarea proprie cu rezultatul unei biblioteci Python, dacă doriţi. *(Nu a fost inclus.)*

---

## Conţinutul folderului

| Fişier | Conţinut |
|---|---|
| `ex1.md` | exerciţiul 1 – demonstraţia Forward, subpunctele a) – c) |
| `ex2.py` | exerciţiul 2, subpunctele a) – f) |

## Rezultate

Secvenţa de note observată: **FB, FB, S, B, B, S, B, B, NS, B, B, S**.

```
δ₁ = (0.033333, 0.050000, 0.066667)
δ₂ = (0.003333, 0.002500, 0.003333)
```

Secvenţa de dificultăţi cea mai probabilă:

```
D, U, D, U, D, M, D, U, D, U, D, M
```

cu `max P(x₁, …, x₁₂, o₁, …, o₁₂) = 2.109375 × 10⁻¹¹`.

**Observaţie asupra unicităţii.** La primul test există egalitate: `π_D · b_D(FB) · A[D][U] = π_U · b_U(FB) · A[U][U]`, deci secvenţa care începe cu U are exact aceeaşi probabilitate. `argmax` alege primul indice, de unde D. O bibliotecă ce rupe egalitatea altfel poate întoarce cealaltă secvenţă — ambele sunt optime.

**Observaţie asupra structurii.** În secvenţa găsită, D nu apare niciodată de două ori la rând. Nu s-a impus nimic: este constrângerea `A[D][D] = 0`, care anulează orice traseu cu două teste dificile consecutive.
