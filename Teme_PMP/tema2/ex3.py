import pandas as pd

# Exemplu propriu: doua metode de predare, testate pe doua grupe de niveluri diferite
date = pd.DataFrame({
    "metoda":    ["A", "A", "B", "B"],
    "grupa":     ["incepatori", "avansati", "incepatori", "avansati"],
    "promovati": [18, 48, 55, 15],
    "total":     [20, 80, 70, 30],
})

date["rata"] = date["promovati"] / date["total"]
print("Rate pe grupe:")
print(date)

# agregam peste grupe si recalculam raportul
total = date.groupby("metoda")[["promovati", "total"]].sum()
total["rata"] = total["promovati"] / total["total"]
print()
print("Rate globale:")
print(total)

print()
print("Metoda A e mai buna in ambele grupe, dar mai slaba global:")
print("a fost aplicata majoritar avansatilor, unde ratele sunt mici oricum.")
