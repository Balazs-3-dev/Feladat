import random
import math

# 1 feladat
print("1 feladat")
jelszo = ""
while jelszo != "admin123":
    felhasznalo = input("Mi a felhasználónév: ")
    jelszo = input("Mi a jelszót: ")
    if jelszo == "admin123":
        print("Helyes")
    else:
        print("Helytelen")
while True:
    felhasznalo = input("Mi a felhasználónév: ")
    jelszo = input("Mi a jelszót:")
    if jelszo != "admin123":
        print("Helytelen")
    else:
        print("Helyes")
        break

# 2 feladat
print("2 feladat")
homerseklet = 0
while homerseklet > 15 or homerseklet < 25:
    homerseklet = int(input("Mennyi a szobahőmérséklet? "))
    if homerseklet > 15 or homerseklet < 25:
        break
    else:
        print("A hőmérséklet nem 15 és 25 között van")
while True:
    homerseklet = int(input("Mennyi a szobahőmérséklet? "))
    if homerseklet > 15 and homerseklet < 25:
        break
    else:
        print("A hőmérséklet nem 15 és 25 között van")

# 3 feladat
print("3 feladat")
szam = random.randint(1 , 100)
tipp = 0
print(szam)
while szam != tipp:
    tipp = int(input("Kérem adja meg a tippét 1 és 100 között:"))
    if szam == tipp:
        print("Találat")
        break
    elif szam > tipp:
        print("A szám nagyobb mint a tipped")
    elif szam < tipp:
        print("A szám kisebb mint a tipped") 
while True:
    tipp = int(input("Kérem adja meg a tippét 1 és 100 között:"))
    if szam == tipp:
        print("Találat")
        break
    elif szam > tipp:
        print("A szám nagyobb mint a tipped")
    elif szam < tipp:
        print("A random szám kisebb mint a tipped")

# 4 feladat
print("4 feladat")
pin = 1234
jelszo = 0
while pin != jelszo:
    jelszo = int(input("Kérem adja meg a PIN kódját."))
    if pin == jelszo:
        print("A Pinkódod helyes.")
    else:
        print("A pinkód helytelen.")
while True:
    jelszo = int(input("Kérem adja meg a PIN kódját."))
    if pin == jelszo:
        print("A Pinkódod helyes.")
        break
    else:
        print("A pinkód helytelen.")

# 5 feladat
print("5 feladat")
szam = 0
a = 1
while a != 0:
    if szam == 0:
        a = 0
    a = int(input("Kérem adjon meg számokat és hogyha végzett adjon meg 0-t a programnak: "))
    szam += a
print(f"Beírta a 0-t a programnak vége. A számok összege: {szam}")
szam = 0
while True:
    if szam == 0:
        a = 0
    a = int(input("Kérem adjon meg számokat és hogyha végzett adjon meg 0-t a programnak: "))
    szam += a
    if a == 0:
        break
print(f"Beírta a 0-t a programnak vége. A számok összege: {szam}")

# 6 feladat
print("6 feladat")
teszpontszam = 0
osszes = 0
db = 0
while teszpontszam != -1:
    teszpontszam = int(input("Kérem adja meg a tesztpontszámokat hogyha befejezte írja be a -1-et: "))
    if teszpontszam != -1:
        osszes += teszpontszam
        db += 1   
print(f"A tesztek átlaga: {osszes / db}")
teszpontszam = 0
osszes = 0
db = 0
while True:
    teszpontszam = int(input("Kérem adja meg a tesztpontszámokat hogyha befejezte írja be a -1-et: "))
    if teszpontszam != -1:
        osszes += teszpontszam
        db += 1
    else:
        break
print(f"A tesztek átlaga: {osszes / db}")

# 7 feladat
print("7. feladat")
allapot = input("Mi a szerver állapota? (OK vagy ERROR) ")
while True:
    if allapot == "OK":
        break
    elif allapot == "ERROR":
        print("A szerver nem jó")
        allapot = input("Mi a szerver állapota? (OK vagy ERROR) ")
    else:
        allapot = input("Mi a szerver állapota? (OK vagy ERROR) ")

# 8 feladat
print("8. feladat")
kor = int(input("Hány éves vagy? "))
while kor > 120 or kor <= 0:
    kor = int(input("Hány éves vagy? "))
    if kor < 120 and kor > 0:
        break
    else:
        kor = int(input("Hány éves vagy? "))

# 9 feladat
print("9. feladat")
szam = int(input("Adj meg egy számot: (0 a vége) "))
while szam != 0:
    print(szam*1)
    print(szam*2)
    print(szam*3)
    print(szam*4)
    print(szam*5)
    print(szam*6)
    print(szam*7)
    print(szam*8)
    print(szam*9)
    print(szam*10)
    szam = int(input("Adj meg egy számot: (0 a vége) "))

# 10 feladat
print("10. feladat")
jelszo = input("Mi az új jelszó? ")
jelszo2 = input("Add meg megint a jelszót")
while True:
    if jelszo == jelszo2:
        print("Sikeres jelszóváltás")
        break
    else:
        jelszo = input("Mi az új jelszó? ")
        jelszo2 = input("Add meg megint a jelszót")

# 11 feladat
print("11. feladat")
szam = int(input("Adj meg egy páros számot: "))
while szam % 2 != 0:
    szam = int(input("Adj meg egy páros számot: "))
print("Hello Szia")

# 12 feladat
print("12 feladat")
valasztas = 0
while valasztas != 3:
    print("1. Üzenet küldés")
    print("2. Fájl Törlése")
    print("3. Kilépés")
    valasztas = int(input("Válassz egy opciót: "))
    if valasztas == 1:
        print("Üzenet elküldve")
        valasztas = int(input("Válassz egy opciót: "))
    if valasztas == 2:
        print("Fájl törölve")
        valasztas = int(input("Válassz egy opciót: "))
    if valasztas == 3:
        break

# 13 feladat
print("13 feladat")
dobas = random.randint(1,6)
eleg = "a"
while eleg != "stop":
    print(dobas)
    eleg = input("Elég? (stop-al leáll)")
    dobas = random.randint(1,6)




















