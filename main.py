paczka_count = 0
waga_count = 0
maks_kg_paczka = 0
ilosc_count = 0
suma_pustych = 0
paczka_min = 0
przedmiot = input()

if przedmiot:
    przedmiot = float(przedmiot)
while przedmiot:
    print(przedmiot)
    if przedmiot <= 1 or przedmiot > 10:
        break
    elif waga_count + przedmiot > 20:
        paczka_count += 1
        suma_pustych += maks_kg_paczka - waga_count
        waga_count = przedmiot
    elif waga_count + przedmiot <= 20:
        waga_count += przedmiot
    przedmiot = input()
    if przedmiot:
        przedmiot = float(przedmiot)
if waga_count > 0:
    paczka_count += 1
    suma_pustych += maks_kg_paczka - waga_count


x = 20 * (paczka_count + 1) - waga_count
print("Paczek: {}, Kilogramów: {}, Suma kilogramów wysłanych: {}, łącznie pustych kg w paczce: {}".format(
    paczka_count,
    waga_count,
    ilosc_count,
    20 * paczka_count - waga_count))
