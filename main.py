# coding:utf-8
import re


def check_input(id_number):
    if len(id_number) == 18:
        pass
    else:
        exit(" error")

    try:
        id_number_0_17 = id_number[:17]
        pattern = re.compile(r'^\d{17}')
        res = pattern.match(id_number_0_17)
        res.group(0)
        id_number_18 = id_number[17]
        pattern = re.compile(r'[123456789xX]')
        res = pattern.match(id_number_18)
        res.group(0)
    except AttributeError:
        exit(" AttributeError")


def check_id(id_number):
    res = 0
    factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    res_correct = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
    for a, b in zip(id_number[:17], factor):
        res += int(a) * b
    res = res % 11
    last_number = str(res_correct[res])
    if id_number[17] == "x":
        id_number = id_number.replace("x", "X")
    if last_number == id_number[17]:
        print(" id number is correct")
        judge_sex(id_number)
    else:
        print(" the correct number is: " + id_number[:17] + last_number)
        exit(" input id number is break ")


def judge_sex(id_number):
    num = int(id_number[16])
    if (num % 2) == 0:
        print(" sex is woman")
    else:
        print(" sex is man")


if __name__ == "__main__":
    id_number_input = input(" input id number: ")
    check_input(id_number_input)
    check_id(id_number_input)
