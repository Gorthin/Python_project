from matplotlib import pyplot as plt
osX=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
osY =[5, 5.6, 8, 9,  11, 20, 14, 12, 10, 9.5]
osY2=[2, 3,   6, 9,  12, 13, 16, 14, 12, 12 ]
seria1,=plt.plot(osX, osY,  marker='*', linestyle='--', color='k',
                 ms=10, linewidth = '1', label='Seria 1.') # Seria 1.
seria2,=plt.plot(osX, osY2, marker='o', linestyle='-',  color='k',
                 ms=10, linewidth = '1', label='Seria 2.') # Seria 1.
plt.legend(handles=[seria1, seria2])
plt.title("Pomiary napięcia")
plt.xlabel("[t]")
plt.ylabel("[V]")
plt.xticks([0, 25,50,75, 100])

plt.show()