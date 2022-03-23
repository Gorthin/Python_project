import argparse  # 'description' zawiera opis skryptu
parser = argparse.ArgumentParser(description='Odczyt parametrów w wersji PRO')

# Lista argumentów obowiązkowych, 'help' zawiera wyjaśnienie przeznaczenia danego parametru
parser.add_argument('timing1', help="Opóźnienie wywoływania modułu I/O")
parser.add_argument('timing2', help="Maksymalne opóźnienie odczytu rekordów \
z bazy danych")
parser.add_argument('limit',   help="Limit ilości wykonania pętli odczytu",\
                    type=int)
# Lista argumentów opcjonalnych
parser.add_argument('-n', '--przebiegi', help="Opcjonalny argument typu int \
z wartością domyślną 5",type=int, default=5, required=False)
# Wywoływanie, wersja krótka, np.: -n 77
# Wywoływanie, wersja rozszerzona, np.: --przebiegi 77

args = parser.parse_args() # Odczyt
print("timing1 (opóźnienie wywoływania modułu I/O):", args.timing1)
print("timing2 (maksymalne opóźnienie odczytu rekordów z bazy danych):",\
      args.timing2)
print("limit   (limit ilości wykonania pętli odczytu):",\
      args.limit)
print("przebiegi (opcjonalny argument typu int z wartością domyślną 5):",\
      args.przebiegi)