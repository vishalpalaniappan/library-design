from computable_units import *
from registered import *
from WorldState import WorldState
from LoggingHelper import semanticLogger

def createBasket():
    worldStateManager.setBehavior('createBasket')
    basket = []
    worldStateManager.create('basket', basket, 'BASKET', 'BOOK_BASKET', False)
    basket = worldStateManager.getValue('basket', '', '')
    inv_result = getFromPosition_invariant_1(basket)
    print(f'Invariant (pos 1 for basket in transformation_getFromPosition in behaviorgetBookFromBasket')
    print(f'Result (false is inv violation): {inv_result}')
    basket = worldStateManager.getValue('basket', '', '')
    inv_result = removeFromPosition_invariant_1(basket)
    print(f'Invariant (pos 1 for basket in transformation_removeFromPosition in behaviorgetBookFromBasket')
    print(f'Result (false is inv violation): {inv_result}')
    basket = worldStateManager.getValue('basket', '', '')
    inv_result = insertIntoList_invariant_1(basket)
    print(f'Invariant (pos 1 for basket in transformation_insertIntoList in behavioraddBookToBasket')
    print(f'Result (false is inv violation): {inv_result}')
    return 'getChoice'

def getChoice():
    worldStateManager.setBehavior('getChoice')
    choice = input('\nGet user choice (a for add book, g for get book, else exit): ')
    worldStateManager.create('choice', choice, 'CHOICE', 'USER_CHOICE', True)
    choice = worldStateManager.getValue('choice', '', '')
    inv_result = isEqual_invariant_1(choice)
    print(f'Invariant (pos 1 for choice in transformation_isEqual in behaviorevaluateChoice')
    print(f'Result (false is inv violation): {inv_result}')
    choice = worldStateManager.getValue('choice', '', '')
    inv_result = isEqual_invariant_1(choice)
    print(f'Invariant (pos 1 for choice in transformation_isEqual in behaviorevaluateChoice')
    print(f'Result (false is inv violation): {inv_result}')
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
    return 'getBookFromBasket'

def getBookFromBasket():
    worldStateManager.setBehavior('getBookFromBasket')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    book = getFromPosition(basket, 0)
    removeFromPosition(basket, 0)
    worldStateManager.add('book', book, 'BOOK', 'BOOK_W_NAME', False)
    return 'getBookName'

def getBookName():
    worldStateManager.setBehavior('getBookName')
    book = worldStateManager.getValue('book', 'BOOK', 'BOOK_W_NAME')
    name = book['name']
    worldStateManager.add('name', name, 'NAME', 'BOOK_NAME', False)
    return 'getFirstLetterOfBookName'

def getFirstLetterOfBookName():
    worldStateManager.setBehavior('getFirstLetterOfBookName')
    name = worldStateManager.getValue('name', 'NAME', 'BOOK_NAME')
    firstLetter = getFromPosition(name, 0)
    print(f'Got book named {name} and it has first letter {firstLetter}')
    worldStateManager.remove('book')
    return 'getChoice'

def getName():
    worldStateManager.setBehavior('getName')
    name = input('\nPlease enter book name: ')
    worldStateManager.create('name', name, 'NAME', 'BOOK_NAME', True)
    name = worldStateManager.getValue('name', '', '')
    inv_result = getFromPosition_invariant_1(name)
    print(f'Invariant (pos 1 for name in transformation_getFromPosition in behaviorgetFirstLetterOfBookName')
    print(f'Result (false is inv violation): {inv_result}')
    return 'createBook'

def createBook():
    worldStateManager.setBehavior('createBook')
    name = worldStateManager.getValue('name', 'NAME', 'BOOK_W_NAME')
    book = {}
    book['name'] = name
    worldStateManager.create('book', book, 'BOOK', 'BOOK_W_NAME', False)
    worldStateManager.remove('name')
    book = worldStateManager.getValue('book', '', '')
    inv_result = insertIntoList_invariant_2(book)
    print(f'Invariant (pos 2 for book in transformation_insertIntoList in behavioraddBookToBasket')
    print(f'Result (false is inv violation): {inv_result}')
    return 'addBookToBasket'

def addBookToBasket():
    worldStateManager.setBehavior('addBookToBasket')
    book = worldStateManager.get('book', 'BOOK', 'BOOK_W_NAME')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    basket = insertIntoList(basket, book, 0)
    worldStateManager.update('basket', basket, 'BASKET', 'BOOK_BASKET')
    worldStateManager.remove('book')
    return 'showBasket'

def showBasket():
    worldStateManager.setBehavior('showBasket')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    print(f'Basket Contents: {basket}')
    return 'getChoice'
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