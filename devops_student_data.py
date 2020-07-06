from student_data import Student


class Devops(Student):
    def __init__(self, first_name, last_name, stream): # This adds an attribute "stream" to the devops sub class.
        self.first_name = first_name
        self.last_name = last_name
        self.stream = stream

    def full_name(self):
        print(self.first_name, " ", self.last_name)

    def roll_call(self):
        print("I am a Devops Student")

    def __change_name(self, first_name, last_name): # this is a private method as changing someones name shouldbnt be easily accessible
        self.first_name = first_name
        self.last_name = last_name


s = Student("ayb", "bocs")

s._Student__change_name("Ib", "Bocus") # this name mangling is a method to call the hidden method
s.full_name()
