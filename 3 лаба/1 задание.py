a = input('Выберите вариант чтения 1 или 2: ')
print(a)
if int(a)==1:
    f=open(r"C:\Users\user\Desktop\igfj\example.txt").read()
    print(f)
else:
    f=open(r"C:\Users\user\Desktop\igfj\example.txt").readlines()
    print(f)