# Implement a class to hold room information. This should have 
# name and description attributes.
  #  def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None ):
class Room: 
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to
        if items is None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return str(self.__dict__)
    
    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.append(item)

    def items_list(self):
        return ', '.join([str(i) for i in self.items])

    def check_item(self, item):
        for i in self.items:
            if i != item: 
                print(f'There are no items')               
                return False
            else:
                print(f'Checking items: {self.items}')
                return True

