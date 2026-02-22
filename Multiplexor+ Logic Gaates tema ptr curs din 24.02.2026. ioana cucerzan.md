Multiplexorul 2:1 este un circuit combinațional care are două intrări de date și o singură ieșire, iar selecția intrării transmise la ieșire se face cu ajutorul unei linii 
de control (S).
În funcție de valoarea selectorului, multiplexorul trimite la ieșire fie intrarea I0, fie intrarea I1.

# Multiplexor 2:1
# I0 si I1 sunt intrarile
# S este selectorul

def multiplexor_2_la_1(I0, I1, S):
    if S == 0:
        return I0
    else:
        return I1

# Exemplu de utilizare
I0 = 0
I1 = 1
S = 1

iesire = multiplexor_2_la_1(I0, I1, S)
print("Iesirea este:", iesire)


Multiplexorul 2:1 are două intrări: I0 și I1
Are o singură linie de selecție: S
Dacă S = 0, ieșirea = I0
Dacă S = 1, ieșirea = I1


Multiplexorul 4:1 este un circuit combinațional care are patru intrări de date și o singură ieșire, iar selecția intrării transmise la ieșire se face cu ajutorul 
a două linii de control (S1 și S0).
Combinația binară formată din S1S0 este transformată în număr zecimal, iar acel număr indică intrarea care va fi conectată la ieșire.




Porți logice în Python
Ultima actualizare: 11 iulie 2025

Porțile logice sunt elementele de bază ale sistemelor digitale. Ele funcționează primind una sau mai multe intrări binare (0 sau 1) și producând o singură ieșire binară, 
în funcție de o regulă logică. Fiecare poartă are un comportament diferit, în funcție de valorile pe care le primește.

Cu Python putem simula foarte ușor comportamentul acestor porți, fără a avea nevoie de hardware fizic. Astfel, înțelegerea circuitelor digitale devine mult mai accesibilă.
 
1. Poarta AND
Poarta AND produce o ieșire de 1 doar dacă toate intrările sunt 1. În orice alt caz, ieșirea va fi 0.
def poarta_AND(*intrari):
    for intrare in intrari:
        if intrare == 0:
            return 0
    return 1
# Exemplu de utilizare
print(poarta_AND(1, 1, 1))  # Output: 1
print(poarta_AND(1, 0, 1))  # Output: 0


Poarta OR
Poarta OR verifică dacă cel puțin una dintre intrări este 1.
Dă 0 doar când ambele sunt 0.

Exemplu: print("A B | Output")
for a in [0, 1]:
    for b in [0, 1]:
        res = a | b
        print(f"{a} {b} |   {res}")



Poarta NOT
Poarta NOT are o singură intrare și o inversează.
1 devine 0, iar 0 devine 1.
Se mai numește și invertor.

Exemplu:
 print("A | Output")
for a in [0, 1]:
    res = 1 if a == 0 else 0
    print(f"{a} |   {res}")


4. Poarta NAND
Poarta NAND este opusul porții AND.
Dă 0 doar când ambele intrări sunt 1.
În rest, dă 1.

Exemplu:
print("A B | Output")
for a in [0, 1]:
    for b in [0, 1]:
        res = 0 if a & b else 1
        print(f"{a} {b} |   {res}")

5. Poarta NOR
Poarta NOR este opusul porții OR.
Dă 1 doar când ambele intrări sunt 0.
Dacă una este 1, ieșirea devine 0.

Exemplu:

print("A B | Output")
for a in [0, 1]:
    for b in [0, 1]:
        res = 0 if a | b else 1
        print(f"{a} {b} |   {res}")

6. Poarta XOR
Poarta XOR dă 1 când intrările sunt diferite.
Dacă sunt la fel, dă 0.

Exemplu:

print("A B | Output")
for a in [0, 1]:
    for b in [0, 1]:
        res = a ^ b
        print(f"{a} {b} |   {res}")

7. Poarta XNOR
Poarta XNOR este opusul porții XOR.
Dă 1 când intrările sunt egale.
Dacă sunt diferite, dă 0.

Exemplu:

print("A B | Output")
for a in [0, 1]:
    for b in [0, 1]:
        res = 1 if a == b else 0
        print(f"{a} {b} |   {res}")



Networking în Python se face cu biblioteca socket.

Un program poate fi server (ascultă) sau client (se conectează).

Comunicarea se face prin send() și recv().

Serverul folosește: bind(), listen(), accept().

Clientul folosește: connect().
Networking în Python înseamnă să scrii programe care pot comunica între ele prin rețea — fie pe același calculator, fie pe internet.
Python are o bibliotecă standard numită socket, care permite:

trimiterea și primirea de date

crearea de servere

conectarea la servere

comunicarea între două programe

Este baza pentru chat-uri, jocuri multiplayer, servere web, aplicații client–server etc.

Două concepte importante
1. Server
Așteaptă conexiuni.

Primește cereri.

Trimite răspunsuri.

2. Client
Se conectează la server.

Trimite cereri.

Primește răspunsuri.



Token = o unitate mică de informație.

În programare: bucățică de cod.

În AI: fragment de text.

În securitate: cod de acces.

În blockchain: activ digital.



Pe GitHub, un fork este o copie completă a unui proiect în contul tău.

Îl folosești când:

vrei să modifici un proiect fără să strici originalul

vrei să contribui la un proiect open‑source

vrei să experimentezi în siguranță

Pe scurt:  
Fork = copie a unui repository pe care o poți modifica liber.
Fork = ramificare sau copiere a unui proiect.

În GitHub: copie a unui repository pentru modificări.

În sisteme de operare: procesul creează un proces copil.

În blockchain: rețeaua se împarte în două versiuni.

Un branch este o ramură de dezvoltare într-un proiect.

Poți lucra pe un branch fără să strici codul principal.

Poți testa idei noi.

Poți dezvolta funcționalități separate.

Pe scurt:  
Branch = o ramură paralelă a proiectului, unde poți lucra independent.

Git = sistem de control al versiunilor.  
Permite salvarea, urmărirea și gestionarea modificărilor dintr-un proiect.
Ajută la lucrul în echipă, la revenirea la versiuni vechi și la dezvoltarea în ramuri separate (branch-uri).
Comenzi importante: add, commit, push, pull.
Git = sistem de control al versiunilor.

Repo = proiect + istoric.

Commit = salvare a unei versiuni.

Branch = ramură separată pentru dezvoltare.

Merge = unirea ramurilor.

Push = trimiți pe GitHub.

Pull = aduci modificări de pe GitHub.


Dependență = relație în care un element are nevoie de altul ca să funcționeze.

În Python: biblioteci sau funcții necesare programului.

În proiecte software: pachete externe instalate cu pip.




