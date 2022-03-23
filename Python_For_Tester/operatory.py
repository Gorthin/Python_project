print("2 do potęgi 3 (czyli 2**3)=\t", 2**3)
print("16 modulo 3 (czyli 16%3)=\t", 16%3)
print("Część całkowita wyrażenia 16/3 (czyli 16//3)=", 16//3)
x = 10
y = 6
print(f"x={x}, y={y}")
print("Wartość porównania 'x > y' to: ", x>y)

z = x + y
print ("z = x + y=", z)
z += x
print("z += x to jest to samo, co z=z+x=\t", z)
z *= x
print("z *= x to jest to samo, co z=z*x=\t", z)
z /= x
print("z /= x to jest to samo, co z=z/x=\t", z)

print("bin(5)=", bin(5))
print("Liczba 5 << 1 to 10 (operacje są wykonywane na bitach!):", 5<<1, "- binarnie: ", bin(5<<1) )