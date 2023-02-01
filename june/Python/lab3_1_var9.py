"""
POZ-41
Mokhorev E.O
lab 2 variant 9
Дан целочисленный вектор А(n). Проверьте, есть ли в нем отрицательные элементы.
Если есть, найдите наибольшее i, при котором А[i]<0.
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


def check_negative_and_return_the_last_negative(list_for_check: list) -> [int]:
    """
    This function checks for negative elements and returns the index of the last negative element,
    if there are no negative elements, it will return "-1"
    :param list_for_check: list in which to find the last negative
    :return: index last negative or "-1" if doesn't have it.
    """
    for i in range(-1, -len(list_for_check)-1, -1):
        if list_for_check[i] < 0:
            return len(list_for_check) + i
    return -1
    pass


def test_check_negative_and_return_the_last_negative():
    assert check_negative_and_return_the_last_negative([0]) == -1
    assert check_negative_and_return_the_last_negative([1, -2, -3, 4, 5]) == 2
    assert check_negative_and_return_the_last_negative([1, 5, -3, 4, 5]) == 2
    assert check_negative_and_return_the_last_negative([1, 5, 5, 5, 5]) == -1
    assert check_negative_and_return_the_last_negative([1, -2, -3, 4, 5]) == 2
    assert check_negative_and_return_the_last_negative([-1, -2, -3, 4, 5]) == 2
    assert check_negative_and_return_the_last_negative([1, -2, 3, 4, -5]) == 4
    assert check_negative_and_return_the_last_negative([0, 0, 0, 0, 0]) == -1
    assert check_negative_and_return_the_last_negative([-4, -3, -2, -1, 0]) == 3
    assert check_negative_and_return_the_last_negative([-1, -2, -3, -4, -5]) == 4


if __name__ == "__main__":
    test_check_negative_and_return_the_last_negative()  # test main function
    try:
        n = int(input("please write len list >"))
        if n > 0:  # check negative length
            list_for_find_last_negative = make_list(n)  # we can use int and float, default its integer.
            index_last_negative = check_negative_and_return_the_last_negative(list_for_find_last_negative)
            if index_last_negative >= 0:
                print(f"index last negative = {index_last_negative}")
            else:
                print("list don't have negative")
        else:
            print("length cannot be less than 1")
    except ValueError:
        print("list length can only be integer")
        exit(0)  # if error program will close
