# Moduł calendar - kilka przykładowych metod
import calendar
cal = calendar.month(2021, 5)
print ("Kalendarz na Maj 2021:")
print (cal)
print ("Kalendarz na Maj 2021 - po częściowej polonizacji:")
print(cal.replace("Mo","Po")) # Częściowa polonizacja wyniki

print ("Kalendarz na rok 2021:")
print ( calendar.calendar(2021) )

print("Rok 2024 jest przestępny:", calendar.isleap(2024))
print("Rok 2021 jest przestępny:", calendar.isleap(2021))