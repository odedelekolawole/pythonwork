# try:
#     x = int(input('Input an integer:  '))
#     print(x)
# except:
#     print('Somethong went wrong')
# else:
#     print('Nothing went wrong')


try:
    x = int(input('Input an integer:  '))
    print(x)
except:
    print('Somethong went wrong')
finally:
    print('Try except finished')

# This is a way that we can display the error message by oursellvesusin the try and except function


# try:
#     x = int(input('Input an integer:  '))
#     print(x)
# except ValueError:
#     print('Value not an integer')