"""
! Найти все делители чисел от 2 до N и записать его в словарь
"""
result_dict = {}
n = int(input("Введите свое число: "))

def Div(n):
    result = [1, n]
    for i in range(2, n):
        if n % i == 0:
            result.append(i)
    return sorted(result)


def DivAll(n):
    for i in range(2, n+1):
        result_dict[i] = Div(i)


DivAll(n)
print(result_dict)
