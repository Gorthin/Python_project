# Stara metoda (obecnie  niepolecana)
import os
#os.system('"C:/Windows/System32/notepad.exe"')
os.system('"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"')
print("Zakończono zewnętrzny proces - program MS Edge")

# Zalecana metoda
import subprocess
# Wywołanie blokujące:
subprocess.call('"C:/Windows/System32/notepad.exe"')
print("Zakończono zewnętrzny proces - program Notepad.exe")
# Wywołanie nieblokujące:
subprocess.Popen('"C:/Windows/System32/calc.exe"')
#subprocess.Popen(['C:\Windows\System32\calc.exe'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
print("W tle działa uruchomiony, zewnętrzny proces - program calc.exe")
input("Naciśnij klawisz ENTER")
print("Do widzenia")

