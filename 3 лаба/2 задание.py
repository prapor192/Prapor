a=input('Введите текст фаила:')
b=input('Дополните текст фаила: ')
new_file = open("user_input1.txt", "w+")
new_file.write(a)
new_file = open("user_input1.txt", "a+")
new_file.write('\n' + b)


new_file.close()