import os
import string
path = r'C:\Users\Пользователь\OneDrive\Рабочий стол\PP2\lab1\lab6\dir_and_files\ex6_A-Z_files'
os.makedirs(path, exist_ok=True)
for letter in string.ascii_uppercase:
    filename = os.path.join(path, f"{letter}.txt") 
    with open(filename, 'w') as f:
        f.write(f"This is file {letter}.txt") 
print("Файлы A-Z успешно созданы!")
