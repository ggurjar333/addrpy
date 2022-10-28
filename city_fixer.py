import pandas
class city_fixer:
    def __init__(self):
        pass

    def detect_city(city_string):
        try:
            split_val = city_string.split(' ')
            str_list = []
            for val in split_val:
                # print(val)
                val_list = []
                if val.isalpha():
                    val_list.append(val)
                str_list.append("".join(val_list))
            return " ".join(str_list).strip()
        except:
            print('string contains invalid characters.')

    def check_city(city_string):
        if city_string.isalpha():
            city_string = detect_city(city_string)
            return city_string
        elif city_string.isalnum():
            return print('city contains string characters and digits.')
        else:
            return print('new data structure please add.')