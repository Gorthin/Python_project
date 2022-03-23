import easygui
input("Naciśnij klawisz Enter i obserwuj uważnie komunikaty\
 wyświetlane w konsoli tekstowej:")
odp1=easygui.ynbox("Czy lubisz Pythona?", "Pytanie na śniadanie", ("Tak", "Nie") )
print("Odpowiedź:", odp1)
easygui.msgbox("Atak Daleków!", "Dr Who, pomocy!")
odp2=easygui.buttonbox("Wybierz ulubiony język programowania",
                       "Ankieta językowa", ("C++", "Python", "Java"))
print("Wybrano:",odp2)
