komunikat=" Strefa wolna od zbędnej teorii"       # Zmienna tekstowa
jezyki   = ["C++", "Python", "Java", "Lisp"]       # Prosta lista (lub klasycznie: tablica)
print("Komunikat:", komunikat)
print("Długość powyższego napisu”", len(komunikat))
print("*--------------------------------------------*")
print("*\t\tNapis po podwójnym '\t' (tabulator)*")
print(f"'The Zen of Python' można przetłumaczyć jako:\n\n{jezyki[1]} jest łatwy do nauki")          # (*)
print( "'The Zen of Python' można przetłumaczyć jako:\n\n" + jezyki[1] + " jest łatwy do nauki")    # (**)

# Rozbijamy dłuższy zapis na kilka linii:

print("Alicja w krainie czarów" \
+ " - " \
+"Alicja po drugiej stronie lustra")

# Powyższy zapis jest równoważny temu:
print("Alicja w krainie czarów" + " - " +"Alicja po drugiej stronie lustra")
