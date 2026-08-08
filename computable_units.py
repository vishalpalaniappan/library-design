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
        TODO: Update invariants so that the invariant that
        is evaluated is for the chosen participant. Currently,
        it will not be possible to know which participant 
        caused the semantically invalid state because I am evaluating
        all of them at the same time.
        
        The objective here is to prevent semantic invalidity, so the invariant should be placed when that can be determined
        unambiguously.

        Also, for the third invariant in this list, the value of
        both position and the list participant is needed to determine
        semantic invalidity. So the invariant should be placed when
        both of those have existing can cause the world to enter a semantically invalid state.

        The algorithm that identifies the provenance of the participants
        will determine where the invariants are placed. For the third 
        invariant, it will identify when the existence of both participants
        can cause the world to enter a semantically invalid state.
    '''
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

def insertIntoList(list_to_modify, value, position):
    '''
        Inserts the value at the given position
        and returns the updated list.
    '''
    list_to_modify.insert(position, value)
    return list_to_modify


def insertIntoList_invariant(list_to_modify, value, position):
    '''
        Invariants:
        - list_to_modify must be list
        - position must be int
        - position must be within insertion range
    '''
    return (
        isinstance(list_to_modify, list)
        and isinstance(position, int)
        and 0 <= position <= len(list_to_modify)
    )