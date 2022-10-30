import pandas

class city:
    """ The city design object pattern """
    _city =

class city_fixer:
    def __init__(self, city_string):
        self.city_string = city_string

    def detect_city(city_string):
        try:
            split_val = city_string.split(' ')
            str_list = []
            for val in split_val:
                # print(val, 'printing elements by splitting string')
                val_list = []
                if val.isalpha():
                    val_list.append(val)
                str_list.append("".join(val_list))
            return " ".join(str_list).strip()
        except:
            print('string contains invalid characters.')

    def check_city(city_string):
        if not has_numbers(city_string):
            return detect_city(city_string)

        # if city_string.isalpha():
        #     return detect_city(city_string)
        elif city_string.isalnum():
            return print('city contains string characters and digits. -- {}'.format(city_string))
        else:
            return print('city contains string characters and digits. -- {}'.format(city_string))

    def has_numbers(inputString):
        return any(char.isdigit() for char in inputString)


def check_city(city_string):
    city = city_fixer(city_string)
    return city.check_city()