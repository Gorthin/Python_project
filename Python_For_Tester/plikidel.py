import pathlib
katalogBiezacy=pathlib.Path.cwd()  # Obiekt wskazujący na bieżący katalog
plikDel=katalogBiezacy / "testdir2/tekstowy.txt"
print("Sprawdzamy, czy plik istnieje:",plikDel.exists())
print(f"Zawartość katalogu {plikDel.parent}:")
for element in plikDel.parent.iterdir():
    print(element.name, end=" ")
print()
plikDel.unlink(missing_ok=True)
print(f"Zawartość katalogu {plikDel.parent}:")
for element in plikDel.parent.iterdir():
    print(element.name, end=" ")
print()
print("Sprawdzamy, czy plik istnieje:",plikDel.exists())