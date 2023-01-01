def reverse(num):
    num = str(num)

    if num[-1] != '0':
        return print(int(str(num)[::-1]))
    else:
        print('Аргумент функции не может оканчиваться на ноль')
        return print(-1)