import random
from time import sleep
new=False
first_time=True
y = random.randint(0, 11454)
with open("cuvinte.in", "r") as f:
    lista_cuvinte = f.read().splitlines()
cheie = lista_cuvinte[y]
g = open("inout.txt", "w+")
print("Cheia este: ", cheie)
g.write(f"{cheie}\n\n")
last_number=0
while True:
    text=g.read()
    g.seek(0)
    if len(text.splitlines())>=3 and cheie==text.splitlines()[-1]:
        print(f"A fost ghichita in {(len(text.splitlines())-last_number-2 if last_number else len(text.splitlines())-2)//2} incercari")
        y = random.randint(0, 11454)
        cheie = lista_cuvinte[y]
        print("Cheia este: ", cheie)
        g.write(f"{cheie}\n\n")
        last_number = len(text.splitlines())-2
g.close()