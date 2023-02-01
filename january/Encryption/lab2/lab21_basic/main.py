# task 2.1
list_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                 'ф', 'х', 'ц',
                 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', '-', ' ', ',', '.', '?', '!', 'я', '=', 'й', '-']

# task 2.2
# Б)Зашифруйте текст аффинным шифром 𝑦 ≡ 𝑎𝑥 + 𝑏 (𝑚𝑜𝑑 𝑚),
# где 𝑎 = (𝑛 + 2) и 𝑏 ≡ 𝑛 − 25 (𝑚𝑜𝑑 𝑚):
n_variant, m, a_revers = 12, 41, 0
a, b = n_variant + 2, (n_variant - 25) % m
print(' a =', a, ' b=', b, 'm =', m)
text_without_encryption, text_with_encryption, text_after_decryption = input().lower(), '', ''


# Процедура шифрования символов
def affine_encryption(x):
    y = (a * x + b) % m
    return y


try:
    for i in range(len(text_without_encryption)):
        index_char_after_encryption = affine_encryption(list_alphabet.index(text_without_encryption[i]))
        text_with_encryption += list_alphabet[index_char_after_encryption]

except:
    print('Error! you need use only russian char. Symbol error = ', text_without_encryption[i])
    exit(0)


print('Зашифрованный текст = ', text_with_encryption)


# ------------------------------------------------------------
# В) Пусть 𝑎 = (𝑛 + 2). Используя расширенный алгоритм Евклида, решите
# 𝑎𝑥 ≡ 1 𝑚𝑜𝑑 41

# ------------------------------------------------------------------
# Г) Зная 𝑎, 𝑏, 𝑚 расшифруйте текст, полученный в задании Б)
# g(y)= "A" в -1 степени * (y+m-b) mod m  формула для шифрования
# А в -1 степени можно получить по формуле "1 = (a* "A в минус 1 степени" % m)"


#Узнаем A в степени -1
while (a * a_revers) % m != 1:
    a_revers = a_revers + 1
    if a_revers == 99999:
        print('Не смог найти a в минус первой степени')
        exit(0)

print('"A" в -1 степени =', a_revers)


#функция расшифрование по формуле
def affine_decryption(encrypted_char):
    decrypted = a_revers * (encrypted_char + m - b) % m
    return decrypted


for i in range(len(text_with_encryption)):
    index_char = affine_decryption(list_alphabet.index(text_with_encryption[i]))
    text_after_decryption += list_alphabet[index_char]
print(text_after_decryption)


