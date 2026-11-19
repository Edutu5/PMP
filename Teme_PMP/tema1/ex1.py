import csv
import random

with open("studenti.csv", encoding="utf-8") as f:
    studenti = [rand[0] for rand in csv.reader(f) if rand]

k = 3

alesi = random.sample(studenti, k)

print("Studenti extrasi:")
for nume in alesi:
    print(" -", nume)