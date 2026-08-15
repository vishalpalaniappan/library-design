from computable_units import *
from registered import *
from WorldState import WorldState
from LoggingHelper import semanticLogger

def initWorldState():
    worldStateManager.setBehavior('initWorldState')
    worldStateManager.create('basket', [], 'BASKET', 'BOOK_BASKET', False)
    worldStateManager.create('choice_prompt', '\nGet user choice (a for add book, g for get book, d for display, else exit): ', 'STRING', 'CHOICE_PROMPT', False)
    worldStateManager.create('book_name_prompt', '\nPlease enter book name: ', 'STRING', 'BOOK_NAME_PROMPT', False)
    worldStateManager.create('basket_position_prompt', '\nPlease enter position to get from basket: ', 'STRING', 'BASKET_POSITION_PROMPT', False)
    hasParticipants = worldStateManager.hasParticipants(['choice_prompt'])
    if hasParticipants:
        choice_prompt = worldStateManager.getValue('choice_prompt', '', '')
        invariantViolated = callIfExist('getInput_invariant_1', choice_prompt)
        if invariantViolated:
            print(f'Semantically invalid state: getInput_invariant_1 for choice_prompt in transformation _getInput in behavior acceptChoice')
            hasParticipants = worldStateManager.setInvariantViolation('getInput_invariant_1', 'choice_prompt', 'acceptChoice')
    hasParticipants = worldStateManager.hasParticipants(['basket'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        invariantViolated = callIfExist('getFromPosition_invariant_1', basket)
        if invariantViolated:
            print(f'Semantically invalid state: getFromPosition_invariant_1 for basket in transformation _getFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('getFromPosition_invariant_1', 'basket', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket', 'position'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        position = worldStateManager.getValue('position', '', '')
        invariantViolated = callIfExist('getFromPosition_invariant_1_2', basket, position)
        if invariantViolated:
            print(f'Semantically invalid state: getFromPosition_invariant_1_2 for basket,position in transformation _getFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('getFromPosition_invariant_1_2', 'basket,position', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        invariantViolated = callIfExist('removeFromPosition_invariant_1', basket)
        if invariantViolated:
            print(f'Semantically invalid state: removeFromPosition_invariant_1 for basket in transformation _removeFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('removeFromPosition_invariant_1', 'basket', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket', 'position'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        position = worldStateManager.getValue('position', '', '')
        invariantViolated = callIfExist('removeFromPosition_invariant_1_2', basket, position)
        if invariantViolated:
            print(f'Semantically invalid state: removeFromPosition_invariant_1_2 for basket,position in transformation _removeFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('removeFromPosition_invariant_1_2', 'basket,position', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        invariantViolated = callIfExist('insertIntoList_invariant_1', basket)
        if invariantViolated:
            print(f'Semantically invalid state: insertIntoList_invariant_1 for basket in transformation _insertIntoList in behavior addBookToBasket')
            hasParticipants = worldStateManager.setInvariantViolation('insertIntoList_invariant_1', 'basket', 'addBookToBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        invariantViolated = callIfExist('insertIntoList_invariant_1_2', basket, 0)
        if invariantViolated:
            print(f'Semantically invalid state: insertIntoList_invariant_1_2 for basket,0 in transformation _insertIntoList in behavior addBookToBasket')
            hasParticipants = worldStateManager.setInvariantViolation('insertIntoList_invariant_1_2', 'basket,0', 'addBookToBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket', 'book'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        book = worldStateManager.getValue('book', '', '')
        invariantViolated = callIfExist('insertIntoList_invariant_1_2_3', basket, 0, book)
        if invariantViolated:
            print(f'Semantically invalid state: insertIntoList_invariant_1_2_3 for basket,0,book in transformation _insertIntoList in behavior addBookToBasket')
            hasParticipants = worldStateManager.setInvariantViolation('insertIntoList_invariant_1_2_3', 'basket,0,book', 'addBookToBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket', 'book'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        book = worldStateManager.getValue('book', '', '')
        invariantViolated = callIfExist('insertIntoList_invariant_1_3', basket, book)
        if invariantViolated:
            print(f'Semantically invalid state: insertIntoList_invariant_1_3 for basket,book in transformation _insertIntoList in behavior addBookToBasket')
            hasParticipants = worldStateManager.setInvariantViolation('insertIntoList_invariant_1_3', 'basket,book', 'addBookToBasket')
    return 'acceptChoice'

def acceptChoice():
    worldStateManager.setBehavior('acceptChoice')
    choice_prompt = worldStateManager.getValue('choice_prompt', 'STRING', 'CHOICE_PROMPT')
    choice = getInput(choice_prompt)
    worldStateManager.create('choice', choice, 'CHOICE', 'USER_CHOICE', True)
    hasParticipants = worldStateManager.hasParticipants(['choice'])
    if hasParticipants:
        choice = worldStateManager.getValue('choice', '', '')
        invariantViolated = callIfExist('isEqual_invariant_1', choice)
        if invariantViolated:
            print(f'Semantically invalid state: isEqual_invariant_1 for choice in transformation _isEqual in behavior evaluateChoice')
            hasParticipants = worldStateManager.setInvariantViolation('isEqual_invariant_1', 'choice', 'evaluateChoice')
    hasParticipants = worldStateManager.hasParticipants(['choice'])
    if hasParticipants:
        choice = worldStateManager.getValue('choice', '', '')
        invariantViolated = callIfExist('isEqual_invariant_1_2', choice, 'a')
        if invariantViolated:
            print(f'Semantically invalid state: isEqual_invariant_1_2 for choice,a in transformation _isEqual in behavior evaluateChoice')
            hasParticipants = worldStateManager.setInvariantViolation('isEqual_invariant_1_2', 'choice,a', 'evaluateChoice')
    return 'displayChoice'

def displayChoice():
    worldStateManager.setBehavior('displayChoice')
    choice = worldStateManager.getValue('choice', 'CHOICE', 'USER_CHOICE')
    printFormattedString(f"User Choice: {choice}")
    return 'evaluateChoice'

def evaluateChoice():
    worldStateManager.setBehavior('evaluateChoice')
    choice = worldStateManager.getValue('choice', 'CHOICE', 'USER_CHOICE')
    isAdd = isEqual(choice, 'a')
    isGet = isEqual(choice, 'g')
    isDisplay = isEqual(choice, 'd')
    if isAdd:
        return 'addBookChoice'
    if isGet:
        return 'getBookChoice'
    if isDisplay:
        return 'displayBasketChoice'

def addBookChoice():
    worldStateManager.setBehavior('addBookChoice')
    return 'getName'

def getBookChoice():
    worldStateManager.setBehavior('getBookChoice')
    return 'acceptPosition'

def displayBasketChoice():
    worldStateManager.setBehavior('displayBasketChoice')
    return 'showBasket'

def acceptPosition():
    worldStateManager.setBehavior('acceptPosition')
    position_str = getInput('\nPlease enter position to get from basket: ')
    worldStateManager.create('position_str', position_str, 'POSITION', 'BASKET_POSITION_STR', True)
    hasParticipants = worldStateManager.hasParticipants(['position_str'])
    if hasParticipants:
        position_str = worldStateManager.getValue('position_str', '', '')
        invariantViolated = callIfExist('convertStrToNumber_invariant_1', position_str)
        if invariantViolated:
            print(f'Semantically invalid state: convertStrToNumber_invariant_1 for position_str in transformation _convertStrToNumber in behavior convertToNumber')
            hasParticipants = worldStateManager.setInvariantViolation('convertStrToNumber_invariant_1', 'position_str', 'convertToNumber')
    return 'convertToNumber'

def convertToNumber():
    worldStateManager.setBehavior('convertToNumber')
    position_str = worldStateManager.getValue('position_str', 'POSITION', 'BASKET_POSITION_STR')
    position = convertStrToNumber(position_str)
    worldStateManager.create('position', position, 'POSITION', 'BASKET_POSITION', False)
    hasParticipants = worldStateManager.hasParticipants(['basket', 'position'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        position = worldStateManager.getValue('position', '', '')
        invariantViolated = callIfExist('getFromPosition_invariant_1_2', basket, position)
        if invariantViolated:
            print(f'Semantically invalid state: getFromPosition_invariant_1_2 for basket,position in transformation _getFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('getFromPosition_invariant_1_2', 'basket,position', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['position'])
    if hasParticipants:
        position = worldStateManager.getValue('position', '', '')
        invariantViolated = callIfExist('getFromPosition_invariant_2', position)
        if invariantViolated:
            print(f'Semantically invalid state: getFromPosition_invariant_2 for position in transformation _getFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('getFromPosition_invariant_2', 'position', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket', 'position'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        position = worldStateManager.getValue('position', '', '')
        invariantViolated = callIfExist('removeFromPosition_invariant_1_2', basket, position)
        if invariantViolated:
            print(f'Semantically invalid state: removeFromPosition_invariant_1_2 for basket,position in transformation _removeFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('removeFromPosition_invariant_1_2', 'basket,position', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['position'])
    if hasParticipants:
        position = worldStateManager.getValue('position', '', '')
        invariantViolated = callIfExist('removeFromPosition_invariant_2', position)
        if invariantViolated:
            print(f'Semantically invalid state: removeFromPosition_invariant_2 for position in transformation _removeFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('removeFromPosition_invariant_2', 'position', 'getBookFromBasket')
    return 'getBookFromBasket'

def getBookFromBasket():
    worldStateManager.setBehavior('getBookFromBasket')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    position = worldStateManager.getValue('position', 'POSITION', 'BASKET_POSITION')
    book = getFromPosition(basket, position)
    removeFromPosition(basket, position)
    worldStateManager.add('book', book, 'BOOK', 'BOOK_W_NAME', False)
    return 'getBookName'

def getBookName():
    worldStateManager.setBehavior('getBookName')
    book = worldStateManager.getValue('book', 'BOOK', 'BOOK_W_NAME')
    name = getNestedValue(book, ['name'])
    worldStateManager.add('name', name, 'NAME', 'BOOK_NAME', False)
    return 'getFirstLetterOfBookName'

def getFirstLetterOfBookName():
    worldStateManager.setBehavior('getFirstLetterOfBookName')
    name = worldStateManager.getValue('name', 'NAME', 'BOOK_NAME')
    firstLetter = getFirstCharacter(name)
    printFormattedString(f"Got book named {name} and it has first letter {firstLetter}")
    worldStateManager.remove('book')
    return 'acceptChoice'

def getName():
    worldStateManager.setBehavior('getName')
    name = getInput('\nPlease enter book name: ')
    worldStateManager.create('name', name, 'NAME', 'BOOK_NAME', True)
    hasParticipants = worldStateManager.hasParticipants(['name'])
    if hasParticipants:
        name = worldStateManager.getValue('name', '', '')
        invariantViolated = callIfExist('getFirstCharacter_invariant_1', name)
        if invariantViolated:
            print(f'Semantically invalid state: getFirstCharacter_invariant_1 for name in transformation _getFirstCharacter in behavior getFirstLetterOfBookName')
            hasParticipants = worldStateManager.setInvariantViolation('getFirstCharacter_invariant_1', 'name', 'getFirstLetterOfBookName')
    return 'createBook'

def createBook():
    worldStateManager.setBehavior('createBook')
    name = worldStateManager.getValue('name', 'NAME', 'BOOK_W_NAME')
    book = setNestedValue({}, ['name'], name)
    worldStateManager.create('book', book, 'BOOK', 'BOOK_W_NAME', False)
    worldStateManager.remove('name')
    hasParticipants = worldStateManager.hasParticipants(['book'])
    if hasParticipants:
        book = worldStateManager.getValue('book', '', '')
        invariantViolated = callIfExist('getNestedValue_invariant_1', book)
        if invariantViolated:
            print(f'Semantically invalid state: getNestedValue_invariant_1 for book in transformation _getNestedValue in behavior getBookName')
            hasParticipants = worldStateManager.setInvariantViolation('getNestedValue_invariant_1', 'book', 'getBookName')
    hasParticipants = worldStateManager.hasParticipants(['book'])
    if hasParticipants:
        book = worldStateManager.getValue('book', '', '')
        invariantViolated = callIfExist('getNestedValue_invariant_1_2', book, ['name'])
        if invariantViolated:
            print(f'Semantically invalid state: getNestedValue_invariant_1_2 for book,name in transformation _getNestedValue in behavior getBookName')
            hasParticipants = worldStateManager.setInvariantViolation('getNestedValue_invariant_1_2', 'book,name', 'getBookName')
    hasParticipants = worldStateManager.hasParticipants(['basket', 'book'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        book = worldStateManager.getValue('book', '', '')
        invariantViolated = callIfExist('insertIntoList_invariant_1_2_3', basket, 0, book)
        if invariantViolated:
            print(f'Semantically invalid state: insertIntoList_invariant_1_2_3 for basket,0,book in transformation _insertIntoList in behavior addBookToBasket')
            hasParticipants = worldStateManager.setInvariantViolation('insertIntoList_invariant_1_2_3', 'basket,0,book', 'addBookToBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket', 'book'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        book = worldStateManager.getValue('book', '', '')
        invariantViolated = callIfExist('insertIntoList_invariant_1_3', basket, book)
        if invariantViolated:
            print(f'Semantically invalid state: insertIntoList_invariant_1_3 for basket,book in transformation _insertIntoList in behavior addBookToBasket')
            hasParticipants = worldStateManager.setInvariantViolation('insertIntoList_invariant_1_3', 'basket,book', 'addBookToBasket')
    hasParticipants = worldStateManager.hasParticipants(['book'])
    if hasParticipants:
        book = worldStateManager.getValue('book', '', '')
        invariantViolated = callIfExist('insertIntoList_invariant_2_3', 0, book)
        if invariantViolated:
            print(f'Semantically invalid state: insertIntoList_invariant_2_3 for 0,book in transformation _insertIntoList in behavior addBookToBasket')
            hasParticipants = worldStateManager.setInvariantViolation('insertIntoList_invariant_2_3', '0,book', 'addBookToBasket')
    hasParticipants = worldStateManager.hasParticipants(['book'])
    if hasParticipants:
        book = worldStateManager.getValue('book', '', '')
        invariantViolated = callIfExist('insertIntoList_invariant_3', book)
        if invariantViolated:
            print(f'Semantically invalid state: insertIntoList_invariant_3 for book in transformation _insertIntoList in behavior addBookToBasket')
            hasParticipants = worldStateManager.setInvariantViolation('insertIntoList_invariant_3', 'book', 'addBookToBasket')
    return 'addBookToBasket'

def addBookToBasket():
    worldStateManager.setBehavior('addBookToBasket')
    book = worldStateManager.get('book', 'BOOK', 'BOOK_W_NAME')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    basket = insertIntoList(basket, 0, book)
    worldStateManager.update('basket', basket, 'BASKET', 'BOOK_BASKET')
    worldStateManager.remove('book')
    hasParticipants = worldStateManager.hasParticipants(['basket'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        invariantViolated = callIfExist('getFromPosition_invariant_1', basket)
        if invariantViolated:
            print(f'Semantically invalid state: getFromPosition_invariant_1 for basket in transformation _getFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('getFromPosition_invariant_1', 'basket', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket', 'position'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        position = worldStateManager.getValue('position', '', '')
        invariantViolated = callIfExist('getFromPosition_invariant_1_2', basket, position)
        if invariantViolated:
            print(f'Semantically invalid state: getFromPosition_invariant_1_2 for basket,position in transformation _getFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('getFromPosition_invariant_1_2', 'basket,position', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        invariantViolated = callIfExist('removeFromPosition_invariant_1', basket)
        if invariantViolated:
            print(f'Semantically invalid state: removeFromPosition_invariant_1 for basket in transformation _removeFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('removeFromPosition_invariant_1', 'basket', 'getBookFromBasket')
    hasParticipants = worldStateManager.hasParticipants(['basket', 'position'])
    if hasParticipants:
        basket = worldStateManager.getValue('basket', '', '')
        position = worldStateManager.getValue('position', '', '')
        invariantViolated = callIfExist('removeFromPosition_invariant_1_2', basket, position)
        if invariantViolated:
            print(f'Semantically invalid state: removeFromPosition_invariant_1_2 for basket,position in transformation _removeFromPosition in behavior getBookFromBasket')
            hasParticipants = worldStateManager.setInvariantViolation('removeFromPosition_invariant_1_2', 'basket,position', 'getBookFromBasket')
    return 'acceptChoice'

def showBasket():
    worldStateManager.setBehavior('showBasket')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    printFormattedString(f"Basket Contents: {basket}")
    return 'acceptChoice'
if __name__ == '__main__':
    worldStateManager = WorldState('verbose')
    nextBehavior = 'initWorldState'
    worldState = {}
    while nextBehavior:
        try:
            nextBehavior = globals()[nextBehavior]()
        except Exception as e:
            worldStateManager.setFailure()
            raise e