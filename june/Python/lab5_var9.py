"""
POZ_41
Mokhorev E.O
lab 5
Написать программу на языке Python, создающую из русско-английского словаря англо-русский словарь
(обязательно использовать словари(dict)). Входные данные берутся из файла input.txt,
выходные данные записываются в файл output.txt. Входные данные лексикографически отсортированы, и
выходные данные тоже должны быть отсортированы! В выходной файл первым записать полученное количество
английских слов!   Необходимо, чтобы во входном файле находилось, как минимум, 5 русских слов, которые
имеют несколько английских значений. На хорошую оценку по работе (8, 9 и 10) слова должны быть подобраны так,
как в моём примере, чтобы в результате одно английское слово имело несколько русских значений.
"""


def dict_swap_language(input_file: str, output_file: str) -> ():
    """
    Function read file with russian and english words,swap dictionary and save in your new file.
    :param input_file: The file to be read from.
    :param output_file: the file for save words.
    :return: nothing
    """
    input_txt = open(input_file, "r", encoding="utf-8")
    dictionary = {}
    for row in input_txt:
        split_row = row[:-1].split()  # [:-1] because last symbol /n
        russian, english = split_row[0], split_row[2:]
        for word in english:
            try:
                dictionary[word].append(russian)
            except KeyError:
                dictionary[word] = [russian]

    output_file = open(output_file, 'w', encoding="utf-8")
    output_file.write(f"{len(dictionary)}\n")

    for key in sorted(dictionary):
        output_file.write("{0} - {1}\n".format(key, ", ".join(dictionary[key])))
    print('output saved to file in directory with you program. output.txt')
    input_txt.close()
    output_file.close()


if __name__ == "__main__":
    dict_swap_language("./input.txt", "./output.txt")

