def angstrom_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        return True
    else:
        return False
n = int(input("Enter the number : "))
if angstrom_number(n):
    print(n,"is an Angstrom number")
else:
    print(n,"is not an Angstrom number")
