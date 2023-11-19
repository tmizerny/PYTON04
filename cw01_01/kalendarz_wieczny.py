
def numer_dnia_tygodnia(data, sep):
    dzien, miesiac, rok = data.split(sep)
    dzien, miesiac, rok = int(dzien), int(miesiac), int(rok)
    if miesiac < 3:
        z = rok - 1
        c = 0
    else:
        z = rok
        c = 2
    return (23 * miesiac // 9 + dzien + 4 + rok + z // 4 - z // 100 + z // 400 - c) % 7


def nazwa_dnia_tygodnia(numer_dnia_tygodnia):
    tydzien = 'niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota'
    return tydzien[numer_dnia_tygodnia]


def jaki_to_dzień(data, sep='-'):
    numer = numer_dnia_tygodnia(data, sep)
    nazwa = nazwa_dnia_tygodnia(numer)
    print(nazwa)

jaki_to_dzień('19/11/2023','/')

