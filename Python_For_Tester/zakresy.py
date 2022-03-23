imie="Janek"
#  J   a   n   e   k
#  0  1   2.  3   4

print("Długość napisu 'Janek' to:", len(imie) )

# Klasyczny zakres "od... do"

print("imie[3:5] ",  imie[3:5])



# Instrukcje równoważne (zakres od początku do pewnej pozycji):
print("imie[:4] ",  imie[:4])
print("imie[0:4]", imie[0:4])

# Instrukcje równoważne (zakres od pewnej pozycji do końca):

print("imie[3:]",  imie[3:])
print("imie[3:5]",  imie[3:5])

# Cały zakres (od początku do końca)

print("imie[:]  ",   imie[:])

# Indeksy ujemne oznaczają licznie od końca, przy czym ostatnia pozycja to... -1:
#  J   a   n   e   k
# -5  -4  -3  -2  -1
print("imie[-4,-2,]  ",   imie[-4:-2])

#W nawiasach możesz umieścić nawet liczby ujemne. Dzięki temu znaki będą liczone od końca, a nie od początku. To oznacza, że -3 to trzeci znak od końca.


# Tablice zawierające liczby można rozszerzać, dodając nowe elementy:
liczby=[3,6,8]
liczby.append(10)
print("Tablica 'liczby'", liczby)


