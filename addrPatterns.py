from createAddr import addr_singleton
from rejected_logger import Logger
import re
from cityFixer import check_city
from streetFixer import check_street_address
class addrpattern1():
    ''' addrpattern1 follows the pattern : e.g. street address, city, state, zipcode
     for example, 1020 Wall Street, New York, New York, 12345
     '''
    def __init__(self, addrString=None):
        self._addrString = addrString

    def show_addr(self):
        return self._addrString

    def fixing_addr(self):
        addrvalue = re.sub('\\s+', ' ', self._addrString)
        addr_list = addrvalue.split(',')
        # print(addr_list[3])
        if addr_list[3][addr_list[3].isnumeric()]:
            zipcode = addr_singleton(zipcode = addr_list[3].strip())
            # print('Detecting Zipcode: ',addr_list[3])
            if addr_list[2][addr_list[2].isalpha()]:
                statename = addr_singleton(statename = addr_list[2].strip())
                # if statename.statename != 'IL':
                #     critical_log_object = Logger('parsing_logs.log')
                #     critical_log_object.critical('CRITICAL', '[{0}] - Statename is not valid - [ {1} ]'.format(addrvalue, addr_list[2]))
                # print('Detecting Statename:', addr_list[2])
                if addr_list[1][addr_list[1].isalpha()]:
                    cityname = addr_singleton(cityname = addr_list[1].strip())
                    if check_city(city_string=addr_list[1]):

                    # print('Detecting Cityname:', addr_list[1])
                    if addr_list[0][addr_list[0].isalnum()]:
                        # print(addr_list[0])
                        street_address = addr_singleton(street_address = addr_list[0].strip())
                        addr_dict = {'street_address': street_address.street_address,
                                     'city': cityname.cityname,
                                     'state': statename.statename,
                                     'zipcode': zipcode.zipcode}
                        print(addr_dict)
                        return addr_dict

class addrpattern2():
    ''' addrpattern2 follows the pattern : e.g. street address, city and zipcode combind.
        for example, input_address: 1020 Wall Street, New York 12345
                    output_address: {'street_address': 1020 Wall Street,'city': New York, 'zip': 12345}
     '''
    def __init__(self, addrString=None):
        self._addrString = addrString

    def show_addr(self):
        return self._addrString

    def fixing_addr(self):
        addrvalue = re.sub('\\s+', ' ', self._addrString)
        addr_list = addrvalue.split(',')
        # print(addr_list)
        if not addr_list[1].isalpha():
            # print(addr_list[1])
            if not addr_list[0].isalpha():
                # print(addr_list[0])
                city_zip = addr_list[1].split(' ')
                # print(city_zip)
                if city_zip[city_zip[2].isdigit()]:
                    if city_zip[city_zip[1].isalpha()]:
                        if addr_list[0][addr_list[0].isalnum()]:
                            addr_dict = {
                                'street_address': addr_list[0].strip(),
                                'city': city_zip[1].strip(),
                                'zipcode': city_zip[2].strip()
                            }
                            print(addr_dict)
                            return addr_dict

class addrpattern3():
    ''' addrpattern3 follows the pattern: e.g. street_address, city, zipcode all separated by commas
    for example: input_address: 1020 Wall Street, New York, 12345
                output_address: { 'street_address': '1020 Wall Street', 'city': 'New York', 'zipcode:' 12345 }
    '''
    def __init__(self, addrString=None):
        self._addrString = addrString

    def show_addr(self):
        return self._addrString

    def fixing_addr(self):
        addrvalue = re.sub('\\s+', ' ', self._addrString)
        addr_list = addrvalue.split(',')
        try:
            arr_addr = []
            addr_list[2] = addr_list[2].lstrip()
            addr_list[2] = addr_list[2].rstrip()
            for record in addr_list[2].split(' '):
                record = record.split(' ')
                arr_addr.append(record)
            zipcode = arr_addr[1]
            state = arr_addr[0]
            if zipcode[0].isnumeric():
                print('Detecting zipcode as digit: ', zipcode[0])
                print('City: {}'.format(addr_list[1]))
                if check_city(city_string=addr_list[1]):
                    cityname = check_city(city_string=addr_list[1])
                    print('from check_city --> City: {}'.format(cityname))
                    if check_street_address(street_address=addr_list[0]):
                        street_address = check_street_address(street_address=addr_list[0])
                        print('from check_street_address --> street_address: {}'.format(street_address))
                        addr_dict = {
                            'street_address': street_address,
                            'city': cityname,
                            'zipcode': zipcode[0].strip(),
                            'state': state[0].strip()
                            }
                        print('Processed text: ',addr_dict)
                        return addr_dict
        except:
            print('Please add more patterns and look into data analysis phase. '.format(addr_list))

