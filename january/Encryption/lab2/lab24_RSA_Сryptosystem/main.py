import math

list_alphabet = ['м', 'о', 'х', 'о', 'р', 'е', 'в', 'э', 'д', 'у', 'а', 'р', 'д', 'о', 'л', 'у', 'г', 'о', 'в', 'и',
                 'ч', ' ']
text_fio = 'Мохорев Эдуард Олегович'.lower()
text_after_encryption = ''
list_fio = []
list_after_encryption = []
list_after_decryption = []

random_block = []
p, q = 3089, 3011
n = p * q
euler_function = (p - 1) * (q - 1)
print(' p =', p, ' q =', q, ' n =', n, end=" ,")
print('функция эйлера =', euler_function, end=' ,')

##  выберем открытую экпоненту, любое простое число
e = 3
print(' e =', e, end=' ,')
#  ( d * e ) mod euler(n) = 1
#  секретная вычисляется с помощью расширенного алгоритма евклида
# d = 0
d = 6196587
while ((d * e) % euler_function) != 1:
    d = d + 1
print(' d=', d)


# публичный ключ (secret ** e,mod n)
# приватный ключ (secret ** d,mod n)

def encyption_rsa(for_hide):
    #test = (pow(for_hide, e)) % n
    hide = for_hide
    for i in range(e-1):
        hide = (hide * for_hide) % n
    return hide


def decryption_rsa(for_show):
    #test = (pow(for_show, d)) % n
    show = for_show
    for i in range(d-1):
        show = (show * for_show) % n
    return show

print('Текст до шифрования = ',text_fio)
for i in range(len(text_fio)):
    list_fio.append(list_alphabet.index(text_fio[i]))
print('Перевели текст в число до шифрования = ', list_fio)


for i in range(len(list_fio)):
    list_after_encryption.append(encyption_rsa(list_fio[i]))
print('Число после шифарования = ', list_after_encryption)


for i in range(len(list_after_encryption)):
    list_after_decryption.append(decryption_rsa(list_after_encryption[i]))
print('число после дешифрования = ', list_after_decryption)


print('Текст после дешифрования = ', end='')
for i in range(len(list_after_decryption)):
    print(list_alphabet[list_after_decryption[i]], end='')

