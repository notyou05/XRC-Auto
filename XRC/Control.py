import re

import re

def replace_after_string(file_path, target_string, new_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        if target_string in line:
            index = line.find(target_string) + len(target_string)
            new_line = line[:index] + str(new_number) + '\n'
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(new_lines)

    print(f"Replaced everything after '{target_string}' with '{new_number}'.")




replace_after_string(r"C:\Program Files (x86)\xRC Simulator\Controls.txt", "a=", "0")