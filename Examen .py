#Ex 1
# class Animal:
#     def __init__(self, specie, an):
#         self.specie = specie
#         self.an = an
# class Caine(Animal):
#     def __init__(self, specie, an, rasa):
#         super().__init__(specie, an)
#         self.rasa = rasa
#     def afisare_detalii(self):
#         print(f"Specia: {self.specie}, An: {self.an}, Rasa: {self.rasa}")
#
#     def sunet(self):
#         return "Ham-ham"
# class Pisica(Animal):
#     def __init__(self, specie, an, rasa):
#         super().__init__(specie, an)
#         self.rasa = rasa
#     def afisare_detalii(self):
#         print(f"Specia: {self.specie}, An: {self.an}, Rasa: {self.rasa}")
#
#     def sunet(self):
#         return "Miau"
# caine1 = Caine(specie="Caine", an=3, rasa="Labrador")
# caine1.afisare_detalii()
# print("Sunetul emis de acest caine este:", caine1.sunet())
#
# pisica1 = Pisica(specie="Pisica", an=2, rasa="Sphinx")
# pisica1.afisare_detalii()
# print("Sunetul emis de aceasta pisica este: ", pisica1.sunet())

#Ex 4
class StudentList:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = {}

    def add_student(self, **kwargs):
        for name, age in kwargs.items():
            self.students[name] = age
    def display_students(self):
        print(f"Students in class {self.class_name}")
        for name, age in self.students.items():
            print(f"Name: {name}, Age: {age}")

class_12 = StudentList("Class 12")
class_12.add_student(Johnny = 16, Nick = 17, Bob = 18)
class_12.display_students()