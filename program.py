from collections import OrderedDict
import math
import random
from time import sleep

y = random.randint(0, 11454)

feedback = []


def functie(cheie, x):            #returneaza feedback-ul cuvantului
    feedback = []
    frecventa = {chr(x): 0 for x in range(ord('A'), ord('Z') + 1)}

    for i in cheie:
        frecventa[i] += 1

    for j in range(5):
        if x[j] == cheie[j]:
            feedback.append('v')
        elif frecventa[x[j]] > 0:
            feedback.append('g')
        else:
            feedback.append('n')

    return feedback


def entropie(lista_cuvinte):                    #returneaza cuvantul din lista cu cea mai mare entropie
    maxi = 0
    nr = len(lista_cuvinte)
    position_1 = {c: 0 for c in letter}
    position_2 = {c: 0 for c in letter}
    position_3 = {c: 0 for c in letter}
    position_4 = {c: 0 for c in letter}
    position_5 = {c: 0 for c in letter}

    for w in lista_cuvinte:
        if w:
            if w[0] in position_1:
                position_1[w[0]] = position_1[w[0]] + 1
            else:
                position_1[w[0]] = 1

    for w in lista_cuvinte:
        if w:
            if w[1] in position_2:
                position_2[w[1]] = position_2[w[1]] + 1
            else:
                position_2[w[1]] = 1

    for w in lista_cuvinte:
        if w:
            if w[2] in position_3:
                position_3[w[2]] = position_3[w[2]] + 1
            else:
                position_3[w[2]] = 1

    for w in lista_cuvinte:
        if w:
            if w[3] in position_4:
                position_4[w[3]] = position_4[w[3]] + 1
            else:
                position_4[w[3]] = 1

    for w in lista_cuvinte:
        if w:
            if w[4] in position_5:
                position_5[w[4]] = position_5[w[4]] + 1
            else:
                position_5[w[4]] = 1
    dict1 = OrderedDict(sorted(position_1.items()))
    dict2 = OrderedDict(sorted(position_2.items()))
    dict3 = OrderedDict(sorted(position_3.items()))
    dict4 = OrderedDict(sorted(position_4.items()))
    dict5 = OrderedDict(sorted(position_5.items()))

    dict1.values()
    dict1_values = list(dict1.values())

    dict2.values()
    dict2_values = list(dict2.values())

    dict3.values()
    dict3_values = list(dict3.values())

    dict4.values()
    dict4_values = list(dict4.values())

    dict5.values()
    dict5_values = list(dict5.values())

    probabilitate_position_1 = []
    probabilitate_position_2 = []
    probabilitate_position_3 = []
    probabilitate_position_4 = []
    probabilitate_position_5 = []

    for k in dict1_values:
        probabilitate_position_1.append(k / nr)

    for m in dict2_values:
        probabilitate_position_2.append(m / nr)

    for n in dict3_values:
        probabilitate_position_3.append(n / nr)

    for p in dict4_values:
        probabilitate_position_4.append(p / nr)

    for q in dict5_values:
        probabilitate_position_5.append(q / nr)

    x = 0
    l = 0
    j = 1
    e = 0
    for cuvant in lista_cuvinte:
        j = 1
        e = 0
        while j <= 5:
            for l in range(0, 5):
                for x in letter:
                    if x == cuvant[l] and j == 1:
                        e = e + (probabilitate_position_1[ord(x) - 65] * math.log2(
                            1 / probabilitate_position_1[ord(x) - 65]))
                        j += 1
                    elif x == cuvant[l] and j == 2:
                        e = e + (probabilitate_position_2[ord(x) - 65] * math.log2(
                            1 / probabilitate_position_2[ord(x) - 65]))
                        j += 1
                    elif x == cuvant[l] and j == 3:
                        e = e + (probabilitate_position_3[ord(x) - 65] * math.log2(
                            1 / probabilitate_position_3[ord(x) - 65]))
                        j += 1
                    elif x == cuvant[l] and j == 4:
                        e = e + (probabilitate_position_4[ord(x) - 65] * math.log2(
                            1 / probabilitate_position_4[ord(x) - 65]))
                        j += 1
                    elif x == cuvant[l] and j == 5:
                        e = e + (probabilitate_position_5[ord(x) - 65] * math.log2(
                            1 / probabilitate_position_5[ord(x) - 65]))
                        j += 1

        if e > maxi:
            maxi = e
            opener = cuvant
    return opener



letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

gasit = 0
feedback = []

m = 0
first=1
while True:
    f = open("inout.txt", "r")
    f = open("inout.txt", "r")
    cheie = f.readlines()[0]
    f.close()
    print(repr(cheie))
    gasit=0
    m=0
    with open("cuvinte.in", "r") as f:
        lista_cuvinte = f.read().splitlines()
    while True:
        first=0
        litere_eliminat = []
        feedback = []
        if m == 0:
            opener = "CAREI"
            m = 1
        elif m == 1:
            if len(lista_cuvinte) == 1:
                opener = lista_cuvinte[0]
            else:
                opener = entropie(lista_cuvinte)
        print(opener)
        f = open("inout.txt", "a")
        f.write(opener)
        f.write("\n")

        if opener == cheie.removesuffix("\n"):
            break
        else:
            feedback = functie(cheie.removesuffix("\n"), opener)

            p = 0
            print(*feedback)
            for l in feedback:
                if l == 'n':
                    litere_eliminat.append(opener[p])
                p = p + 1

            # print(litere_eliminat)
            cuvinte2 = []
            for c in lista_cuvinte:
                ok = 1
                for i in c:
                    if i in litere_eliminat:
                        ok = 0
                for i in range(5):
                    if feedback[i] == 'g':
                        if c[i] == opener[i]:
                            ok = 0
                for i in range(5):
                    if feedback[i] == 'v':
                        if c[i] != opener[i]:
                            ok = 0
                if ok == 1:
                    cuvinte2.append(c)

            lista_cuvinte = cuvinte2
            # print(lista_cuvinte)
            cuvinte2 = []
        f.close()
#print(*lista_cuvinte)