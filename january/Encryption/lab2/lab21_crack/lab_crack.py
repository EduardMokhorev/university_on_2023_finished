list_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                 'ф', 'х', 'ц',
                 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', '-', ' ', ',', '.', '?', '!', 'я', '=', 'й', '-']
m = 41

text_with_encryption = 'фьа.щёябь.рдф.щ,у угр.щв-сьаерёжйщпрёф.ьтки-джйщпрб ьф.рёжщфэрерё-ёупь.кщерфдуткдущьбсьзрпщбутррщ реррщуф яфтрееуэущ.рдф.ьщёябящеьщёжффду щнсядрйщьщеьц-еь=ир жщуёь.уёжщу..уц-.кщеьпядщ,жбт-цея?щпяф.ж,тре-ащпщву ь!е-?щжфтуп-н?мщ'
text_after_decryption = ''


def affine_decryption(encrypted_char):
    decrypted = a_revers * (encrypted_char + m - b) % m
    return decrypted


for a_revers in range(1, 4):
    for b in range(1, 35):
        for i in range(len(text_with_encryption)):
            index_char = affine_decryption(list_alphabet.index(text_with_encryption[i]))
            text_after_decryption += list_alphabet[index_char]
        print(text_after_decryption, 'a_revers =', a_revers, ' b= ', b, end='\n \n')
        text_after_decryption = ' '
