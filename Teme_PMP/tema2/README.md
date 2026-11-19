# Tema 2 – Laboratorul 3

**Probabilităţi condiţionate. Formula lui Bayes**

## Exerciţiul 1

Se aruncă două zaruri, iar rezultatele sunt notate cu `X` şi `Y`.

1. Calculaţi probabilitatea ca suma să fie cel puţin 10, ştiind că primul zar indică un număr par.
2. Calculaţi probabilitatea ca suma să fie cel puţin 10, ştiind că cel puţin unul dintre zaruri indică un număr par.
3. Calculaţi probabilitatea ca ambele zaruri să indice numere pare, ştiind că suma lor este 8.
4. Sunt evenimentele `A = {X + Y ≥ 10}` şi `B = {X este par}` independente?

**Extensie Python:** Simulaţi 100.000 de aruncări şi estimaţi probabilităţile condiţionate. Comparaţi rezultatele cu valorile exacte.

## Exerciţiul 2 – Filtrarea mesajelor spam

Un sistem de e-mail primeşte 30% mesaje spam. Cuvântul „ofertă" apare în 80% dintre mesajele spam şi în 15% dintre mesajele legitime.

1. Care este probabilitatea ca un mesaj care conţine cuvântul „ofertă" să fie spam?
2. Presupunem că termenul „gratuit" apare în 60% dintre mesajele spam şi în 10% dintre mesajele legitime. Considerând independenţa condiţionată a apariţiei celor două cuvinte, calculaţi probabilitatea ca un mesaj care conţine ambele cuvinte să fie spam.
3. Explicaţi de ce ipoteza independenţei condiţionate poate fi nerealistă.
4. Propuneţi o regulă de clasificare bazată pe probabilitatea condiţionată.

## Exerciţiul 3 – Paradoxul lui Simpson

O universitate analizează rata de promovare la două discipline, A şi B, pentru studenţii din două programe de studiu:

| Program | Disciplina A | Disciplina B |
|---|---|---|
| Programul 1 | 81 din 90 | 19 din 20 |
| Programul 2 | 1 din 10 | 16 din 80 |

Valorile reprezintă numărul studenţilor promovaţi din totalul celor evaluaţi.

1. Calculaţi rata de promovare la fiecare disciplină, separat pentru fiecare program.
2. Care disciplină are o rată de promovare mai mare în fiecare program?
3. Calculaţi rata globală de promovare pentru cele două discipline.
4. Explicaţi de ce ordinea disciplinelor se inversează atunci când agregăm datele.
5. Formulaţi fenomenul în termeni de probabilităţi condiţionate.

**Extensie Python:** Construiţi un exemplu propriu de paradox Simpson şi utilizaţi librăria pandas pentru a analiza datele.

*Notă:* Pentru calculele teoretice, încărcaţi calculul fie în Markdown/LaTeX, fie ca foto la foaia de lucru.

---

## Conţinutul folderului

| Fişier | Conţinut |
|---|---|
| `calcule.md` | calculele teoretice pentru exerciţiile 1, 2 şi 3 |
| `ex1.py` | extensia Python a exerciţiului 1 (simulare 100.000 de aruncări) |
| `ex3.py` | extensia Python a exerciţiului 3 (exemplu propriu, analiză cu pandas) |
