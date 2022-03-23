import pathlib
katalogBiezacy=pathlib.Path.cwd()        # Obiekt wskazujący na bieżący katalog

# Zmiana nazwy
folderSRC=katalogBiezacy / "test-touch"             # Stara nazwa
folderDEST=katalogBiezacy / "test-touch-odmieniony" # Nowa nazwa

try:
    print(f"Zmieniam nazwę {folderSRC.name} na {folderDEST.name}")
    folderSRC=folderSRC.rename(folderDEST) # Podmieniam zawartość referencji pierwotnej
    print(f"Nowa nazwa {folderSRC.name}")
except FileNotFoundError:
    print("Hm, nie znalazłem pliku!")