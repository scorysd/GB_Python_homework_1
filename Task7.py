# проверить число на простоту (т.е. что число делится только на 1 и само на себя)
def prime_number(n):
    j = 0
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            j += 1
    if (j <= 0):
        print(f'Число {n} простое')
    else:
        print(f'Число {n} не является простым')
prime_number(int(input('Введите число:')))