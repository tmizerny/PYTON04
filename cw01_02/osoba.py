osoba1 = {'imie': 'Jan',
          'nazwisko': 'Kowalski',
          'adres': 'Poznań',
          'płeć': True,
          'wiek': 22,
           }
osoba2 = {'imie': 'Anna',
          'nazwisko': 'Jabłońska',
          'adres': 'Szczecin',
          'płeć': False,
          'wiek': 18,
           }
osoba3 = {'imie': 'Tomasz',
          'nazwisko': 'Nowak',
          'adres': 'Wrocław',
          'płeć': True,
          'wiek': 30,
           }

osoba4 = {'imie': 'Alicja',
          'nazwisko': 'Młynarska',
          'adres': 'Poznań',
          'płeć': False,
          'wiek': 25,
           }

baza_osób = [osoba1,osoba2,osoba3,osoba4]
# #Wszyscy
# print(*baza_osób, sep='\n')
# print('-'*100)
# #Mezczyzni
def predykat_mezczyzn_z_poznania(osoba):
    return osoba['płeć'] and osoba['adres'] == 'Poznań'


mezczyzni_z_poznania = filter(predykat_mezczyzn_z_poznania, baza_osób)
# mezczyzni_z_poznania = [osoba for osoba in baza_osób if osoba['płeć'] and osoba['adres'] == 'Poznań']
# print(mezczyzni_z_poznania)
# print('-'*100)
def predykat_dwudziestolatkowie(osoba):
    return osoba['wiek'] in range(20, 30)


dwudziestolatkowie = filter(predykat_dwudziestolatkowie, baza_osób)
# dwudziestolatkowie = [osoba for osoba in baza_osób if osoba['wiek'] in range(20, 30)]
# print(*dwudziestolatkowie, sep='\n')
# wiek_kobiet = [osoba['wiek'] for osoba in baza_osób if osoba['imie'][0] == 'A' and not osoba['płeć']]
# if len(wiek_kobiet):
#     print(średnia := sum(wiek_kobiet) / len(wiek_kobiet))
# else:
#     print('Lista pusta')

print(*mezczyzni_z_poznania)
print(*dwudziestolatkowie)