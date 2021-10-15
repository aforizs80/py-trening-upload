class Employee:

    def __init__(self, first_name, last_name, age):
        print("konstruktor")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def get_name(self):
    return self.first_name + " " + self.last_name

def inc_age(self):
    self.age +=1

john = Employee("john", "doe", 30)
print(john.first_name)
print(john.last_name)
print(john.age)




