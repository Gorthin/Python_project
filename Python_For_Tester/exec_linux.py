import subprocess

# Stara metoda (obecnie  niepolecana)
#import os
#os.system("./bash.sh")
#print("Zewnętrzny program został uruchomiony, wracam do skryptu Pythona")

# zalecana metoda:
subprocess.call(['sh', 'bash.sh'])
print("Zewnętrzny program został uruchomiony, wracam do skryptu Pythona")
