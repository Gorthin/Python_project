from matplotlib import pyplot as plt
testy=['Wydajnościowe', 'Funkcjonalne', 'Niefunkcjonalne', 'Pozostałe']
passRate =[5, 15, 20, 5]
statystyki=plt.bar(testy, passRate,  color='k', label='Status=OK')
plt.legend(handles=[statystyki])
plt.title("Testy regresji - faza 2.")
plt.xlabel("Kategorie")
plt.ylabel("Wyniki")
plt.yticks([0, 5,10,15,20])
plt.show()
