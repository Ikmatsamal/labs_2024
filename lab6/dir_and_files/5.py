with open(r'C:\Users\Пользователь\OneDrive\Рабочий стол\PP2\lab1\lab6\dir_and_files\5.txt', 'w',) as f:
    lst = [1, 'is', 'mine', [1, 1, 1], (1, 7), {1: 5}, {1, 4, 5}]
    
    # Записываем элементы в одну строку через пробел
    f.write(' '.join(map(str, lst)) + '\n')

    # Записываем каждый элемент на отдельной строке
    f.writelines(str(item) + '\n' for item in lst)
