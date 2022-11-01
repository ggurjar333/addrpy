from common import has_numbers
def detect_zipcode(zipcode_string):
    try:
        split_val = zipcode_string.split(' ')
        str_list = []
        for val in split_val:
            val_list = []
            if val.isalpha():
                val_list.append(val)
            str_list.append("".join(val_list))
        return " ".join(str_list).strip()
    except:
        print('zipcode_string name contains invalid characters.')


def check_zipcode(zipcode_string):
    if not has_numbers(zipcode_string):
        return detect_zipcode(zipcode_string)
    elif zipcode_string.isalnum():
        return print('zipcode string characters and digits. -- {}'.format(zipcode_string))
    else:
        return print('zipcode string characters and digits. -- {}'.format(zipcode_string))

class zipcode:
    """ The city design object pattern """
    _zipcode = {}
    def __init__(self):
        self.__str__ = self._zipcode


class zipcodeFixer(zipcode):
    def __init__(self, **kwargs):
        zipcode.__init__(self)
        self._zipcode = check_zipcode(kwargs['zipcode'])

    def __str__(self):
        return str(self._zipcode)

# x = zipcodeFixer(zipcode='65123')
# print(x)