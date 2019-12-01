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
        output += f' \n List of items in room: {self.print_item()} \n'
        #output += f'items in this room: {self.check_item()}'
        return output
        # output += f'Here are the following items in this room:'
        # i = 0 
        # for item in self.items:
        #     output += f' {i}....{str(item)}.. \n'
        #         # output += f' {i} in {str(item)} \n'
        #     i += 1
        # return output

    
    def check_item2(self, item):
        for i in self.items:
            if i.name != item: 
                print(f'There are no items item 2')               
                return False
            else:
                print(f'Checking items in this room: {self.items[i]}')
                return True

    def check_items3(self, item):
        for i in self.items:
            if i == item:
                # print(i)
                # print(item)
                print(f'Here are the items: {self.items.print_item}')
                return True
            else:
                # print(i)
                # print(item)
                print(self.items)
                return False

    def check_item(self, item):
        for i in self.items:
            if i != item: 
                print(f'There are no items original')               
                return False
            else:
                print(f'Checking items: {self.items[i].item}')
                return True

    def print_item(self):
        if self.items == []:
            output = f'No items found.....'
            print(output)
            return output
        else:
            # output = f'\n name --- {self.items}, -- name '
            output = ';\n '.join([str(i) for i in self.items])
            return output

    # def items_list(self):
    #     items_in_room = ', '.join(
    #         [str(i) for i in self.items])
    #     print(f'Here are the items in this room: {items_in_room}.')
        

        # for i in self.items:
        #     if i != item:
        #         print(item)
        #         # print({self.items})
        #         output += f'no items here. '
        #     else:
        #         output += f' {i}....{str(item)}... {self.items}.. \n'
        #         # output += f' {i} in {str(item)} \n'
        #         i += 1
        # return output
        
    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def desc_only(self):
        return f'Room description is: {self.description}'


