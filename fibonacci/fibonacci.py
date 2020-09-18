num = int(input("Enter the number of terms : "))

x = 1
y = 0
z = 0
print("\nFIbonacci numbers :")
while(num>0):
    print(z, end="  ")
    z = x + y
    x = y
    y = z
    num -= 1
