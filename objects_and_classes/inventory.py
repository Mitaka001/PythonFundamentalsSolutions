class Inventory:
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > 0:
            self.items.append(item)
            self.__capacity -= 1
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return len(self.items)

    def __repr__(self):
        returned_string = f"Items: {', '.join(self.items)}.\n"
        returned_string += f"Capacity left: {self.__capacity}"
        return returned_string


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
