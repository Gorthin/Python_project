import pandas as pd
pomiary = pd.read_csv("misiePanda/dane1.csv")
pomiary.dropna(inplace=True) # Kasujemy wierszy zawierających puste komórki (NaN)
print(pomiary)
pomiary.to_excel("Inne/pandas2excel.xlsx")





