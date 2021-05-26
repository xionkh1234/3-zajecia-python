paczka_count = 0
waga_count = 0
maks_kg_paczka = 20
ilosc_count = 0
suma_pustych = 0
min_paczka = 0
min_paczka_numer = 0
przedmiot = input()

if przedmiot:
    przedmiot = float(przedmiot)
while przedmiot:
    if przedmiot <= 1 or przedmiot > 10:
        break
    ilosc_count += przedmiot
    if min_paczka < (20 - ilosc_count):
        min_paczka = 20 - ilosc_count
        min_paczka_numer = waga_count
        ilosc_count = przedmiot
    if waga_count + przedmiot > 20:
        paczka_count += 1
        suma_pustych += maks_kg_paczka - waga_count
        waga_count = przedmiot
    elif waga_count + przedmiot <= 20:
        waga_count += przedmiot
    przedmiot = input()
    if przedmiot:
        przedmiot = float(przedmiot)
    if min_paczka < (20 - ilosc_count):
        min_paczka = 20 - ilosc_count
        min_paczka_numer = waga_count
        ilosc_count += przedmiot
if waga_count > 0:
    paczka_count += 1
    suma_pustych += maks_kg_paczka - waga_count
print("Paczek: {}, KG wysłanych: {}, łącznie pustych KG: {}, Najwięcej pustych KG w paczce nr: ".format(
    paczka_count,
    ilosc_count,
    suma_pustych,
    min_paczka_numer))
