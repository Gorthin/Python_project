# Program powinien zostać uruchomiony pod Linux lub macOS!
import pathlib

p1=pathlib.Path("mytoolkit")
domowy=pathlib.Path.home()

print(f"Czy '{p1.name}' to katalog: ", p1.is_dir())
print(f"Czy '{domowy}'  to plik: ", domowy.is_file())
print(f"Dekompozycja {domowy} na składowe (tupla): {domowy.parts}")

skryptBash=pathlib.Path("bash.sh")
wzorzec1="b*"
wzorzec2="bas?.s[abcdefghijkl]"
print(f"Czy '{skryptBash.name}' jest zgodny ze wzorcem '{wzorzec1}': {skryptBash.match(wzorzec1)}")
print(f"Czy '{skryptBash.name}' jest zgodny ze wzorcem '{wzorzec2}': {skryptBash.match(wzorzec2)}")
print(f"""Informacje o pliku {skryptBash}:
  {skryptBash.stat()}
  Rozmiar: {skryptBash.stat().st_size}
  Tryb (bin): {skryptBash.stat().st_mode.__format__("b")}
  Tryb (oct): {skryptBash.stat().st_mode.__format__("o")} 
""")

