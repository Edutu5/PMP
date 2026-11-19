# Tema 3 – Exerciţiul 2, subpunctul d)

Calculul celor două probabilităţi cu regula lui Bayes, pornind de la factorizarea reţelei.

## Modelul

Structura este $B \to T$, $B \to X$, $(B, T) \to D$, deci distribuţia comună se factorizează:

$$P(B, T, X, D) = P(B) \, P(T \mid B) \, P(X \mid B) \, P(D \mid B, T)$$

Date:

$$P(B{=}1) = 0.1, \quad P(B{=}0) = 0.9$$
$$P(T{=}1 \mid B{=}1) = 0.8, \quad P(T{=}1 \mid B{=}0) = 0.3$$
$$P(X{=}1 \mid B{=}1) = 0.9, \quad P(X{=}1 \mid B{=}0) = 0.1$$
$$P(D{=}1 \mid B{=}1, T{=}1) = 0.9, \quad P(D{=}1 \mid B{=}1, T{=}0) = 0.4$$
$$P(D{=}1 \mid B{=}0, T{=}1) = 0.5, \quad P(D{=}1 \mid B{=}0, T{=}0) = 0.1$$

---

## Subpunctul b): $P(B = 1 \mid T = 1, D = 1)$

Regula lui Bayes:

$$P(B{=}1 \mid T{=}1, D{=}1) = \frac{P(B{=}1, T{=}1, D{=}1)}{P(T{=}1, D{=}1)}$$

**Numărătorul.** Variabila $X$ nu apare în interogare şi nici în evidenţă, deci o eliminăm prin însumare. Fiind o frunză, factorul ei sumează la 1 şi dispare:

$$\sum_{x} P(X{=}x \mid B) = 1$$

Rămâne

$$P(B, T, D) = P(B) \, P(T \mid B) \, P(D \mid B, T)$$

$$P(B{=}1, T{=}1, D{=}1) = 0.1 \cdot 0.8 \cdot 0.9 = 0.072$$

**Numitorul.** Prin formula probabilităţii totale după $B$:

$$P(B{=}0, T{=}1, D{=}1) = 0.9 \cdot 0.3 \cdot 0.5 = 0.135$$

$$P(T{=}1, D{=}1) = 0.072 + 0.135 = 0.207$$

**Rezultatul.**

$$P(B{=}1 \mid T{=}1, D{=}1) = \frac{0.072}{0.207} = \frac{72}{207} = \frac{8}{23} \approx 0.3478$$

Priorul de 10% urcă la aproximativ **34.8%**: cele două simptome cresc de peste trei ori plauzibilitatea bolii, dar rămân departe de certitudine, fiindcă ele apar frecvent şi la pacienţii sănătoşi.

---

## Subpunctul c): $P(X = 1 \mid B = 0, T = 1, D = 1)$

Aici nu mai este nevoie de niciun calcul, dacă folosim independenţele condiţionate ale modelului.

În reţea, singurul drum de la $X$ la $T$ este $X \leftarrow B \to T$, iar singurele drumuri de la $X$ la $D$ sunt $X \leftarrow B \to D$ şi $X \leftarrow B \to T \to D$. Toate trec prin $B$, iar $B$ nu este collider pe niciunul dintre ele. **Condiţionând pe $B$, toate drumurile se blochează**, deci

$$X \perp\!\!\!\perp \{T, D\} \mid B$$

Aceasta este chiar proprietatea Markov locală (Cursul 2, slide 13): $X$ este independentă de nedescendenţii săi, dat fiind părintele său $B$.

Prin urmare evidenţa despre tuse şi respiraţie devine irelevantă odată ce boala este cunoscută:

$$P(X{=}1 \mid B{=}0, T{=}1, D{=}1) = P(X{=}1 \mid B{=}0) = \boxed{0.1}$$

**Verificare directă**, fără a folosi independenţa:

$$P(X{=}1 \mid B{=}0, T{=}1, D{=}1) = \frac{P(X{=}1, B{=}0, T{=}1, D{=}1)}{P(B{=}0, T{=}1, D{=}1)}$$

$$= \frac{P(B{=}0) P(T{=}1 \mid B{=}0) P(D{=}1 \mid B{=}0, T{=}1) \, P(X{=}1 \mid B{=}0)}{P(B{=}0) P(T{=}1 \mid B{=}0) P(D{=}1 \mid B{=}0, T{=}1)}$$

$$= \frac{0.9 \cdot 0.3 \cdot 0.5 \cdot 0.1}{0.9 \cdot 0.3 \cdot 0.5} = \frac{0.0135}{0.135} = 0.1$$

Factorii comuni se simplifică exact, ceea ce este forma algebrică a aceleiaşi independenţe condiţionate.
