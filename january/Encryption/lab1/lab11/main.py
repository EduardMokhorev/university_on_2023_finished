import math
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#               lab1.1
variant = 27
N = int(math.sqrt(30202020 + (20190 * variant)) + (24 * variant))
K = int(math.sqrt(20192019 - (20200 * variant)) - (38 * variant))

print('N = ', N, ' K =', K)


# 1. нод по алгоритму евклида
def gcd_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


NOD, X, Y = gcd_extended(N, K)
print('Задание 1 Нод =', NOD, ', X =', X, ' Y =', Y)



# 2 задание
print("N = ", N)
result_task2 = (2 ** N) % ((2 * variant) + 143)
print(2 * N + 143)
print('Задание 2, результат равен = ', result_task2)




# 3
def gety(nod, n, k):
    for x in range(1, 100000):
        y = (nod - x * n) / k
        if (y % 1 == 0):
            return y


def getx(y, n, k):
    return (1 - y * k) / n

a = getx(gety(1, 2027, N), 2027, N)



print(a)

nod_k = gcd_extended(K, 2027)[0]
nod_n = gcd_extended(N, 2027)[0]
assert nod_n == nod_k == 1
print("это взаимно простые числа")
print(f"NOD {K} and {2027} = {nod_k} , Nod {N} and {2027} = {nod_n}")
print(f"{2027}a + {N} = НОД({2027},{N}) = 1")



print(f"а = {a}")

print("Т.к. 𝑎𝑥 = 1, то:")
print(f"2027𝑥 = {K} 𝑚𝑜𝑑 {N}")
result = (a * K) % N
print(int(result), f"mod {N}")
