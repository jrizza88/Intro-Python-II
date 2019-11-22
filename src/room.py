# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def __str__(self):
        output = f'room: {self.name}, description: {self.description} \n'
        output += f'Here are the following items in this room: '
        # i = 0 
        for item in self.items:
            if item != self.items:
                output += f'no items here.'
            else:
                output += f' {str(item)}... \n'
                # output += f' {i} in {str(item)} \n'
                # i += 1
        return output
    def desc_only(self):
        return f'Room description is: {self.description}'


