from addrPatterns import addrpattern1, addrpattern2, addrpattern3, addrpattern4, addrpattern5

class addrpatternfactory():
    def __init__(self, address):
        self._address = address

    def get_addr(self):
        return addrpattern1(self._address)

    def fix_address(self):
        if self._address.count(',') == 3:
            print('Address Pattern 1 - splitting into four elems => ')
            return addrpattern1(self._address)

        try:
            if self._address.count(',') == 2:
                print('Address Pattern 3 - splitting into three elems')
                print('new things: ')
                if addrpattern3(self._address).fixing_addr().values() != []:
                    return addrpattern3(self._address)
        except:
            if self._address.count(',') == 2:
                print('Address Pattern 4 - splitting into three elems')
                return addrpattern4(self._address)


        try:
            if self._address.count(',') == 1:
                print('Address Pattern 2 - splitting into two elems => ')
                if addrpattern2(self._address).fixing_addr().values != []:
                    return addrpattern2(self._address)
        except:
            if self._address.count(',') == 1:
                print('Address Pattern 5 - splitting into two elems => ')
                return addrpattern5(self._address)



