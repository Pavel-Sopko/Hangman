import os
from random import choice
import figurka
vyber_slov = ["petrzel", "jablko", "brambora", "cibule", "mrkev", "kedlubna", "paprika"]
#v realu by se vytvořil zvlást soubor s vice slovy a provedl import
zivoty = 7
hra_probiha = True


def vytvor_tajenku():
    return (slovo := choice(vyber_slov), len(slovo) * ["_"])


def aktualni_stav_hry(zivoty: int, hra_probiha: bool, tajenka: list) -> None:
    """funkce na proveveri stavu hry + vytisk obrazku hangman"""
    os.system("clear")
    stav = f"Tajenka: {' '.join(tajenka)}", f"ZIVOTY: {zivoty}"
    print("Hádej slovo z kategorie zelenina.")
    print(stav, figurka.hangman[7 - zivoty], sep="\n")
    if "_" not in tajenka:
        print("SUPER, UHODL JSI TAJNE SLOVO!")
        exit()
    elif not hra_probiha and zivoty:
        print("SUPER, UHODL JSI TAJNE SLOVO!")
    elif not zivoty:
        print(f"PROHRAL JSI, TAJNE SLOVO BYLO *{slovo}*")


def zkontroluj_pismeno(slovo, tajenka, hadani):
    for index, pismeno in enumerate(slovo):
        if pismeno == hadani:
            tajenka[index] = hadani


slovo, tajenka = vytvor_tajenku()
while hra_probiha and zivoty > 0:
    aktualni_stav_hry(zivoty, hra_probiha, tajenka)
    hadani = input("HADEJ PISMENO NEBO CELE SLOVO: ").lower()
    if slovo == hadani:
        hra_probiha = False
    elif len(hadani) == 1 and hadani in slovo:
        zkontroluj_pismeno(slovo, tajenka, hadani)
    else:
        zivoty -= 1
aktualni_stav_hry(zivoty, hra_probiha, tajenka)
