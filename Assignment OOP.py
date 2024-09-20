class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def displayDetails(self):
        print(f"Welcome {self.name}! You are {self.age} years old and identify as {self.gender}.")
    
def userInput():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    while not age.isdigit():
        print("Invalid Entry!! Please enter a valid age.")
        age = input ("Please enter your age: ")
    gender = input("Please enter your gender: ")
    
    return name, age, gender

name, age, gender = userInput()

person1 = Person(name, age, gender)
person1.displayDetails()