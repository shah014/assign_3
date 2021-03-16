fileName = input("Enter a file name: ")
print(fileName)
fileext = fileName.split('.')
file_for_ext = repr(fileext[-1:])
file_ext_wout_bracs = str(file_for_ext[1:-1])
print(f'The extension of filename: {file_ext_wout_bracs[1:-1]}')

file = repr(fileext[:-1])
file_wout_bracs = str(file[1:-1])
print(f'Filename without extension: {file_wout_bracs[1:-1]}')


