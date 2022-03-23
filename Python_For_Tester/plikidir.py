import pathlib

katalogBiezacy=pathlib.Path.cwd()  # Obiekt wskazujący na jakiś katalog, tutaj: bieżący
print(" *** Przeglądamy bieżący katalog ***")
print("*Wypisz zawartość (format długi):")

for element in katalogBiezacy.iterdir():
    print(element)

print("*Wypisz zawartość (format krótki):")
for element in katalogBiezacy.iterdir():
    print(element.name)

print("*Wypisz wyłącznie pliki zgodne ze wzorcem *.py:")
for element in katalogBiezacy.glob("*.py"):
    print(f"Znalazłem {element.name} ", end="")
print()

print(" *** Przeglądamy bieżący katalog oraz podkatalogi ***")

print("*Wypisz wyłącznie pliki zgodne ze wzorcem test*.py:")
for element in katalogBiezacy.rglob("test*.py"):
    print(f"Znalazłem {element.name} ", end="")
print()
