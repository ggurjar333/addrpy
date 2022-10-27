class addr:
    """ The addr design pattern """
    _shared_data = {} # Attribute dictionary
    def __init__(self):
        self.__dict__ = self._shared_data # Make an address attribute dictionary


class addr_singleton(addr):
    """ The addr_singleton class """
    def __init__(self, **kwargs):
        addr.__init__(self)
        self._shared_data.update(kwargs) # Update the address attribute dictionary by inserting key-value pair

    def __str__(self):
        return str(self._shared_data) # Return the string representation of the address attribute dictionary


# x = addr_singleton(street_address = '123', city = '', state = 'IL')
# # print(x)
# y = addr_singleton(street_address = '123', city='New City')
# z = addr_singleton(street_address = '323', state = 'IL')
# # print(y)
# k = addr_singleton(street_address = '123')
# # print(z)
# print(k)
# # print(addr_singleton(street_address = '456', state = 'IL'))