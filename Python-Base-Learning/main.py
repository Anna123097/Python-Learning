"""
! Найти все делители числа N и записать его в словарь
"""
result_dict = {}


def Div(n):
    result = [1, n]
    for i in range(2, n):
        if n % i == 0:
            result.append(i)
    return sorted(result)


n = int(input("Введите свое число: "))
result_dict[n] = Div(n)

print(result_dict)
