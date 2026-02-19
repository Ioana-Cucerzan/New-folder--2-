"""
Student solutions file.

IMPORTANT:
- Do not change function names/signatures.
- You may add helper functions/classes, but keep required API intact.
"""

from __future__ import annotations


# ----------------------------
# Part II — Problem 1
# ----------------------------
def parse_transactions(lines: list[str]) -> list[dict]:
    """
    Parse lines of format "name;category;amount" into dicts:
    {"name": str, "category": str, "amount": float}

    Invalid lines are ignored:
    - not exactly 3 fields
    - amount not a number
    """
    
    rezultat = [] 
    for linie in lines :
        bucati =linie.split (";")
        if len(bucati) != 3:
            continue
        try:
            suma = float(bucati[2])
        except:
            continue 
        rezultat.append({
            "name" : bucati[0],
            "category" : bucati[1],
            "amount": suma
        })    
    return rezultat
 

def totals_by_category(transactions: list[dict]) -> dict[str, float]:
    """
    Sum amounts by category.
    Output values are rounded to 2 decimals.
    """
    tot = {}
    for t in transactions:
        categorie = t["category"]
        suma = t["amount"]
        tot[categorie] = tot.get(categorie, 0) + suma
    for c in tot:
        tot[c] = round(tot[c], 2)
    return tot        


def top_spender(transactions: list[dict]) -> tuple[str | None, float]:
    """
    Return (name, total_spent) for the biggest spender.
    Ties: lexicographically smaller name wins.
    Empty input: (None, 0.0)
    """
    if not transactions:
        return (None, 0.0)
    totaluri = {}
    for t in transactions:
     totaluri[t["name"]] = totaluri.get(t["name"], 0) + t["amount"]
     nume_max, suma_max = None, 0.0
    for n, s in totaluri.items():
     if s > suma_max or (s == suma_max and (nume_max is None or n < nume_max)):
        nume_max, suma_max = n, s
    return (nume_max, round(suma_max, 2))



# ----------------------------
# Part II — Problem 2
# ----------------------------

def max_len_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Return the maximum length of a contiguous subarray with sum exactly k.
    Full-credit solution: O(n) using prefix sums and a dict of first occurrences.
    """
    suma = 0
    pozitii = {0: -1}
    maxim = 0
    for i, x in enumerate(nums):
        suma += x
        caut = suma - k
        if caut in pozitii:
            lung = i - pozitii[caut]
            if lung > maxim:
                maxim = lung
        if suma not in pozitii:
            pozitii[suma] = i
    return maxim



# ----------------------------
# Part III — Debugging
# ----------------------------

def average_per_student(records: list[tuple[str, int]]) -> tuple[str | None, float]:
    """
    Return (name, average) for the student with the highest average.
    Ties: choose lexicographically smaller name.
    Empty records: (None, 0.0)

    Task:
    - Write at least 6 issues of the original buggy code as comments here.
    - Then implement the corrected version.
    """
   

    # 1. nu verifica daca lista este goala
    # 2. nu aduna notele pe student, doar le suprascrie
    # 3. nu tine minte cate note are fiecare student
    # 4. calculeaza media gresit (foloseste doar ultima nota)
    # 5. nu rezolva egalitatea dupa nume (lexicografic)
    # 6. nu rotunjeste media la final

    if not records:
        return (None, 0.0)

    sume = {}
    count = {}

    for nume, nota in records:
        sume[nume] = sume.get(nume, 0) + nota
        count[nume] = count.get(nume, 0) + 1

    max_nume = None
    max_medie = 0.0

    for nume in sume:
        medie = sume[nume] / count[nume]
        if medie > max_medie or (medie == max_medie and (max_nume is None or nume < max_nume)):
            max_nume = nume
            max_medie = medie

    return (max_nume, round(max_medie, 2))


# ----------------------------
# Part IV — OOP mini-project
# ----------------------------

class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Validate:
        - title and author are non-empty after strip
        - year in [1450, 2026]
        Set is_borrowed = False initially.
        """
        class Book:
   
        # verific daca titlul e bun
         if not title.strip():
            raise ValueError("titlu gresit")
        # verific autorul
        if not author.strip():
            raise ValueError("autor gresit")
        # verific anul
        if year < 1450 or year > 2026:
            raise ValueError("an gresit")

        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False  # la inceput nu e luata

    def __str__(self) -> str:
        # fac textul afisat
        if self.is_borrowed:
            st = "BORROWED"
        else:
            st = "AVAILABLE"
        return f"{self.title} - {self.author} ({self.year}) [{st}]"


class Library:
    def __init__(self):
        self.books = []  # lista simpla

    def add_book(self, book: Book) -> None:
        # doar bag cartea in lista
        self.books.append(book)

    def find_by_author(self, author: str) -> list[Book]:
        gasite = []
        for c in self.books:
            if c.author == author:
                gasite.append(c)
        return gasite

    def borrow(self, title: str) -> bool:
        for c in self.books:
            if c.title == title and not c.is_borrowed:
                c.is_borrowed = True
                return True
        return False

    def return_book (self, title : str) -> bool:
        for c in self.books:
            if c.title == title and c.is_borrwed:
                c.is_borowed = False
                return True
        return False    
   


    def available_books(self) -> list[Book]:
        libere = []
        for c in self.books:
            if not c.is_borrowed:
                libere.append(c)
            return libere    

       
    
    def library_summary(lib: Library) -> dict[str, int]:
     total = len(lib.books)
     imprumutate = 0 
     for c in lib.books: 
      if c.is_borrowed:
         imprumutate += 1 
         libere = total - imprumutate 
     return {"total": total, "borrowed": imprumutate, "available": libere}