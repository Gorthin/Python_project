dozwolone = [1, 2, 3]
v= None

if v==None:
    try:
        v=int ( input("Podaj wartość: ") )
        print("Odebrano: ", v)
    except EOFError:
        print("... wykryto Ctrl+D, ustawiam 'v'=3")
        v=3

if v in dozwolone:
    print("OK!")
else:
    print("Poza zakresem wartości dozwolonych")

