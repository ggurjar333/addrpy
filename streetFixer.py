from common import has_numbers

def check_street_address(street_address):
    try:
        split_val = street_address.split(' ')
        str_list = []
        for val in split_val:
            val_list = []
            if val.isalnum() or val.isalpha() or val.isdigit():
                val_list.append(val)
            str_list.append("".join(val_list))
        return " ".join(str_list).strip()
    except:
        print('street_address contains invalid characters.')

class streetAddr:
    _streetAddr = {}
    def __init__(self):
        self.__str__ = self._streetAddr

class streetAddress(streetAddr):
    def __init__(self, **kwargs):
        streetAddr.__init__(self)
        self._streetAddr = check_street_address(kwargs['streetAddress'])