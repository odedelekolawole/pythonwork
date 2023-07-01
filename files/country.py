# This Section is for reading of files

# files = open('files/countries.txt', 'r')
# print(files.readable())
# print(files.readlines())
# print(files.readlines()[3])
# for lines in files.readlines():
#     print(lines)
# files.close()




# This Section is for reading of files
# files = open('files/country.txt', 'w')
# files.write('This is the new country list file')



# This Section is for appending to the files
# files = open('files/countries.txt', 'a')
# files.write('\nThis is a new line that I just wrote')

# This section is using Python to open and write in new python file
new_file = open('files/pythonfile.py', 'w')
new_file.write('print("This is a new file")')