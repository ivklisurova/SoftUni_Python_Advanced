from os import remove

file_path = 'text.txt'
try:
    remove(file_path)
except:
    print('File already deleted!')
