# # лабораторная 3 коды рида саламона
# # n=27
# # 17-простое число, следовательно
# # фи(17)
# ## задание 1
# print("\n*************************************************  Задание 1")
# n = 27
# # n = input("введите вариант > ")
# # n = 12 #-my variant
# print("n = мой вариант = ", n)
# print("17- простое число ->  ф(17) = 16")
# a = (3 ** ((2 * n) + 1)) % 17
# print(f"a = (3**((2*{n})+1)) % 17")
# print("a = ", a)
#
# list_extend = []
# for i in range(1, 17):
#     temp_result_a_in_the_extend_i = a ** i % 17
#     list_extend.append(temp_result_a_in_the_extend_i)
#     print(f"{a}**{i} = ", temp_result_a_in_the_extend_i, "mod 17")
#
# print(list_extend)
# print("Таким образом, при любом b из 𝐺𝐹(17) сравнение имеет решение")
#
# print("\n*************************************************  Задание 2")
# print("Найдите коэффициенты многочлена в поле 𝐺𝐹(17)")
# print("g(x) = (𝑥 − a**1)(𝑥 − a**2)(𝑥 − a**3)(𝑥 − a**4)")
# print(f"g(x) = (𝑥 − {list_extend[0]})(𝑥 − {list_extend[1]})(𝑥 − {list_extend[2]})(𝑥 − {list_extend[3]})")
#
# ##################
# ################ хуй знает как тут это делается
# #################

print("\n*************************************************  Задание 3")
tuple_alphabet = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
                  "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "Ъ", "ы", "ь", "э", "ю", "я")

fio = "СОРОКИНАРМАНЭДУАРДОВИЧ".lower()
# fio = input("введите фио без пробелов > ").lower()
if len(fio) % 17 != 1:
    first = 0
    for i in range(len(fio), 36, 1):
        fio += fio[first]
        first += 1
[print(_ + " ", end=" ") for _ in fio]
print()

list_index_alphobet = []
list_index_mode_17 = []
[list_index_alphobet.append(tuple_alphabet.index(_)) for _ in fio]
[list_index_mode_17.append(i % 17) for i in list_index_alphobet]

[print(_, end=" ") if _ > 10 else print(str(_) + " ", end=" ") for _ in list_index_alphobet]
print(end="\n")
[print(_, end=" ") if _ > 10 else print(str(_) + " ", end =" ") for _ in list_index_mode_17]
print(end="\n")

print("i0(x) = ", end="")
for i in range(0, 12):
    print(list_index_mode_17[i], end=" ")
print()
print("i1(x) = ", end="")
for i in range(12, 24):
    print(list_index_mode_17[i], end=" ")
print()
print("i2(x) = ", end="")
for i in range(24, len(list_index_mode_17)):
    print(list_index_mode_17[i], end=" ")

