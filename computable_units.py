#==================================
#   Remove From Position
#==================================
def removeFromPosition(list_to_modify, position):
    '''
        Remove entry at position and return updated list.
    '''
    list_to_modify.pop(position)
    return list_to_modify

def removeFromPosition_invariant_1(list_to_modify):
    '''
        list_to_modify must be list
    '''
    return not isinstance(list_to_modify, list)

def removeFromPosition_invariant_2( position):
    '''
        position must be int
    '''
    return not isinstance(position, int)

def removeFromPosition_invariant_1_2(list_to_modify, position):
    '''
        position must be within range
    '''
    return not (0 <= position < len(list_to_modify))

#==================================
#   Remove From Position
#==================================
def getFromPosition(list_to_access, position):
    '''
        Gets the entry at the given position.
    '''
    return list_to_access[position]

def getFromPosition_invariant_1(list_to_access):
    '''
        list_to_access must be list
    '''
    return not hasattr(list_to_access, "__len__")

def getFromPosition_invariant_2(position):
    '''
        position must be int
    '''
    return not isinstance(position, int)

def getFromPosition_invariant_1_2(position, list_to_access):
    '''
        position must be within range
    '''
    return not (0 <= position < len(list_to_access))

#==================================
#   Is Equal
#==================================
def isEqual(a, b):
    return a == b

#==================================
#   Get Length
#==================================
def getLength(value):
    return len(value)

def getLength_invariant_1(value):
    '''
        Invariants:
        - value must have a length
    '''
    return not hasattr(value, '__len__')

#==================================
#   Insert Into List
#==================================
def insertIntoList(list_to_modify, position, value):
    '''
        Inserts the value at the given position
        and returns the updated list.
    '''
    list_to_modify.insert(position, value)
    return list_to_modify

def insertIntoList_invariant_1(list_to_modify):
    '''
        list_to_modify must be list
    '''
    return not hasattr(list_to_modify, "__len__")

def insertIntoList_invariant_2(position):
    '''
        position must be int
    '''
    return not isinstance(position, int)

def insertIntoList_invariant_1_2(list_to_modify, position):
    '''
        position must be within insertion range
    '''
    return not (0 <= position <= len(list_to_modify))

#=====================================
#      Get Value From Object
#=====================================
def getNestedValue(obj, keys):
    '''
        Returns value that given keys.
    '''
    value = obj

    for key in keys:
        value = value[key]

    return value


def getNestedValue_invariant_1(obj):
    '''
        obj must support keyed/indexed access
    '''
    return not isinstance(obj, (dict, list, tuple, str))


def getNestedValue_invariant_2(keys):
    '''
        keys must be a list/tuple of valid key/index types
    '''
    return not (
        isinstance(keys, (list, tuple))
        and all(isinstance(key, (str, int)) for key in keys)
    )


#=====================================
#      Convert String To Number
#=====================================
def convertStrToNumber(strValue):
    return int(strValue)