from common import has_numbers


def check_state(state):
    try:
        split_val = state.split(' ')
        str_list = []
        for val in split_val:
            val_list = []
            val_list.append(val)
            if val.isalpha():
                val_list.append(val)
            str_list.append("".join(val_list))
        return " ".join(str_list).strip()
    except:
        print('state contains invalid characters.')


class state:
    _state = {}

    def __init__(self):
        self.__str__ = self._state


class streetAddress(state):
    def __init__(self, **kwargs):
        state.__init__(self)
        self._state = check_state(kwargs['state'])
