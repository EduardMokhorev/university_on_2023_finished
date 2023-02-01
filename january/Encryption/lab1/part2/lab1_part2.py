import math
variant = 12
variant = 27


def gcd_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


first_number = (9 * variant) % 256
second_number = 7*(41-variant)

print(first_number, " = первое число в 10с/с", bin(first_number), 'оно же в двоичной')
print(second_number, " = первое число в 10с/с", bin(second_number), 'оно же в двоичной')

print(len(bin(first_number)))
