"""
POZ-41
Mohorev E.O.
lab4 variant 9
Используя Множества
Во введенном тексте удваивает все прописные(заглвные) гласные буквы, удваивает все цифры
и подсчитывает количество пробелов. На печать выдать исходный текст, количество пробелов и преобразованный текст.
"""


def double_text_and_numbers_and_count_spase(text_for: str) -> [str, int]:
    """
    The function doubles capital letters and counts the number of spaces.
    :param text_for: text for double capital letters and count spaces.
    :return: list(changed list) and integer(count spaces)
    """
    set_uppercase_vowels = set("АЯУЮОЕЁЭИЫAEIOUY")
    set_numbers = set("0123456789")
    count_spase = 0
    result_text = ""
    for _ in text_for:
        result_text += _
        if _ == " ":
            count_spase += 1
        elif _ in set_uppercase_vowels or _ in set_numbers:
            result_text += _
    return result_text, count_spase


def test_double_text_and_numbers_and_count_spase():
    result_text, count_space_ = double_text_and_numbers_and_count_spase("123ыыЫ")
    assert result_text == "112233ыыЫЫ" and count_space_ == 0
    result_text, count_space_ = double_text_and_numbers_and_count_spase("123 ыыЫ")
    assert result_text == "112233 ыыЫЫ" and count_space_ == 1
    result_text, count_space_ = double_text_and_numbers_and_count_spase("""Lorem Ipsum is simply dummy text of the \
printing and typesetting industry. Lorem Ipsum""")
    assert result_text == """Lorem IIpsum is simply dummy text of the \
printing and typesetting industry. Lorem IIpsum""" and count_space_ == 13


if __name__ == "__main__":
    test_double_text_and_numbers_and_count_spase()
    text = input("input your text please>")
    print("text before =", text)
    result_Text, count_space = double_text_and_numbers_and_count_spase(text)
    print(f"count space = {count_space}")
    print(f"result text = {result_Text}")
