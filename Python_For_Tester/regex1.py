import re
kodyRegex = re.compile(r'(\d\d)-(\d\d\d)')
wynik = kodyRegex.findall('Kody 55-113 55-22 53-99 \n 55-555')
print( wynik )

txt = "Kot Kociak"
x = re.findall("Koc*", txt)
print(x)