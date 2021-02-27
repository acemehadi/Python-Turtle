class Animal:
    def __init__(self, animal, name, color, behave):
        self.animal = animal
        self.name = name
        self.color = color
        self.quality = behave

    def set_name(self, new_name):
        self.name = new_name

    def get_details(self):
        return f"Animal: {self.animal},name :{self.name},Color :{self.color}, Behave: {self.quality} "


one_animal = Animal("cat", "White_ninja", "white", "angry")

print(one_animal.get_details())

one_animal.set_name("white x")
print(one_animal.get_details())
