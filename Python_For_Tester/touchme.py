import pathlib
katalogBiezacy=pathlib.Path.cwd()        # Obiekt wskazujący na bieżący katalog

# Od tego folderu rozpoczniemy operację "Nieszkodliwy dotyk":
folderStartowy=katalogBiezacy / "test-touch"

if not folderStartowy.exists():
    print(f"Katalog startowy '{folderStartowy}' nie istnieje!")
    exit()

nazwaZnacznika="NasiTuByli.txt"
plikZnacznik=folderStartowy / nazwaZnacznika    # Nazwa pliku-znacznika dla folderu startowego
print("Odwiedzam :", folderStartowy.name)

plikZnacznik.touch(exist_ok=True)               # Tworzę pierwszy plik w katalogu startowym
                                                # exist_ok=True pozwala uniknąć wyjątku 'FileExistsError'

for element in folderStartowy.rglob("*"):       # Przeglądamy zawartość katalogu startowego i jego "potomków"
    if element.is_dir():
        print("Odwiedzam :", element.name, end= "-->")
        (element / nazwaZnacznika).touch(exist_ok=True)  # Tworzę pliki znczników w podkatalogach
        print("Maks i Albert tu byli!")
print()
