import os
path = r'C:\Users\Пользователь\OneDrive\Рабочий стол\PP2\lab1\lab6\dir_and_files\4.txt'
with open(path, 'r') as f:
     lines = f.readlines()
     print(f"Количество строк в файле {os.path.basename(path)}: {len(lines)}")

