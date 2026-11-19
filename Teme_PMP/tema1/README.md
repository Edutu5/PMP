# Tema 1 – Laboratorul 2

**Simularea variabilelor aleatoare**

## Exerciţiul 1

Scrieţi un program în Python care să preia ca input un fişier `.csv` cu o listă oarecare şi să aibă ca output un număr predeterminat de elemente din acea listă, fără repetiţie. Aplicaţi pe lista studenţilor din grupa dumneavoastră care nu au prezentat încă o temă.

*Notă:* Pentru generarea unui eşantion aleator se poate apela funcţia `sample` din modulul `random` sau funcţia `random.choice` cu argumentul `replace=False` din librăria NumPy.

## Exerciţiul 2

Doi prieteni joacă următorul joc, după următoarele reguli:

**Pasul 1.** Primul jucător aruncă cu o monedă.

- Dacă pică stemă, cel de-al doilea trebuie să arunce cu zarul şi să-i dea primului o sumă egală cu `z – 3` $, unde `z` este rezultatul aruncării cu zarul (a da o sumă negativă este echivalent cu a lua opusul acelei sume). Jocul se încheie aici.
- Dacă pică ban, atunci primul jucător trebuie să-i dea celui de-al doilea 0.5 $.

**Pasul n.** În caz că jocul nu s-a încheiat, se reia pasul 1.

Astfel, jocul se opreşte la pasul corespunzător obţinerii stemei de către primul jucător.

a) Ce fel de distribuţie urmează `N`, numărul de paşi ai jocului?

b) Simulaţi în Python un astfel de joc. Variabilele care ne interesează sunt `N` şi suma totală `S` pe care cel de-al doilea jucător trebuie să i-o dea primului.

c) Prin simularea unui număr mare de astfel de jocuri, determinaţi cu aproximaţie media lui `S` şi reprezentaţi grafic (printr-o histogramă) distribuţia acesteia.

d) Ce se întâmplă dacă moneda este măsluită? Încercaţi să refaceţi pct. c) cu o probabilitate de apariţie a stemei `p = 0.3`, respectiv `p = 0.7`.

## Exerciţiul 3

Într-o frizerie, trei frizeri îşi tund clienţii cu următoarele viteze *medii*: primul cu 3 clienţi pe oră, al doilea cu 6 pe oră iar al treilea cu 4 pe oră. Astfel, timpul de servire al unui client este modelat de distribuţii exponenţiale cu parametrii `λ₁ = 3 h⁻¹`, `λ₂ = 6 h⁻¹`, respectiv `λ₃ = 4 h⁻¹`, iar probabilităţile de preluare a unui client de către un anumit frizer sunt 3/13, 6/13, respectiv 4/13 (de ce?). Fie `X` timpul de servire pentru un client.

Generaţi 10000 de valori pentru `X`, şi în felul acesta estimaţi media şi deviaţia standard a lui `X`. Realizaţi un grafic aproximativ al densităţii distribuţiei lui `X`.

*Notă:* Distribuţia `Exp(λ)` se poate apela prin `random.exponential(scale=1/λ)` în NumPy, sau cu `stats.expon(scale=1/λ)` în SciPy. Având în vedere că `X` are o distribuţie continuă, densitatea aproximativă a acesteia se poate vizualiza folosind funcţia `plot_kde` din librăria ArviZ.

---

## Conţinutul folderului

| Fişier | Conţinut |
|---|---|
| `studenti.csv` | lista de intrare pentru exerciţiul 1 — conţine doar studenţii care nu au prezentat încă o temă |
| `ex1.py` | exerciţiul 1 |
| `ex2.py` | exerciţiul 2, subpunctele a) – d) |
| `ex3.py` | exerciţiul 3 |
