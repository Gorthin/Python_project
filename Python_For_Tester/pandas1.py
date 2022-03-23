import pandas as pd # Alias nazwy pandas

dni =    { "DNI": ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"] }
odczyty= {"ODCZYTY": [50, 60, 80, 50, 60, 90, 100] }

dane={} # Pusty słownik
dane.update(dni)        # Dokładamy pierwszą kolumnę
dane.update(odczyty)    # Druga kolumna

seria2D = pd.DataFrame(dane)
print("seria2D=")
print(seria2D)
print("seria2D[\"ODCZYTY\"]=\n",seria2D["ODCZYTY"])
print("Ta i każda inna kolumna danych w DataFrame jest obiektem 'Series':", type(seria2D["ODCZYTY"]))

mojindeksik= ['Runda1','Runda2', 'Runda3', 'Runda4', 'Runda5', 'Runda6', 'Runda7']
seria2D.index=mojindeksik
seria2D.index.name="Rundy:"
seria2D.rename(columns={"DNI": "Dni", "ODCZYTY": "Odczyty"}, inplace=True)
print(seria2D)
