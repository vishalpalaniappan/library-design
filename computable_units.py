#==================================
#   Remove From Position
#==================================
def removeFromPosition(list_to_modify, position):
    '''
        Remove entry at position and return updated list.
    '''
    list_to_modify.pop(position)
    return list_to_modify

def removeFromPosition_invariant_1(type, list_to_modify):
    '''
        list_to_modify must be list
    '''
    if type == "evaluate":
        return not (isinstance(list_to_modify, list) and hasattr(list_to_modify, "__len__"))

    
    if type == "getInvalidValues":
        # List of invalid values
        # Each entry is a list with multiple args to the invariant
        # In this case, it is a single arg
        return [
            ["not a list"]
        ]

def removeFromPosition_invariant_2(type, position):
    '''
        position must be int
    '''
    if type == "evaluate":
        return not isinstance(position, list)

    if type == "getInvalidValues":
        return [
            ["test"]
        ]

def removeFromPosition_invariant_1_2(type, list_to_modify, position):
    '''
        position must be within range
    '''
    if type == "evaluate":
        return not (0 <= position < len(list_to_modify))

    if type == "getInvalidValues":
        # Basket with single book and position is 9
        return [
            [
                [{"name":"book"}], 9
            ]
        ]

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
    if type == "evaluate":
        return not (isinstance(list_to_access, list) and hasattr(list_to_access, "__len__"))

    if type == "getInvalidValues":
        # Basket with single book and position is 9
        return [
            [
                "not a list"
            ]
        ]

def getFromPosition_invariant_2(position):
    '''
        position must be int
    '''
    if type == "evaluate":
        return not isinstance(position, list)

    if type == "getInvalidValues":
        return [
            ["test"]
        ]

def getFromPosition_invariant_1_2(list_to_access, position):
    '''
        position must be within range
    '''
    if type == "evaluate":
        return not (0 <= position < len(list_to_access))

    if type == "getInvalidValues":
        # Basket with single book and position is 9
        return [
            [
                [{"name":"book"}], 9
            ]
        ]

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
#      Set Value In Object
#=====================================
def setNestedValue(obj, keys, value):
    '''
        Sets value at the given nested keys.
    '''
    nestedObj = obj

    for key in keys[:-1]:
        nestedObj = nestedObj[key]

    nestedObj[keys[-1]] = value
    return obj


def setNestedValue_invariant_1(obj):
    '''
        obj must support keyed/indexed access and assignment
    '''
    return not isinstance(obj, (dict, list))


def setNestedValue_invariant_2(keys):
    '''
        keys must be a non-empty list/tuple of valid key/index types
    '''
    return not (
        isinstance(keys, (list, tuple))
        and len(keys) > 0
        and all(isinstance(key, (str, int)) for key in keys)
    )

#=====================================
#      Get First Character Of String
#=====================================
def getFirstCharacter(value):
    return value[0]


def getFirstCharacter_invariant_1(value):
    '''
        The value must be a string and its length
        has to be greater than 0.
    '''
    return not (isinstance(value, str) and len(value) > 0)


#=====================================
#      Convert String To Number
#=====================================
def convertStrToNumber(strValue):
    return int(strValue)

def convertStrToNumber_invariant_1(strValue):
    '''
        It has to be a string and it has to represent
        a valid whole number.

        This can be extended to include float values as
        well.
    '''
    return not (isinstance(strValue, str) and strValue.isdigit())

#=====================================
#      Get Input From Terminal
#=====================================
def getInput(strValue):
    '''
        TODO: 
        The design of input says that EOF error
        is possible if the environment doesn't
        terminate the input properly.

        I would have to catch that error and then
        it would become included in the semantics
        and it would modify the behavior of the
        design to continue realizing its intentions.

        If I was working with the design of input
        directly, through shared meaning, it could
        tell me that EOF occured. This would then
        have an unambiguous meaning in my design and
        my behavior would act accoringly.

        Since I am using an opaque transformation, I
        have to introduce the valid state into the
        world and my behvior has to act accordingly.

        If getInput was a composite behavior, it would
        operate on the world state directly, so the
        necessary semantics would already be available
        and my behavior would have to act accordingly.
    '''
    return input(strValue)

#=====================================
#      Display
#=====================================
def printFormattedString(formatted_string):
    return print(formatted_string)

def printFormattedString_invariant_1(formatted_string):
    return not isinstance(formatted_string, str)