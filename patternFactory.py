from addrPatterns import addrpattern1, addrpattern2, addrpattern3, addrpattern4

class addrpatternfactory():
    def __init__(self, address):
        self._address = address

    def get_addr(self):
        return addrpattern1(self._address)

    def fix_address(self):
        # if self._address.contains(',  '):
        #     self._address = self._address.replace(',  ', ',')
        #
        # if self._address.contains('  '):
        #     self._address = self._address.replace('  ', ' ')

        if self._address.count(',') == 3:
            print('Address Pattern 1 - splitting into four elems => ')
            # try:
            #     return addrpattern1(self._address)
            # except:
            #     return addrpattern4(self._address)
            return addrpattern1(self._address)

        # if self._address.count(', ') == 3:
        #     print('Address Pattern 4 - splitting into four elems => ')
        #     return addrpattern4(self._address)

        if self._address.count(',') == 1:
            print('Address Pattern 2 - splitting into two elems => ')
            return addrpattern2(self._address)

        if self._address.count(',') == 2:
            print('Address Pattern 3 - splitting into three elems')
            return addrpattern3(self._address)


