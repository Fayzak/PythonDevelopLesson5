from packet import module
n = int(input("Введите натуральное число от 1 до 1000: "))
if n < 0:
    print('Вы ввели не натуральное число')
elif n > 1000:
    print('Вы ввели натуральное число, больше 1000')
else:
    module.num_div_max(n)
    module.num_divs_canon(n)
    module.num_div_max_simple(n)
    module.num_divs(n)
    module.num_simple(n)