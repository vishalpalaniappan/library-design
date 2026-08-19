from computable_units import *

def callIfExist(method_name, *args, **kwargs):
    method = globals().get(method_name)

    if callable(method):
        return method(*args, **kwargs)
    else:
        return None