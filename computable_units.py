def removeFromPosition(list_to_modify, position):
    '''
        Removes the entry at the given position
        and returns the updated list.
    '''
    list_to_modify.pop(position)
    return value

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
