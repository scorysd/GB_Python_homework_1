# найти факториал числа
def fucktorial(n):
    if n == 0:
        return 1
    return fucktorial(n-1) * n
print(fucktorial(5))