import openpyxl
skoroszyt  = openpyxl.load_workbook("Inne/raport.xlsx") # Otwórz skoroszyt z dysku
arkusz = skoroszyt["Arkusz1"]                           # Otwórz 'Arkusz1'
komorka = arkusz.cell(row=12, column=4)         # D12
komorka.value = "=SUM(D3:D11)"                  # Formuły muszą używać nazw w języku angielskim
komorka.font = komorka.font.copy(bold=True)     # Styl pogrubiony
arkusz["C11"]= 200.5                            # Dopisujemy wartość
arkusz["B15"]= "Autor:"                         # Dopisujemy zwykły napis
skoroszyt.save("Inne/raport2.xlsx")             # Wynik możesz też zapisac pod taką samą nazwą, nadpisujac stary plik!




