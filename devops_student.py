from student_data import Student


class Devops(Student):
    def __init__(self, first_name, last_name):
        super(Devops, self).__init__(first_name, last_name)

    def full_name(self):
        print(self.first_name, " ", self.last_name)

    def roll_call(self):
        print("I am a Devops Student")


s = Student("ayb", "bocs")
d = Devops("ayb", "bocs")


# s.change_name("Ib", "Bocus")
# s.full_name()
#
# d.change_name("Ib", "Bocus")
# d.full_name()

s._Student__change_name("Ib", "Bocus") # this name mangling is a method to call the hidden method
s.full_name()

d._Student__change_name("Ib", "Bocus") # this name mangling is a method to call the hidden method
d.full_name()


