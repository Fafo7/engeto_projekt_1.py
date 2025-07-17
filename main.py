"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Filip Trepáň
email: filip.trepan@gmail.com
"""
oddelovac = "=" * 30

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# registrovaný uživatelia a ich hesla
uzivatelia = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

meno = input("Zadej své jméno: ").lower()
heslo = input("Zadej své heslo: ")
print(oddelovac)

# kontrola uživateľa
if meno in uzivatelia and uzivatelia[meno] == heslo:
    print(f"Welcome to the app, {meno}!")
else:
    print("unregistered user, terminating the program...")
    exit()

# analýza textov
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(oddelovac)

while True:
    zadaj_cislo = input("Enter a number between 1 and 3 to select a text: ")

    if not zadaj_cislo.isdigit():
        print("Invalid input, please enter a number.")
        continue
    cislo = int(zadaj_cislo)

    if 1 <= cislo <= 3:
        break
    else:
        print("Number out of range. Please try again.")
        
print(f"You selected text number {cislo}.")
print(oddelovac)

# práca s textom
text = TEXTS[cislo - 1]
slova = text.split()
pocet_slov = len(slova)
velke_pismena = sum(1 for slovo in slova if slovo.istitle())
velke_slova = sum(1 for slovo in slova if slovo.isupper())
male_slova = sum(1 for slovo in slova if slovo.islower())
ciselny_str = sum(1 for slovo in slova if slovo.isdigit())
sucet_cisel = sum(int(slovo) for slovo in slova if slovo.isdigit())

print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {velke_pismena} titlecased words in the selected text.")
print(f"There are {velke_slova} uppercase words in the selected text.")
print(f"There are {male_slova} lowercase words in the selected text.")
print(f"There are {ciselny_str} numeric strings in the selected text.")
print(f"The sum of all the numbers: {sucet_cisel}.")
print(oddelovac)

# počítanie výskytov slov
sucet = {}
for slovo in slova:
    dlzka = len(slovo.strip(".,!?"))
    if dlzka not in sucet:
        sucet[dlzka] = 0
    sucet[dlzka] += 1

print("LEN | OCCURRENCES        | NR.")
print(oddelovac)

for dlzka in sorted(sucet):
    pocet = sucet[dlzka]
    hviezdy = "*" * pocet
    print(f"{dlzka:>3} | {hviezdy:<18} | {pocet}")