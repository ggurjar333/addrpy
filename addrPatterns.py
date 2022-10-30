from createAddr import addr_singleton
from rejected_logger import Logger
import re
from cityFixer import cityFixer
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
                if statename.statename != 'IL':
                    critical_log_object = Logger('parsing_logs.log')
                    critical_log_object.critical('CRITICAL', '[{0}] - Statename is not valid - [ {1} ]'.format(addrvalue, addr_list[2]))
                # print('Detecting Statename:', addr_list[2])
                if addr_list[1][addr_list[1].isalpha()]:
                    cityname = addr_singleton(cityname = addr_list[1].strip())
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

# City goes well with the following chunk of code here.
#     def fixing_addr(self):
#         addrvalue = re.sub('\\s+', ' ', self._addrString)
#         addr_list = addrvalue.split(',')
#         if addr_list[2][addr_list[2].isdigit()]:
#            if addr_list[1][addr_list[1].isalpha()]:
#                if addr_list[0][addr_list[0].isalnum()]:
#                     addr_dict = {
#                             'street_address': addr_list[0].strip(),
#                             'city': addr_list[1].strip(),
#                             'zipcode': addr_list[2].strip()
#                             }
#                     print(addr_dict)
#                     return addr_dict

# 26102022

    def fixing_addr(self):
        addrvalue = re.sub('\\s+', ' ', self._addrString)
        addr_list = addrvalue.split(',')
        try:
            arr_addr = []
            addr_list[2] = addr_list[2].lstrip()
            addr_list[2] = addr_list[2].rstrip()
            # print(addr_list[2])
            for record in addr_list[2].split(' '):
                record = record.split(' ')
                # print('--------------------')
                # print(record)
                arr_addr.append(record)
            zipcode = arr_addr[1]
            statename = arr_addr[0]
            # print(zipcode[0], statename[0])
            if zipcode[0].isnumeric():
                print('Detecting zipcode as digit: ', zipcode[0])
                print('City: {}'.format(addr_list[1]))
                if cityFixer(city=addr_list[1]):
                    city = cityFixer(city=addr_list[1])
                    print('from check_city --> City: {}'.format(city))
                    if addr_list[0].isalnum() == True:
                        print('Street Address: '.format(addr_list[0]))
                        addr_dict = {
                            'street_address': addr_list[0].strip(),
                            'city': city.strip(),
                            'zipcode': zipcode[0].strip(),
                            'statename': statename[0].strip()
                            }
                        print(addr_dict)
                        return addr_dict
        except:
            print('IN the except block.:------------- {}'.format(addr_list))
        #     for record in addr_list[2]:
        #         # record = record.split(' ')
        #         print(record)

            # if not addr_list[2].isdigit():
            #     ''' Iterate every row of the column values and split the values by a space. '''
            #     print('Detecting zipcode as non-digit: ', addr_list[2])
            #     if addr_list[1].isalpha():
            #         if addr_list[0].isalnum():
            #             split_zip = addr_list[2].split(' ')
            #             addr_dict = {
            #                      'street_address': addr_list[0].strip(),
            #                      'city': addr_list[1].strip(),
            #                     'zipcode': split_zip[1].strip()
            #                 }
            #             print(addr_dict)
            #             return addr_dict

# 22102022
#     def fixing_addr(self):
#         addrvalue = re.sub('\\s+','', self._addrString)
#         addr_list = addrvalue.split(',')
#         full_address = addr_singleton(street_address='', city='', state='', zipcode='' )
#         if addr_list[2][addr_list[2].isdigit()]:
#             try:
#                 zipcode = addr_list[2].split(' ')
#                 full_address = addr_singleton(state=zipcode[0], zipcode=zipcode[1])
#             except:
#                 zipcode = addr_list[2]
#                 full_address = addr_singleton(zipcode= zipcode)
#             if addr_list[1][addr_list[1].isalpha()]:
#                 city = addr_list[1]
#                 full_address = addr_singleton(city=city)
#                 if addr_list[0][addr_list[0].isalnum()]:
#                     street_address = addr_list[0]
#                     full_address = addr_singleton(street_address=street_address)
#                     return full_address

# 21102022
    # def fixing_addr(self):
    #     addrvalue = re.sub('\\s+', ' ', self._addrString)
    #     addr_list = addrvalue.split(',')
    #     if addr_list[2][addr_list[2].isnumeric()]:
    #         arr_zipcode = addr_singleton(zipcode = addr_list[2].strip())
    #     else:
    #         arr_zipcode = addr_list[2].split(' ')
    #         if len(arr_zipcode) == 2:
    #             arr_zipcode = addr_singleton(statename= arr_zipcode[0], zipcode= arr_zipcode[1])
    #
    #     if addr_list[1][addr_list[1].isalpha()]:
    #         if addr_list[0][addr_list[0].isalnum()]:
    #             print('length of arr_zipcode', len(arr_zipcode))
    #             if len(arr_zipcode) == 1:
    #                 addr_dict = {
    #                    'street_address': addr_list[0].strip(),
    #                     'city': addr_list[1].strip(),
    #                     'zipcode': arr_zipcode.zipcode.strip(),
    #                     'statename': ''
    #                 }
    #                 print(addr_dict)
    #                 return addr_dict
    #             else:
    #                 addr_dict = {
    #                     'street_address': addr_list[0].strip(),
    #                     'city': addr_list[1].strip(),
    #                     'zipcode': arr_zipcode.zipcode.strip(),
    #                     'statename': arr_zipcode.statename.strip()
    #                     }
    #                 print(addr_dict)
    #                 return addr_dict


        # if addr_list[2][addr_list[2].isdigit()]:
        #    print(addr_list[2])
        #    try:
        #        state_zip = addr_list[2].str.split(' '):

           # if addr_list[2].contains([addr_list[2].isdigit()]):
           #     print(addr_list[2])
           # if addr_list[1][addr_list[1].isalpha()]:
           #     if addr_list[0][addr_list[0].isalnum()]:
           #         # print(addr_list[0])
           #         addr_dict = {
           #             'street_address': addr_list[0].strip(),
           #             'city': addr_list[1].strip(),
           #             'zipcode': addr_list[2].strip()
           #         }
           #         print(addr_dict)
           #         return addr_dict



        # else:
        #     city_zip = addr_list[2].split(' ')

class addrpattern4():
    ''' addrpattern4 follows the pattern: e.g. street_address, city, zipcode all separated by commas
    for example: input_address: 1020 Wall Street,  New York 12345
                output_address: { 'street_address': '1020 Wall Street', 'city': 'New York', 'zipcode:' 12345 }
    '''
    def __init__(self, addrString=None):
        self._addrString = addrString

    def show_addr(self):
        return self._addrString

    def fixing_addr(self):
        addrvalue = re.sub('\\s+', ' ', self._addrString)
        addr_list = addrvalue.split(', ')
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
                                'zipcode': city_zip[2].strip()}
                            print(addr_dict)
                            return addr_dict
