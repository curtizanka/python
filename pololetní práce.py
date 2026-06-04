print("Konfigurátor zdícího systému.")
print("*"*29)

uzi_jmeno = "stavebnik"
heslo = "stavba"
email = "stavebnik@email.cz"

zad_jmeno = input("\nZadejte uživatelské jméno nebo email: ")
zad_heslo = input("Zadejte heslo: ")
if zad_jmeno == uzi_jmeno or email and zad_heslo == heslo:
    print("Přihlášení bylo úspěšné.")
    
else:
    print("Zadali jste chybné jméno nebo heslo.")

delka = float(input("\nZadejte délku stěny (v metrech): "))
vyska = float(input("Zadejte výšku stěny (v metrech): "))
vyska_okna = float(input("Zadejte výšku okna (v metrech): "))
sirka_okna = float(input("Zadejte šířku okna (v metrech): "))
 
plocha_steny = delka * vyska
plocha_okna = vyska_okna * sirka_okna
plocha_bez_okna = plocha_steny - plocha_okna
 
tvarnice = plocha_bez_okna * 10

print(f"\nPlocha stěny včetně okna: {plocha_steny:.2f} m^2")
print(f"Plocha okna: {plocha_okna:.2f} m^2")
print(f"Plocha bez okna: {plocha_bez_okna:.2f} m^2")
print(f"Počet tvárnic potřebných k vyzdění plochy stěny: {tvarnice:.0f} ks")

print("\nDostupnost materiálu na pobočkách v ČR")
print("*"*38)
print("| Město      | Druh materiálu  | Počet kusů na pobočce  |")
print("*"*57)
print("| Praha      | tvárnice        | 500                    |")
print("| Brno       | tvárnice        | 300                    |")
print("| Ostrava    | tvárnice        | 700                    |")
