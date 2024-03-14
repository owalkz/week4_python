class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi. My name is {self.name} and I am {self.age} years old. I am a {self.gender}")
        
personA = Person("John", 25, "Male")
personA.introduce()