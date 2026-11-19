# Programare şi modelare probabilistă (PMP) — teme

Rezolvările temelor de laborator, Facultatea de Informatică, UAIC Iaşi.

| Folder | Temă | Subiect |
|---|---|---|
| [`tema1/`](tema1) | Tema 1 – Laboratorul 2 | Simularea variabilelor aleatoare |
| [`tema2/`](tema2) | Tema 2 – Laboratorul 3 | Probabilităţi condiţionate. Formula lui Bayes |
| [`tema3/`](tema3) | Tema 3 – Laboratorul 4 | Reţele Bayesiene |
| [`tema4/`](tema4) | Tema 4 – Laboratorul 5 | Reţele Markov: independenţă, predicţie, restaurarea imaginilor |
| [`tema5/`](tema5) | Tema 5 – Laboratorul 5 | Modele Markov ascunse (HMM) |
| [`tema6/`](tema6) | Tema 6 – Laboratorul 7 | Inferenţă Bayesiană şi simulare probabilistică |

Fiecare folder conţine propriul `README.md` cu enunţul complet, rezultatele numerice şi lista fişierelor.

## Structura unei teme

- `ex*.py` — rezolvările în Python, cu subpunctele marcate `# a)`, `# b)` etc., în ordinea din enunţ;
- `*.md` — părţile teoretice (demonstraţii şi calcule cerute pe hârtie);
- `README.md` — enunţul temei şi rezultatele.

## Cum se rulează

Fiecare script se rulează independent, din folderul temei:

```bash
cd tema1
python3 ex1.py
```

## Pachete folosite

```
numpy  scipy  matplotlib  pandas  networkx  arviz  pgmpy  pyagrum
```

Instalare:

```bash
pip install numpy scipy matplotlib pandas networkx arviz pgmpy pyagrum
```

**Versiuni cu care a fost rulat codul:** `numpy 2.5.3`, `scipy 1.18.1`, `pandas 3.0.5`, `networkx 3.7`, `arviz 1.3.0`, `pgmpy 1.1.2`, `pyagrum 3.3.2`.
