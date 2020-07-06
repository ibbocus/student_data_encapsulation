class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        print(self.first_name, " ", self.last_name)

    def roll_call(self):
        print("I am a student")

    def __change_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# s = Student("ayb", "bocs")
# s._Student__change_name("Ib","Bocus")
# s.full_name()
