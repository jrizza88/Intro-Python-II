class Item: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
# repr is good at helping to give devs more information / gives official deets of what value reps
# can help give info about the class, extra info that is useful to present
# i.e. 
    def __repr__(self):
        return f" (name info):{self.name}, (descrip info):{self.description}"
# str is usually meant for consumer 
    def __str__(self):
        return f"{self.name}"