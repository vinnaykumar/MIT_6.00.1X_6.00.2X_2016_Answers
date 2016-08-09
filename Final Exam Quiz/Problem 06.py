""" Following are solutions for Final Exam. """


# Final Exam - Problem 06 - Part 01
class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: It is obvious that ' + Person.say(self,stuff)
    def lecture(self, stuff):
        return 'It is obvious that '+ Person.say(self, stuff)



# Final Exam - Problem 06 - Part 02
class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return self.name + ' says: It is obvious that I believe that ' + Person.say(self,stuff)
    def lecture(self, stuff):
        return 'It is obvious that I believe that '+ Person.say(self, stuff)



# Final Exam - Problem 06 - Part 03
class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return "Prof. " + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return Professor.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)

# Following are a few test cases    
e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')
