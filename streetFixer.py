class streetAddr:
    _streetAddr = {}
    def __init__(self):
        self.__str__ = self._streetAddr


def check_street_address(param):
    pass


class streetAddress(streetAddr):
    def __init__(self, **kwargs):
        streetAddr.__init__(self)
        self._streetAddr = check_street_address(kwargs['streetAddress'])