with open(r'C:\Users\Пользователь\OneDrive\Рабочий стол\PP2\lab1\lab6\dir_and_files\4.txt', 'r') as f1:
    with open('ex7.txt', 'w') as f2:
        f2.write(f1.read())
        