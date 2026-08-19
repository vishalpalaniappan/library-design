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

def getFromPosition_invariant_1(type, list_to_access):
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

def getFromPosition_invariant_2(type, position):
    '''
        position must be int
    '''
    if type == "evaluate":
        return not isinstance(position, list)

    if type == "getInvalidValues":
        return [
            ["test"]
        ]

def getFromPosition_invariant_1_2(type, list_to_access, position):
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

def getLength_invariant_1(type, value):
    '''
        Invariants:
        - value must have a length
    '''
    if type == "evaluate":
        return not hasattr(value, '__len__')
    
    if type == "getInvalidValues":
        # Int doesn't have length attribute
        return [
            [
                1
            ]
        ]

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

def insertIntoList_invariant_1(type, list_to_modify):
    '''
        list_to_modify must be list
    '''
    if type == "evaluate":
        return not (isinstance(list_to_modify, list) and hasattr(list_to_modify, "__len__"))

    if type == "getInvalidValues":
        # Basket with single book and position is 9
        return [
            [
                "not a list"
            ]
        ]

def insertIntoList_invariant_2(type, position):
    '''
        position must be int
    '''
    if type == "evaluate":
        return not isinstance(position, list)

    if type == "getInvalidValues":
        return [
            ["test"]
        ]

def insertIntoList_invariant_1_2(type, list_to_modify, position):
    '''
        position must be within insertion range
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


def getNestedValue_invariant_1(type, obj):
    '''
        obj must support keyed/indexed access
    '''
    if type == "evaluate":
        return not isinstance(obj, (dict, list, tuple, str))

    if type == "getInvalidValues":
        # Int does not have keyed/indexed access
        return [
            [
                1
            ]
        ]


def getNestedValue_invariant_2(type, keys):
    '''
        keys must be a list/tuple of valid key/index types
    '''
    if type == "evaluate":
        return not (
            isinstance(keys, (list, tuple))
            and all(isinstance(key, (str, int)) for key in keys)
        )

    if type == "getInvalidValues":
        return [
            # keys is not a list/tuple
            [
                1
            ],

            # keys contains an invalid key type
            [
                [1.5]
            ]
        ]

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

def setNestedValue_invariant_1(type, obj):
    '''
        obj must support keyed/indexed access and assignment
    '''
    if type == "evaluate":
        return not isinstance(obj, (dict, list))

    if type == "getInvalidValues":
        return [
            # Does not support keyed/indexed access
            [
                1
            ],

            # Supports indexed access, but not assignment
            [
                (1, 2)
            ]
        ]

def setNestedValue_invariant_2(type, keys):
    '''
        keys must be a non-empty list/tuple of valid key/index types
    '''
    if type == "evaluate":
        return not (
            isinstance(keys, (list, tuple))
            and len(keys) > 0
            and all(isinstance(key, (str, int)) for key in keys)
        )

    if type == "getInvalidValues":
        return [
            # keys is not a list/tuple
            [
                1
            ],

            # keys is empty
            [
                []
            ],

            # keys contains an invalid key type
            [
                [1.5]
            ]
        ]

#=====================================
#      Get First Character Of String
#=====================================
def getFirstCharacter(value):
    return value[0]


def getFirstCharacter_invariant_1(type, value):
    '''
        The value must be a string and its length
        has to be greater than 0.
    '''
    if type == "evaluate":
        return not (isinstance(value, str) and len(value) > 0)

    if type == "getInvalidValues":
        return [
            # value is not a string
            [
                1
            ],

            # value is an empty string
            [
                ""
            ]
        ]


#=====================================
#      Convert String To Number
#=====================================
def convertStrToNumberInt(strValue):
    return int(strValue)

def convertStrToNumberInt_invariant_1(type, strValue):
    '''
        It has to be a string and it has to represent
        a valid whole number.
    '''
    if type == "evaluate":
        return not (
            isinstance(strValue, str)
            and len(strValue) > 0
            and strValue.isdigit()
        )

    if type == "getInvalidValues":
        return [
            # value is not a string
            [
                1
            ],

            # string does not represent a whole number
            [
                "1.5"
            ],

            # string is empty
            [
                ""
            ]
        ]

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