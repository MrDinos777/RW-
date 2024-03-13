import os

file_list = ['1.txt', '2.txt']

file_list.sort(key=lambda x: sum(1 for line in open(x)), reverse=True)

with open('result.txt', 'w') as result_file:
    for file in file_list:
        with open(file, 'r') as current_file:
            result_file.write(f'{file}\n{sum(1 for line in current_file)}\n')
            result_file.write(current_file.read())