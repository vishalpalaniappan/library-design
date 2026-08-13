from computable_units import *

def callIfExist(method_name, *args, **kwargs):
    try:
        method = globals().get(method_name)

        if callable(method):
            return method(*args, **kwargs)
        else:
            return None
    except:
        # Not all participants were loaded into world state,
        # so the invariant doesn't apply.
        return None