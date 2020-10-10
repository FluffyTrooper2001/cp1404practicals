class ProgrammingLanguage():
    def __init__(self, name, typing = "Static", reflection = False, year = "2020"):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    
    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
    
    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False