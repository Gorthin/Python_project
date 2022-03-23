import pathlib

katalogDomowy=pathlib.Path.home()
katalogBiezacy=pathlib.Path.cwd()

pewienplik=katalogBiezacy / pathlib.Path("witamy.py")
# pewienplik=katalogBiezacy / "witamy.py" # Identyczny efekt jw. (alternatywana postać)

print(f"Katalog domowy:{katalogDomowy} \nBieżący katalog:{katalogBiezacy}")
print(f"Nasz pierwszy program w Pythonie: {pewienplik}")

print(f"Dekompozycja składowych - nazwa :{pewienplik.name}")
print(f"Dekompozycja składowych - trzon : {pewienplik.stem}")
print(f"Dekompozycja składowych - suffiks' : {pewienplik.suffix}")
print(f"Dekompozycja składowych - 'parent' : {pewienplik.parent}")
print(f"Dekompozycja składowych - 'anchor' : {pewienplik.anchor}")

katalogBiezacy=pathlib.Path.cwd()
katalogDel=katalogBiezacy / pathlib.Path("testdir2")
try:
    print(f"Chcemy usunąć {katalogDel}")
    katalogDel.rmdir()# Usuwamy katalog wskazywany przez obiekt klasy Path  (**)
except OSError:
    print("Coś poszło nie tak. Sprawdź, czy katalog istnieje lub czy nie zawiera plików")

if katalogDel.exists():
    print(f"Katalog {katalogDel} istnieje")
else:
    print(f"Katalog {katalogDel} nie istnieje")

if pewienplik.exists():
    print(f"Plik {pewienplik} istnieje")
else:
    print(f"Katalog {pewienplik} nie istnieje")

katalogNowy=pathlib.Path("testdir3")
try:
    print(f"W katalogu bieżącym tworzymy folder {katalogNowy}")
    katalogNowy.mkdir() # Ta operacja powiedzie się tylko raz...
except OSError:
    print("Coś poszło nie tak. Sprawdź, czy katalog już istnieje")



