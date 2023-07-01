# def greetings(name, time, temperature):
#     greeting = f'Welcome  {name}, how are you doing this {time}. The temperature over here is {temperature} degree celcius'
#     print(greeting) 
# greetings('Kolawole', 'morning', 21)


# def greet(*name):
#     greeting = f'Welcome {name[1]}'
#     print(greeting)
# greet('John', 'Tim', 'Tome')




def user(name, age, state):
    response = f'Welcome {name}, you are {age} year old. You are from the {state} state, Nigeria'
    print(response)
name = input("Enter your name:\n")
age = input("Enter your age:\n")
state = input("Enter your state:\n")
user(name, age, state)