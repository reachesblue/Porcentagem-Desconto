import time
import os

var = int(input('Press 1 to start the program: '))

if var == 1:
    while var == 'yes' or '1':
        print('Program by Riique')
        print('Language: PT-BR')
        print("\n" * 2),
        p = float(input('Qual o preço do produto (Price of Product)? '))
        x = int(input('De quanto será o desconto (Discount Percentage)? '))
        d = (p/100) * x
        v = p-d
        print("\n" * 130),
        print('O produto que custava R${:.2f}, com {}% de desconto vai custar R${:.2f}'.format(p, x, v))
        print('The product that cost R${:.2f}, with {}% discount will cost R${:.2f}'.format(p, x, v))
        time.sleep(3.0)
        print("\n" * 3)
        print('Now, use only "yes" or "1"  ')
        var = input('Gostaria de fazer a conta novamente? (Would you like to make the account again?) ')
        os.system('cls') or None
    else:
        print('Ok, thanks by using the program')    
else:
    print('Ok, thanks by using the program')
time.sleep(3)

"""
Thanks everyone
My GitHub: https://github.com/reachesblue
"""