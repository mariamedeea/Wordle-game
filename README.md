# Wordle-game

Programul "main.py" reprezintă o clonă a jocului Wordle – generează numărul de încercări pentru a găsi un cuvânt dat și îl afișează pentru fiecare. Cuvintele sunt introduse continuu.

 Programul "Program.py" conține algoritmul de bază care rezolvă jocul și afișează cuvintele încercate și feedback-ul. Cele două programe comunică prin fișierul "inout.txt", unde sunt introduse cuvintele “cheie”, plus încercările.

Pentru a afla entropia, algoritmul calculează frecvența fiecărei litere pe fiecare poziție și o stochează într-un dicționar. Calculează probabilitatea ca fiind frecvența literei pe poziția corespunzătoare/numărul total de cuvinte. Entropia este apoi calculată cu formula E= Σ (p(x)*log2(1/p(x))), unde p(x) este probabilitatea.

Prima dată calculăm entropia doar pentru cuvintele cu litere distincte.

Următorul guess este cuvântul cu cea mai mare entropie, acum fiind calculată în funcție de toate cuvintele. Apelăm funcția “functie“ pentru feedback. Vom primi: ‘n’- litera nu este în cuvânt, ‘g’ - litera este în cuvânt, dar nu pe poziția respectivă, ‘v’ - litera este în cuvânt, pe aceeași poziție.

Din lista inițială de cuvinte scoatem cuvintele care au litere pentru care am primit feedback 'n' ( adică litera respectivă nu este în cuvântul cheie), cuvintele care au literele corespunzătoare pe poziția unde feedback-ul este 'g' ( litera respectivă este in cuvânt, dar nu este pe poziția respectivă) și, în cazul în care avem feedback 'v' (litera este pe poziția corectă), adăugăm condiția ca un cuvânt să rămână în listă numai dacă litera coincide.

exemplu :
cheie : BUNIC
cuvânt introdus : BANCA
feedback : vnvgn

Deci, scoatem cuvintele care conțin 'A', dar și pe cele care au 'C' pe poziția 4. În același timp, vor fi eliminate și cuvintele care nu au pe pozițiile 0 și 2 litera 'B', respectiv 'N'.

Toate acestea sunt implementate intr-un while, în 'Program.py'.
Media noastra de încercări este de: 5.54

Pentru rulare trebuie mai intai compilat main.py, si in timp ce il compileaza, se da compilare si la program.py, iar inout.txt trebuie sa fie mereu gol (inainte de compilare).
