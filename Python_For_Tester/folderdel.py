import pathlib
katalogBiezacy=pathlib.Path.cwd()        # Obiekt wskazujący na bieżący katalog
folderDel=katalogBiezacy / "testdir3"    # Usuwamy podkatalog 'testdir3'
print(f"Sprawdzamy, czy katalog {folderDel} istnieje:",folderDel.exists())

print(f"Kasujemy katalog {folderDel}:")
for element in folderDel.iterdir():
    print("Usuwam:", element.name)       # Kasuję zawartość folderu
    element.unlink()
print(f"Teraz usuwam {folderDel}")       # Dopiero teraz usuwam sam folder
folderDel.rmdir()

print(f"Sprawdzamy, czy katalog {folderDel} istnieje:",folderDel.exists())
