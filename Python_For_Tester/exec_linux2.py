import subprocess
prog = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
(wynik, err) = prog.communicate()
print("Typ danych zmiennej 'wynik' to", type(wynik))
print(f"Dziś jest:\n{wynik}")
prog = subprocess.Popen("who", stdout=subprocess.PIPE, shell=True)
(wynik, err) = prog.communicate()

print(f"Zalogowani użytkownicy:\n {wynik} ")
