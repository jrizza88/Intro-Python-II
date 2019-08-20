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
        self.items.remove(item)

    def inventory_quantity(self):
        # ', '.join([str(i) for i in self.items])
        if len(self.items) > 1:
            print(f'{self.name} has an inventory of: {len(self.items)} items.')
        elif len(self.items) == 1:
            print(f'{self.name} has an inventory of: {len(self.items)} item.')
        else:
            print(f'{self.name} has no items')

    def items_list(self):
        items_in_room = ', '.join(
            [str(i) for i in self.items])
        print(f'Here are the items in this room: {items_in_room}.')

    def check_item(self, item):
        for i in self.items:
            if i != item: 
                print(f'There are no items')               
                return False
            else:
                print(f'Checking items: {self.items}')
                return True

    # def inventory(self):
    #     print(f'Here are the items listed in {self.name}: {self.items}')