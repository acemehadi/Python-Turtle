class Person:
    def __init__(self, name: str, age: int, born: int):
        self.__name = name
        self.__age = age
        self.__date_of_birh = born

    def name(self):
        return self.__name

    def get_of_birth(self):
        return self.__date_of_birh

    def set_new_name(self, new_name):
        if __has_any_number(new_name):
            print("plz enter only text")
            return
        self.__name = new_name

    def get_details(self):
        return f"Name :{self.__name}\nAge  :{self.__age}\nBorn :{self.__date_of_birh}"

    def __has_any_number(self, string):
        return "0" in string


person_list = [(Person("Mehadi", 17, 2004)),
               Person("Captain jack", 60, 1989),
               Person("Stevs jobs", 60, 1960),
               Person("Rhaan paul", 30, 1990)
               ]
# for person in person_list:
#    if person.get_of_birth() >= 1960:
#        print(person.get_details())


# Creat a new class :

class Student(Person):
    def __init__(self, name, age, born, phone_number: int, students_id: str):
        super().__init__(name, age, born)
        self.phone = phone_number
        self.student_id = students_id

    def get_details(self):
        return f"Name :{self.name()} \n Born{self.get_of_birth()}\nNo :{self.phone}"

    def __str__(self):
        return f"Name :{self.name()} \n Born{self.get_of_birth()}\nNo :{self.phone}"


student_one = Student("mehadi", 17, 2004, 1922571100, "GSCA-20210022")
print(student_one)


class Teacher(Person):
    def __init__(self, name, age, born, deparment: str):
        super().__init__(name, age, born)
        self.dep = deparment


new_person_list = [
    Person("mehadi", 17, 2020),
    Student("S", 17, 2000, 1922571100, "Gsca -11"),
    Teacher("s", 50, 1990, "CSE")
]

for mix in new_person_list:
    print(mix.get_details())
