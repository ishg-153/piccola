class Dog:
    animal = 'dog'
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color

Aldo = Dog("Labrador","Yellow")
Guppy = Dog("Chihuahua","Black")

print("Details of Aldo: ")
print("Aldo is a ", Aldo.animal)
print("Breed: ",Aldo.breed)
print("Color: ",Aldo.color)

print("\nDetails of Guppy: ")
print("Guppy is a ", Guppy.animal)
print("Breed: ",Guppy.breed)
print("Color: ",Guppy.color)
