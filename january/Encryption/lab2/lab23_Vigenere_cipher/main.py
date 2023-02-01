# Шифр Виженера
list_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                 'ф', 'х', 'ц',
                 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', '-', ' ', ',', '.', '?', '!', 'я', '=', 'й', '-']
m = 41
key_for_encryption = "Мохорев Эдуард Олегович".lower()
text_for_encryption = "Шифрование это обратимое преобразование информации в целях сокрытия".lower()
array_after_encryption = []

print('Зашифрованный текст')
for i in range(len(text_for_encryption)):
    id_key = list_alphabet.index(key_for_encryption[i % 22])
    id_text = list_alphabet.index(text_for_encryption[i])
    array_after_encryption.append((id_key + id_text) % 41)
    print(list_alphabet[(id_key + id_text) % 41], end='')

text_for_decryption = '!чаююжвд=икэ.тчьмхг лхъумэ кр,ддыотддчрямыцчьъх!що..фъшлмщч-щпуафтз'.lower()
array_after_decryption = []


print(end="\n \n \n")
print('Расшифровка')
for i in range(len(text_for_decryption)):
    id_key = list_alphabet.index(key_for_encryption[i % 22])
    id_text = list_alphabet.index(text_for_decryption[i])
    array_after_decryption.append((id_key - id_text) % 41)
    print(list_alphabet[(id_text - id_key) % 41], end='')
