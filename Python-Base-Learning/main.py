"""
! Найти все делители числа N и записать его в словарь
"""

def Div(n):
    result = [1, n]
    for i in range(2, n):
        if n % i == 0:
            result.append(i)
    return sorted(result)


def addDiv():
    result_dict = {}
    n = int(input("Введите свое число: "))
    result_dict[n] = Div(n)

    return result_dict


x=7
y=5

print("{x} sdopjgspog {y}")
print(f"{x} sdopjgspog {y}")



