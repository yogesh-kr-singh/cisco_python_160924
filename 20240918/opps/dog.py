class Dog:
    # Class attribute
    species = "Canis lupus familiaris"
    
    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating an object (instance of the class)
dog1 = Dog("Buddy", 3)
print(dog1.description())  # Output: Buddy is 3 years old.
print(dog1.speak("Woof!"))  # Output: Buddy says Woof!

dog2 = Dog("Duggu", 6)
print(dog2.description())  # Output: Duggu is 6 years old.
print(dog2.speak("Bhooww!"))  # Output: Duggu says Woof!

from functools import reduce
dogs = [dog1,dog2]
# reduce syntax
# reduce (<func>, iterable, init_value) 
ages_sum = reduce(lambda s, dog: s+ dog.age, dogs, 0) # s=0 
#for i in nums: [1,2,3,4] i->1 , 2, 3, 4
print(ages_sum)


