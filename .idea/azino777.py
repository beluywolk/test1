from random import choice

def casino():
    MY_MONEY2 = 1000
    MY_MONEY1 = MY_MONEY2


    while True:
        if MY_MONEY1 == 0:
            print(' у вас закончились деньги ')
            break

        a1 = choice(range(1, 31))
        a = input(f'ваш бюджет - {MY_MONEY1}\nвведите сумму ставки\n для выхода введите "!"')


        if a == '!':
            print('ПРИХОДИТЕ ЕЩЕ')
            break


        a = int(a)
        if a > MY_MONEY1:
            print('вы не можете поставить столкьо')
            break
        MY_MONEY1 = MY_MONEY1 - a
        a2 = input('выберите число(1, 30)')
        if a1 == int(a2):
            print('you won!')
            MY_MONEY1 = MY_MONEY1 + a * 2
        else:
            print(f'you loose, win = {a1}')
    if MY_MONEY1 > MY_MONEY2:
        print(f'вы в плюсе на {MY_MONEY1 - MY_MONEY2}')
    if MY_MONEY2 > MY_MONEY1:
        print(f'вы в минусе на {MY_MONEY2 - MY_MONEY1}')




