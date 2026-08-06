def removeFromPosition(list_to_modify, position):
    '''
        Removes the entry at the given position
        and returns the updated list.
    '''
    list_to_modify.pop(position)
    return list_to_modify

def removeFromPosition_invariant(list_to_modify, position):
    '''
        Invariants:
        - list_to_modify must be list
        - position must be int
        - position must be within range
    '''
    return (
        isinstance(list_to_modify, list)
        and isinstance(position, int)
        and 0 <= position < len(list_to_modify)
    )

def getFromPosition(list_to_access, position):
    '''
        Gets the entry at the given position.
    '''
    return list_to_access[position]


def getFromPosition_invariant(list_to_access, position):
    '''
        Invariants:
        - list_to_access must be list
        - position must be int
        - position must be within range
    '''
    return (
        isinstance(list_to_access, list)
        and isinstance(position, int)
        and 0 <= position < len(list_to_access)
    )


def isEqual(a, b):
    return a == b


def isEqual_invariant(a, b):
    '''
        Invariants:
        - None
    '''
    return True


def getLength(value):
    return len(value)


def getLength_invariant(value):
    '''
        Invariants:
        - value must have a length
    '''
    return hasattr(value, '__len__')