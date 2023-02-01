"""
POZ41
Mokhorev E.O
Lab 6
Variant 9

Написать программу на языке Python, реализующую решение задачи с использованием строкового типа данных.
Программу просчитать для различных исходных данных.
Дан текст. Создать новый текст, в котором все слова, которые начинаются на ту же букву,
что и слово минимальной длины, продублировать.

при решении считалось что символы,цифры могут разделять слова, но частью слова не являются.
"""


def first_letter_of_smallest_first_word(text: str) -> str:
    """
    The function takes a text and find the first letter of the shortest word in text.
    !function save case first letters,
    :param text: text for find first smallest letter
    :return: the first letter of the smallest first word
    """
    string_for_check = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяA' \
                       'BCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'  # letter russian and eng

    len_smallest_word = len(text)
    text += " "  # Workaround, without this we can get IndexOutOfRangeException
    first_letter_smallest_words = ""
    i = 0

    while i < len(text):
        # here we work with first letter
        if text[i] in string_for_check:
            count_letter = 1  # nullified last, and add first count
            temp_first_letter = text[i]
            i += 1
            while text[i] in string_for_check:
                # here we work with others letters
                count_letter += 1
                i += 1
            else:
                i += 1
                # when the word is over we get here
                if len_smallest_word > count_letter:
                    len_smallest_word = count_letter
                    first_letter_smallest_words = temp_first_letter
        else:
            i += 1
    if len(first_letter_smallest_words) == 0:
        return "don't have words"
    return first_letter_smallest_words


def test_first_letter_of_smallest_first_word():
    assert first_letter_of_smallest_first_word("несколько1слов2для3примера") == "д"
    assert first_letter_of_smallest_first_word("some1text2for3example") == "f"
    assert first_letter_of_smallest_first_word("SOME1TEXT2FOR3EXAMPLE") == "F"
    assert first_letter_of_smallest_first_word(" 2 example 4 {text}") == "t"
    assert first_letter_of_smallest_first_word("0 1 2 3 4 5 6 7 9 1") == "don't have words"
    assert first_letter_of_smallest_first_word("O 0 1 2 3 4 5 6 7 9 1") == "O"
    assert first_letter_of_smallest_first_word("SOs{ME}1TE/XT,2FOsR3Et12a XAMPLE") == "a"
    assert first_letter_of_smallest_first_word("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


def delete_all_words_without_need_first_letter(text_for_del: str, first_letter: str) -> str:
    """
    the function takes text and removes all words where the first letter not the one you mentioned.
    function save case, delete excess space.
    :param text_for_del: text for work.
    :param first_letter: desired letter.
    :return: where all words start with the same letter.
    """
    assert len(first_letter) == 1, "len letter not equal 1"
    string_for_check = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюяA' \
                       'BCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'  # letter russian and eng
    text = text_for_del + " "  # Workaround, without this we can get IndexOutOfRangeException
    new_text = ""
    i = 0
    while i < len(text):
        # here we work with first letter
        if text[i] == first_letter.lower() or text[i] == first_letter.upper():
            new_text += text[i]
            i += 1
            while text[i] in string_for_check:
                # here we work with others letters
                new_text += text[i]
                i += 1
            else:
                new_text += text[i]
                i += 1
        elif text[i] not in string_for_check:  # it's symbol saved it.
            new_text += text[i]
            i += 1
        else:  # it's not need words just skip
            while text[i] in string_for_check:
                i += 1
    new_text = new_text.strip()
    while "  " in new_text:
        new_text = new_text.replace("  ", " ")  # del double space
    return new_text


def test_delete_all_words_without_need_first_letter():
    assert delete_all_words_without_need_first_letter("qwe asds            qwwwww", "q") == "qwe qwwwww"
    assert delete_all_words_without_need_first_letter("несколько1слов2для3примера", "д") == "12для3"
    assert delete_all_words_without_need_first_letter("some1text2for3example", "f") == "12for3"
    assert delete_all_words_without_need_first_letter("SOME1TEXT2FOR3EXAMPLE", "F") == "12FOR3"
    assert delete_all_words_without_need_first_letter(" 2 example 4 {text}", "t") == "2 4 {text}"
    assert delete_all_words_without_need_first_letter("0 1 2 3 4 5 6 7 9 1", "a") == "0 1 2 3 4 5 6 7 9 1"
    assert delete_all_words_without_need_first_letter("O 0 1 2 3 4 5 6 7 9 1", "O") == "O 0 1 2 3 4 5 6 7 9 1"
    assert delete_all_words_without_need_first_letter("SOs{ME}1TE/XT,2FOsR3Et12a XAMPLE", "a") == "{}1/,2312a"
    assert delete_all_words_without_need_first_letter("aaaaaaaaaaaaaaaaaaaa bbbbbbbbb", "a") == "aaaaaaaaaaaaaaaaaaaa"


if __name__ == "__main__":
    test_first_letter_of_smallest_first_word()  # tests def find first letters the smallest word.
    test_delete_all_words_without_need_first_letter()  # tests delete words without the necessary first letter.

    text_for_work = input("please, input your text ->")
    first_letter_smallest = first_letter_of_smallest_first_word(text_for_work)
    result = delete_all_words_without_need_first_letter(text_for_work, first_letter_smallest)
    print("your text =", text_for_work)
    print("result text =", result)
    print("end")
