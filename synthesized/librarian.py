from computable_units import *
from registered import *
from WorldState import WorldState
from LoggingHelper import semanticLogger

def createBasket():
    worldStateManager.setBehavior('createBasket')
    worldStateManager.create('basket', [], 'BASKET', 'BOOK_BASKET', False)
    basket = worldStateManager.getValue('basket', '', '')
    inv_result = callIfExist('getFromPosition_invariant_1', basket)
    if inv_result:
        print(f'Invariant Violation: getFromPosition_invariant_1 for basket in transformation _getFromPosition in behavior getBookFromBasket')
    basket = worldStateManager.getValue('basket', '', '')
    inv_result = callIfExist('removeFromPosition_invariant_1', basket)
    if inv_result:
        print(f'Invariant Violation: removeFromPosition_invariant_1 for basket in transformation _removeFromPosition in behavior getBookFromBasket')
    basket = worldStateManager.getValue('basket', '', '')
    inv_result = callIfExist('insertIntoList_invariant_1', basket)
    if inv_result:
        print(f'Invariant Violation: insertIntoList_invariant_1 for basket in transformation _insertIntoList in behavior addBookToBasket')
    return 'acceptChoice'

def acceptChoice():
    worldStateManager.setBehavior('acceptChoice')
    choice = input('\nGet user choice (a for add book, g for get book, else exit): ')
    worldStateManager.create('choice', choice, 'CHOICE', 'USER_CHOICE', True)
    choice = worldStateManager.getValue('choice', '', '')
    inv_result = callIfExist('isEqual_invariant_1', choice)
    if inv_result:
        print(f'Invariant Violation: isEqual_invariant_1 for choice in transformation _isEqual in behavior evaluateChoice')
    return 'displayChoice'

def displayChoice():
    worldStateManager.setBehavior('displayChoice')
    choice = worldStateManager.getValue('choice', 'CHOICE', 'USER_CHOICE')
    print(f'User Choice: {choice}')
    return 'evaluateChoice'

def evaluateChoice():
    worldStateManager.setBehavior('evaluateChoice')
    choice = worldStateManager.getValue('choice', 'CHOICE', 'USER_CHOICE')
    isAdd = isEqual(choice, 'a')
    isGet = isEqual(choice, 'g')
    if isAdd:
        return 'addBookChoice'
    if isGet:
        return 'getBookChoice'

def addBookChoice():
    worldStateManager.setBehavior('addBookChoice')
    return 'getName'

def getBookChoice():
    worldStateManager.setBehavior('getBookChoice')
    return 'acceptPosition'

def acceptPosition():
    worldStateManager.setBehavior('acceptPosition')
    position = input('\nPlease enter position to get from basket: ')
    worldStateManager.create('position', position, 'POSITION', 'BASKET_POSITION', True)
    position = worldStateManager.getValue('position', '', '')
    inv_result = callIfExist('convertStrToNumber_invariant_1', position)
    if inv_result:
        print(f'Invariant Violation: convertStrToNumber_invariant_1 for position in transformation _convertStrToNumber in behavior convertToNumber')
    return 'convertToNumber'

def convertToNumber():
    worldStateManager.setBehavior('convertToNumber')
    position = worldStateManager.getValue('position', 'POSITION', 'BASKET_POSITION')
    position = convertStrToNumber(position)
    worldStateManager.update('position', position, 'POSITION', 'BASKET_POSITION')
    position = worldStateManager.getValue('position', '', '')
    inv_result = callIfExist('getFromPosition_invariant_2', position)
    if inv_result:
        print(f'Invariant Violation: getFromPosition_invariant_2 for position in transformation _getFromPosition in behavior getBookFromBasket')
    position = worldStateManager.getValue('position', '', '')
    inv_result = callIfExist('removeFromPosition_invariant_2', position)
    if inv_result:
        print(f'Invariant Violation: removeFromPosition_invariant_2 for position in transformation _removeFromPosition in behavior getBookFromBasket')
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
    print(f'Got book named {name} and it has first letter {firstLetter}')
    worldStateManager.remove('book')
    return 'acceptChoice'

def getName():
    worldStateManager.setBehavior('getName')
    name = input('\nPlease enter book name: ')
    worldStateManager.create('name', name, 'NAME', 'BOOK_NAME', True)
    name = worldStateManager.getValue('name', '', '')
    inv_result = callIfExist('getFirstCharacter_invariant_1', name)
    if inv_result:
        print(f'Invariant Violation: getFirstCharacter_invariant_1 for name in transformation _getFirstCharacter in behavior getFirstLetterOfBookName')
    return 'createBook'

def createBook():
    worldStateManager.setBehavior('createBook')
    name = worldStateManager.getValue('name', 'NAME', 'BOOK_W_NAME')
    book = {}
    book['name'] = name
    worldStateManager.create('book', book, 'BOOK', 'BOOK_W_NAME', False)
    worldStateManager.remove('name')
    book = worldStateManager.getValue('book', '', '')
    inv_result = callIfExist('getNestedValue_invariant_1', book)
    if inv_result:
        print(f'Invariant Violation: getNestedValue_invariant_1 for book in transformation _getNestedValue in behavior getBookName')
    book = worldStateManager.getValue('book', '', '')
    inv_result = callIfExist('insertIntoList_invariant_3', book)
    if inv_result:
        print(f'Invariant Violation: insertIntoList_invariant_3 for book in transformation _insertIntoList in behavior addBookToBasket')
    return 'addBookToBasket'

def addBookToBasket():
    worldStateManager.setBehavior('addBookToBasket')
    book = worldStateManager.get('book', 'BOOK', 'BOOK_W_NAME')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    basket = insertIntoList(basket, 0, book)
    worldStateManager.update('basket', basket, 'BASKET', 'BOOK_BASKET')
    worldStateManager.remove('book')
    basket = worldStateManager.getValue('basket', '', '')
    inv_result = callIfExist('getFromPosition_invariant_1', basket)
    if inv_result:
        print(f'Invariant Violation: getFromPosition_invariant_1 for basket in transformation _getFromPosition in behavior getBookFromBasket')
    basket = worldStateManager.getValue('basket', '', '')
    inv_result = callIfExist('removeFromPosition_invariant_1', basket)
    if inv_result:
        print(f'Invariant Violation: removeFromPosition_invariant_1 for basket in transformation _removeFromPosition in behavior getBookFromBasket')
    return 'showBasket'

def showBasket():
    worldStateManager.setBehavior('showBasket')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    print(f'Basket Contents: {basket}')
    return 'acceptChoice'
if __name__ == '__main__':
    worldStateManager = WorldState('verbose')
    nextBehavior = 'createBasket'
    worldState = {}
    while nextBehavior:
        try:
            nextBehavior = globals()[nextBehavior]()
        except Exception as e:
            worldStateManager.setFailure()
            raise e