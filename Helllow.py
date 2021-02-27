class Animal:
    def __init__(self, animal, name, color, behave):
        self.animal = animal
        self.name = name
        self.color = color
        self.quality = behave

    def set_name(self, new_name):
        if (self.__hash_any_number(new_name)):
            print("Sorry Person name can't have any number")
            return
        self.name = new_name

    def __hash_any_number(self, string):
        return "0" in string

    def get_details(self):
        return f"Animal: {self.animal},name :{self.name},Color :{self.color}, Behave: {self.quality} "


one_animal = Animal("cat", "White_ninja", "white", "angry")
print(one_animal.get_details())
one_animal.set_name("white x")
print(one_animal.get_details())
one_animal.set_name("0whitex")
print(one_animal.get_details())
