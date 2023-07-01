# def greetings(name, time, temperature):
#     greeting = f'Welcome  {name}, how are you doing this {time}. The temperature over here is {temperature} degree celcius'
#     print(greeting) 
# greetings('Kolawole', 'morning', 21)


# def greet(*name):
#     greeting = f'Welcome {name[1]}'
#     print(greeting)
# greet('John', 'Tim', 'Tome')




def user(name, age):
    response = f'Welcome {name}, you are {age} year old'
    print(response)
name = input("Enter your name:\n")
age = input("Enter your age:\n")
user(name, age)