class addrpattern4():
    ''' addrpattern4 follows the pattern: e.g. street_address, city, zipcode all separated by commas
    for example: input_address: 1020 Wall Street,  New York, 12345
                output_address: { 'street_address': '1020 Wall Street', 'city': 'New York', 'zipcode:' 12345 }
    '''
    def __init__(self, addrString=None):
        self._addrString = addrString

    def show_addr(self):
        return self._addrString

    def fixing_addr(self):
        addrvalue = re.sub('\\s+', ' ', self._addrString)
        addr_list = addrvalue.split(', ')
        print(addr_list)
        try:
            addr_list[2] = addr_list[2].lstrip()
            addr_list[2] = addr_list[2].rstrip()
            zipcode = addr_list[2]
            print(zipcode)
            if zipcode.isnumeric():
                print('Detecting zipcode as digit: ', zipcode)
                print('City: {}'.format(addr_list[1]))
                if check_city(city_string=addr_list[1]):
                    cityname = check_city(city_string=addr_list[1])
                    print('from check_city --> City: {}'.format(cityname))
                    if check_street_address(street_address=addr_list[0]):
                        street_address = check_street_address(street_address=addr_list[0])
                        print('from check_street_address --> street_address: {}'.format(street_address))
                        addr_dict = {
                            'street_address': street_address,
                            'city': cityname,
                            'zipcode': zipcode.strip(),
                            'state': ''
                            }
                        print('Processed text: ',addr_dict)
                        return addr_dict
        except:
            print('Please add more patterns and look into data analysis phase. '.format(addr_list))

class addrpattern5():
    ''' addrpattern5 follows the pattern: e.g. street_address, state zipcode
        for example: input_address: 1020 Wall Street,  New York 12345
                    output_address: { 'street_address': '1020 Wall Street', 'state': 'New York', 'zipcode:' 12345 }
        '''
    def __init__(self, addrString=None):
        self._addrString = addrString

    def show_addr(self):
        return self._addrString

    def fixing_addr(self):
        addrvalue = re.sub('\\s+', ' ', self._addrString)
        addr_list = addrvalue.split(', ')
        print(addr_list)
        try:
            if addr_list[1].isnumeric():
                zipcode = addr_list[1].strip()
                street_address = addr_list[0].strip()
                print(zipcode,street_address)
            else:
                state_zipcode_list = addr_list[1].split(' ')
                print(state_zipcode_list)
        except:
            print('Please add more patterns and look into data analysis phase. '.format(addr_list))
        # try:
        #     addr_list[1] = addr_list[2].lstrip()
        #     addr_list[1] = addr_list[2].rstrip()
        #     state_zipcode = addr_list[1]
        #     print(state_zipcode)
        #     if state_zipcode.isnumeric():
        #         print('Detecting zipcode as digit: ', state_zipcode)
        #         print('City: {}'.format(addr_list[1]))
        #         if check_city(city_string=addr_list[1]):
        #             cityname = check_city(city_string=addr_list[1])
        #             print('from check_city --> City: {}'.format(cityname))
        #             if check_street_address(street_address=addr_list[0]):
        #                 street_address = check_street_address(street_address=addr_list[0])
        #                 print('from check_street_address --> street_address: {}'.format(street_address))
        #                 addr_dict = {
        #                     'street_address': street_address,
        #                     'city': cityname,
        #                     'zipcode': zipcode.strip(),
        #                     'state': ''
        #                     }
        #                 print('Processed text: ',addr_dict)
        #                 return addr_dict
        # except:
        #     print('Please add more patterns and look into data analysis phase. '.format(addr_list))

        # if not addr_list[1].isalpha():
        #     # print(addr_list[1])
        #     if not addr_list[0].isalpha():
        #         # print(addr_list[0])
        #         city_zip = addr_list[1].split(' ')
        #         # print(city_zip)
        #         if city_zip[city_zip[2].isdigit()]:
        #             if city_zip[city_zip[1].isalpha()]:
        #                 if addr_list[0][addr_list[0].isalnum()]:
        #                     addr_dict = {
        #                         'street_address': addr_list[0].strip(),
        #                         'city': city_zip[1].strip(),
        #                         'zipcode': city_zip[2].strip()}
        #                     print(addr_dict)
        #                     return addr_dict
