a = input('Выберите вариант чтения 1 или 2: ')
print(a)
try:
    if int(a)==1:
        f=open(r"C:\Users\user\Desktop\igfj\examp.txt").read()
        print(f)
    else:
        f=open(r"C:\Users\user\Desktop\igfj\examp.txt").readlines()
        print(f)
except FileNotFoundError:
    print("Файл не найден. Пожалуйста, убедитесь, что вы ввели правильное название файла.")
    