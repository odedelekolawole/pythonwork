# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
  
# name = input("Enter your name:  ")
# age = input("Enter your age:  ")

# p1 = Person(name, age)
# print(p1.name)
# print(p1.age)


# This section shows how to delete in  a class

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 10)
del p1
print(p1.name)