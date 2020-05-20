class Employee:
    def __init__(self, firstname, lastname, salary=0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    def give_raise(self, funds=''):
        if funds:
            self.salary += int(funds)
        else:
            self.salary += 5000
            
