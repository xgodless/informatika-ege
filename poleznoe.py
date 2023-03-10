#Делаем это все в cmd
#В Python есть интересные функции bin(), oct() и hex(). С их помощью можно перевести любое число в 2-ичную, 8-ичную и 16-ичную системы счисления.
#Пример:
bin(156) #Выводит '0b10011100', где число после '0b' - двоичное число
oct(156) #Выводит '0o234', где число после '0o' - восьмеричное число
hex(156) #Выводит '0x9c', где число после '0x' - шестадцатиричное число

#Программа для перевода в любую систему счисления:

def convert_base(num, to_base=10, from_base=10):
    # Перевод в десятичную систему
    if isinstance(num, str): # Если число - строка, то ...
        n = int(num, from_base) # ... переводим его в нужную систему счисления
    else: # Если же ввели число, то ...
        n = int(num) # ... просто воспринять его как число
    # Перевод десятичной в 'to_base' систему
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Берём алфавит
    if n < to_base: # Если число меньше системы счисления в которую переводить...
        return alphabet[n] # ... вернуть значения номера в алфавите (остаток от деления)
    else: # Иначе...
        return convert_base(n // to_base, to_base) + alphabet[n % to_base] # ... рекурсивно обратиться к функии нахождения остатка
print(convert_base(247, 4, 10)) # Использование: print(convert_base(число, система в которую переводим, система из которой переводим))
# А введя print(convert_base('23', 21, 4)) переведёт 23 из 4-ичной в 21-ичную систему
