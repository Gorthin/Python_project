import easygui

# msgbox
"""
msg="Komunikat"
easygui.msgbox(msg) # Przycisk domyślny, okienko nie zawiera żadnego tytułu
tytul="Tytuł okna"       # Opcjonalny
ok_button="nadpisany OK" # Opcjonalny
easygui.msgbox(msg, tytul, ok_button)
"""

# ccbox

"""
msg = "Kontynuujemy?"
title = "Prośba o potwierdzenie"
pytania=["Tak", "Anuluj" ]
if easygui.ccbox(msg, title, pytania): # Pierwszy wybór = True
    pass    # Wybrano pierwszy przycisk (OK)
else:       # Wybrano drugi przycisk    (Continue)
    print("Do widzenia!")
    
#"""

# ynbox (tu działające w trybie ccbox)
"""
msg = "Kontynuujemy?"
title = "Prośba o potwierdzenie"
pytania=["Tak", "Nie" ]
if easygui.ynbox(msg, title, pytania): # Pierwszy wybór = True
    pass    # Wybrano pierwszy przycisk (OK)
else:       # Wybrano drugi przycisk    (Continue)
    print("Do widzenia!")
"""

"""
# buttonbox
title = "Jaką rasę psów lubisz?"
pytania=["Jamniki", "Shih-tzu", "Mieszańce"]
odp=easygui.buttonbox("Wybierz dobrze!", title, pytania, image="moje-logo.gif")
if odp in pytania:
    easygui.msgbox("Wybrano" + " " + odp)
else:
    easygui.msgbox("Czyżbyś lubił(a) koty?)")
"""

#  choicebox
"""
title = "Scenariusze"
pytanie = "Wybierz jeden ze scenariuszy do uruchomienia"
listawyboru=["Test-run1", "Test-run2", "Test-run3", "Test-run4", "Test-run5"]
odp = easygui.choicebox(pytanie, title, listawyboru, preselect=0)
easygui.msgbox("Wybrano:"+str(odp))
"""

#  multichoicebox
"""
title = "Scenariusze"
pytanie = "Wybierz jeden lub więcej scenariuszy do uruchomienia"
listawyboru=["Test-run1", "Test-run2", "Test-run3", "Test-run4", "Test-run5"]
odp = easygui.multchoicebox(pytanie, title, listawyboru, preselect=0)
easygui.msgbox("Wybrano:"+str(odp))
"""

"""
# enterbox
msg = "Podaj wartość"
title = "Liczba  przebiegów"
wynik = easygui.enterbox(msg, title)
print("Podano ", wynik)
"""

"""
# multenterbox
msg = "Podaj parametry testu"
title = "Warunki brzegowe"
pola = ["Min", "Max", "Krotność", "Odchyłka"]
wyniki=[]
wyniki = easygui.multenterbox(msg, title, pola)

while 1: # Wymuszamy wprowadzenie każdej z wartości
    if wyniki is None:  # Nic nie wybrano
        break
    errmsg = ""         # Tworzymy komunikat błędu
    for i in range(len(pola)):
        if wyniki[i].strip() == "":
          errmsg += ('"Pole %s" jest wymagane.\n' % pola[i])
    if errmsg == "":
        break           # OK
    wyniki = easygui.multenterbox(errmsg, title, pola, wyniki)
print("Wprowadzono: ", str(wyniki))
"""
"""
msg="Katalogi zawierające logi aplikacyjne"
title="Pobieranie nazwy katalogu"
default="."
res=easygui.diropenbox(msg, title, default)
print(res)

msg="Logi aplikacyjne"
title="Pobieranie nazwy pliku"
default="."
res=easygui.fileopenbox(msg, title, default)
easygui.filesavebox(msg, title, default)
print(res)
"""
"""
msg="Raporty"
title="Zapisywanie nowej wersji raportu"
default=""
res=easygui.filesavebox(msg, title, default)
print(res)
"""

easygui.codebox(msg="Nowa oferta", title="Ogłoszenie", text="Aaaaby sprzedać\nAaaaaale wcaaaaaleeee\nniedrogo")

