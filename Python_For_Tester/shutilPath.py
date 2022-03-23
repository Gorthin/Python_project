import pathlib
import shutil
katalogBiezacy=pathlib.Path.cwd()        # Bieżący katalog

# Skopiowanie  plików z folderu X do Y
folderSRC=katalogBiezacy / "test-x"     # Folder źródłowy
folderDEST=katalogBiezacy / "test-x2"   # Folder docelowy
for element in folderSRC.glob('*.*'):
    shutil.copy(element, folderDEST)   # Kopiowanie
    #shutil.move(element, folderDEST)  # Przenoszenie
