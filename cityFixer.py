
def detect_city(city_string):
    try:
        split_val = city_string.split(' ')
        str_list = []
        for val in split_val:
            val_list = []
            if val.isalpha():
                val_list.append(val)
            str_list.append("".join(val_list))
        return " ".join(str_list).strip()
    except:
        print('city name contains invalid characters.')


def check_city(city_string):
    if not has_numbers(city_string):
        return detect_city(city_string)
    elif city_string.isalnum():
        return print('city name string characters and digits. -- {}'.format(city_string))
    else:
        return print('city name string characters and digits. -- {}'.format(city_string))


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


class city:
    """ The city design object pattern """
    _city = {}
    def __init__(self):
        self.__str__ = self._city


class cityFixer(city):
    def __init__(self, **kwargs):
        city.__init__(self)
        self._city = check_city(kwargs['city'])

    def __str__(self):
        return str(self._city)

# x = cityFixer(city='abc abc 123')
# print(x)