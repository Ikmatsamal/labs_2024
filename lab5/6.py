def replace_chars_with_colon(input_string):
    chars_to_replace = [' ', ',', '.']
    for char in chars_to_replace:
        input_string = input_string.replace(char, ':')
    return input_string

def replace_in_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as file:
        text = file.read()
    modified_text = replace_chars_with_colon(text)
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(modified_text)

input_filename = 'lab5/row.txt'  # Update with your input file name
output_filename = 'row_modifed.txt'  # Update with your output file name
replace_in_file(input_filename, output_filename)
print(output_filename)