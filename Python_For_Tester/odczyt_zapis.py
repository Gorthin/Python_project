# Zapis do pliku testowego

nowyplik="output.txt" # Plik wyjściowy, otwarty do zapisu i następnie używany do odczytu i zapisu

# Otwieram plik do zapisu. Ewentualny stary plik o tej samej nazwie zostanie nadpisany!
# Plik wyjściowy będzie zawierał 3 wiersze: Nowy wiersz 1","Nowy wiersz 2","Nowy wiersz 3"
print(f"Zapis do pliku tekstowego: {nowyplik}")
plik_out = open(nowyplik, "w")      # Tryb 'w' - ang. write
print("Zapisuję do ", nowyplik, "zawartość: 'Nowy wiersz 1', 'Nowy wiersz 2', 'Nowy wiersz 3'")

plik_out.write("Nowy wiersz 1\n")
plik_out.write("Nowy wiersz 2\n")
plik_out.write("Nowy wiersz 3\n")

"""  Alternatywna metoda:
lst=["Nowy wiersz 1\n", "Nowy wiersz 2\n", "Nowy wiersz 3\n"]
plik_out.writelines(lst)
"""

plik_out.close()
input(f"Plik {nowyplik} został utworzony lub nadpisany na dysku - sprawdź jego zawartość, a następnie naciśnij Enter, aby kontynuować")
print(f"Otwieram plik: {nowyplik} do odczytu i zapisu")
plik_in_out = open(nowyplik, "r+")    # Tryb 'r+' - ang. read, oraz zapis (+)
print("Czytam wiersz 1.:", plik_in_out.readline(), end="")
print("Czytam wiersz 2.:", plik_in_out.readline(), end="")
print("Zapisuję do ", nowyplik,"nowy napis: 'THE DOORS:")
plik_in_out.write("THE DOORS:")
print("Dopisuję do ", nowyplik,"nowy napis: 'This is the end, my only fiend...' oraz znak nowej linii")
plik_in_out.write("This is the end, my only fiend...\n")
print("Czytam dalej:", plik_in_out.readline(), end="") # W tym miejscu nic nie ma, jesteśmy przecież na samym końcu pliku po dokonanym zapisie!
plik_in_out.close()

print("\nOtwieramy ponownie plik i sprawdzamy zawartość")
plik_in = open(nowyplik, "r")
print(plik_in.read()) # Czytamy zawartość całego pliku naraz
plik_in.close()
