'''
By using multiple inheritace we can use attributes and functions of inherited class to our defined class
This makes our works easy by not dublicating code and helps in reduction of code repeatation
ordering matters herr
'''

class Employee:
    no_of_leaves = 8
    var = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game
    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"


class Both(Player, Employee):
    language = "Python"
    def printlanguage(self):
        print(self.language)



emp1 = Employee("Jack", 255, "Teacher")
emp2 = Employee("Rose", 455, "CA")

play1 = Player("Alex", ["Soccer"])
bot = Both("Manav",["Soccer"])

print(bot.var)

