dia = int(input('digite um dia'))
mes = int(input('digite um mês'))

if  mes == 12 and 31>= dia > 22 or mes == 1 or mes ==2 or mes == 3 and dia<20:
    print('verão')
elif mes == 4 and 31 >=dia>= 20  or mes ==5 or mes == 6 and dia<21:
    print('outono')
elif mes == 7 and 31 >=dia>= 21 or mes ==8 or mes == 9 and dia<23:
    print('inverno')
elif mes == 10 and 31 >=dia>= 23 or mes ==11 or mes == 12:
    print('primavera')
else:
    print('escolha um número que preste!')
