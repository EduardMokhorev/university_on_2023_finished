"""
POZ-41
Mokhorev E.O
lab 2_2 variant 9
Дан целочисленный вектор А(n). Построить вещественный вектор B(n),
i-ый элемент которой равен среднему арифметическому двух соседних элементов вектора
А: В [i]= =(А[i]+А[i+1])/2, (и B[10]=A[10]).
"""


def make_list(len_list: int, type_list: [float, int] = int) -> list:
    """
    This function takes the length of the array, and optionally the data type,
    the input of the array in the function is done manually. Returns a list
    _
    :param len_list: enter the length of the array.
    :param type_list: default integer, but you can use float.
    :return list: list with type int or float.
    """
    try:
        return_list = [type_list(input(f"input {i} el> ")) for i in range(len_list)]
        return return_list
    except Exception:
        print(f"You can use only type {type_list}, start over")
        return make_list(len_list, type_list)


def make_list_b_equals_a_i_plus_ai_plus1(list_a: list) -> [list, str]:
    """
    The function takes a list A and return list b[i] = a[i] + a[i+1] but b[last]=a[last].
    Return list b or string on error.
    :param list_a: List for make list b
    :return: return list b[i] = a[i] + a[i+1] but b[last]=a[last] if error return "you need use only integer"
    """
    try:
        if len(list_a) > 0:
            list_temp = [float(list_a[i]) for i in range(len(list_a))]
            list_b = [float(list_temp[i] + list_temp[i + 1]) for i in range(len(list_a) - 1)]
            list_b.append(float(list_temp[-1]))
            return list_b
    except ValueError:
        return "you need use only integer"


def test_make_list_b():
    assert make_list_b_equals_a_i_plus_ai_plus1([1, 1, 1, 1, 1]) == [2.00, 2.00, 2.00, 2.00, 1.00], "doesn't work"
    assert make_list_b_equals_a_i_plus_ai_plus1([0, 0, 0, 0, 0]) == [0.00, 0.00, 0.00, 0.00, 0.00], "zero error"
    assert make_list_b_equals_a_i_plus_ai_plus1([5, -5, 2, -2, 5]) == [0.00, -3.00, 0.00, 3.00, 5.00], "negative number"
    assert make_list_b_equals_a_i_plus_ai_plus1(["0", "5", "0", "0"]) == [5.00, 5.00, 0.00, 0.00], "string number"
    assert make_list_b_equals_a_i_plus_ai_plus1(["0", "0", "x0", "0"]) == "you need use only integer", "Type error"


if __name__ == "__main__":
    test_make_list_b()
    try:
        n = int(input("please write len list >"))
        if n > 0:  # check negative length
            made_list_a = make_list(n)  # we can use int and float, default its integer.
            print(f"your list = {made_list_a}")
            made_list_b = make_list_b_equals_a_i_plus_ai_plus1(made_list_a)
            print(f"your result list = {made_list_b}")
        else:
            print("error len < 0")
    except ValueError:
        print("list length can only be integer")
        exit(0)  # if error program will close
