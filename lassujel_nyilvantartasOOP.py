import os
import datetime

class Lassujelek:
    def __init__(self, sorszam:int, vonal:int, hossz:float, vmax:int, ok:str, pos:int):
        self.sorszam = sorszam
        self.vonal = vonal
        self.hossz = hossz
        self.vmax = vmax
        self.pos = pos
        self.ok = ok

    def mindenki(self):
        return (f"A {self.sorszam} számú lassújel a {self.vonal} számú vonalon "
                f"{self.hossz} km hosszú, jelenleg maximum {self.vmax} km/h-val járható, "
                f"a 0 km-től számított pozíciója {self.pos} km. A lassújel oka: {self.ok}.")

    def szamoski(self):
        return f"A lassújel sorszáma: {self.sorszam}."

    def __str__(self):
        return (f"A {self.sorszam} jelzésű lassújel a {self.vonal}. vonalon van, "
                f"hossza {self.hossz} km, maximális sebesség {self.vmax} km/h, "
                f"helyzete {self.pos} km, oka: {self.ok}.")

    def to_file(self, filepath: str):
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(f"{datetime.datetime.now()}: {self.mindenki()}\n")

    def update_reason(self, new_reason: str, filepath: str | None = None):
        old = self.ok
        self.ok = new_reason
        if filepath:
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(f"{datetime.datetime.now()}: A {self.sorszam} lassújel oka megváltozott: '{old}' -> '{new_reason}'\n")

    def move_position(self, new_pos: int, filepath: str | None = None):
        old = self.pos
        self.pos = new_pos
        if filepath:
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(f"{datetime.datetime.now()}: A {self.sorszam} lassújel pozíciója {old} -> {new_pos}\n")

    def change_vmax(self, new_vmax: int, filepath: str | None = None):
        old = self.vmax
        self.vmax = new_vmax
        if filepath:
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(f"{datetime.datetime.now()}: A {self.sorszam} lassújel vmax értéke {old} -> {new_vmax}\n")


lista = []
OUTFILE = os.path.join(os.path.dirname(__file__), 'lassujel_kimenet.txt')


def peldanyositas():
    lista.append(Lassujelek(4589, 100, 1.64, 60, "A 485-ös számú talpfa sérülése", 138))
    lista.append(Lassujelek(7821, 150, 0.8, 80, "Felsővezeték hibája", 258))
    lista.append(Lassujelek(6387, 80, 2.45, 100, "A töltés szerkezetének meggyengülése", 58))
    lista.append(Lassujelek(6413, 1, 0.1, 15, "A vasúti átjáró meghibásodása", 26))
    lista.append(Lassujelek(5465, 100, 0.4, 20, "A 956-os számú váltó meghibásodása", 186))
    lista.append(Lassujelek(6523, 30, 3.82, 80, "Lakott terület", 149))


def kibasszuk():
    header = f"=== Lassújelek listája ({datetime.datetime.now()}) ===\n"
    print(header.strip())
    with open(OUTFILE, 'a', encoding='utf-8') as f:
        f.write(header)
        for item in lista:
            line = item.mindenki()
            print(line)
            f.write(line + '\n')


def szamalapuf(milyenszamotkeressekxdd: int):
    for item in lista:
        if item.sorszam == milyenszamotkeressekxdd:
            prompt = (f"{item.szamoski()} megtalálva! "
                      "Ha szeretnéd, hogy írjak ki róla minden információt, írj be egy 1-est, ha nem, egy 0-t: ")
            try:
                more = int(input(prompt))
            except ValueError:
                print("Hibás bemenet, kilépés.")
                return "Hibás bemenet, kilépés."
            if more == 1:
                info = item.mindenki()
                with open(OUTFILE, 'a', encoding='utf-8') as f:
                    f.write(f"{datetime.datetime.now()}: Részletes info a {item.sorszam} lassújelről: {info}\n")
                return info
            else:
                with open(OUTFILE, 'a', encoding='utf-8') as f:
                    f.write(f"{datetime.datetime.now()}: A felhasználó nem kérte a részletes információt a {item.sorszam} lassújelről.\n")
                return "Rendben, kilépés..."
    return "Nincs ilyen sorszámú lassújel."


def io():
    try:
        milyenszamotkeressekxdd = int(input("Add meg melyik sorszámú lassújelre keressek rá: "))
    except ValueError:
        print("Hibás szám, kilépés.")
        return
    res = szamalapuf(milyenszamotkeressekxdd)
    print(res)


def main():
    try:
        if os.path.exists(OUTFILE):
            os.remove(OUTFILE)
    except Exception:
        pass

    peldanyositas()
    kibasszuk()
    print("\n-- Metódusteszt: frissítések és fájlba írás --")
    target = lista[0]
    print(target)
    target.update_reason("Általános karbantartás miatt", OUTFILE)
    target.move_position(140, OUTFILE)
    target.change_vmax(50, OUTFILE)
    target.to_file(OUTFILE)
    print(f"A {target.sorszam} lassújel adatainak frissítése megtörtént és mentve.")
    lista[1].to_file(OUTFILE)
    lista[2].update_reason("Vízfolyás miatti megereszkedés", OUTFILE)
    lista[3].move_position(30, OUTFILE)
    print("\nInteraktív keresés következik (próbáld ki egy sorszámmal).")
    io()


if __name__ == '__main__':
    main()
