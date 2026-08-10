from computable_units import *
from registered import *
from WorldState import WorldState
from LoggingHelper import semanticLogger

def createBasket():
    worldStateManager.setBehavior('createBasket')
    global worldState
    if True:
        print(f'Invariant for transformation _insertIntoList in behavior addBookToBasket')
    if True:
        print(f'Invariant for transformation _removeFromPosition in behavior getBookFromBasket')
    if True:
        print(f'Invariant for transformation _getFromPosition in behavior getBookFromBasket')
    basket = []
    worldStateManager.create('basket', basket, 'BASKET', 'BOOK_BASKET', False)
    return 'getChoice'

def getChoice():
    worldStateManager.setBehavior('getChoice')
    global worldState
    if True:
        print(f'Invariant for transformation _isEqual in behavior evaluateChoice')
    if True:
        print(f'Invariant for transformation _isEqual in behavior evaluateChoice')
    choice = input('\nGet user choice (a for add book, g for get book, else exit): ')
    worldStateManager.create('choice', choice, 'CHOICE', 'USER_CHOICE', True)
    return 'displayChoice'

def displayChoice():
    worldStateManager.setBehavior('displayChoice')
    global worldState
    choice = worldStateManager.getValue('choice', 'CHOICE', 'USER_CHOICE')
    print(f'User Choice: {choice}')
    return 'evaluateChoice'

def evaluateChoice():
    worldStateManager.setBehavior('evaluateChoice')
    global worldState
    choice = worldStateManager.getValue('choice', 'CHOICE', 'USER_CHOICE')
    isAdd = isEqual(choice, 'a')
    isGet = isEqual(choice, 'g')
    if isAdd:
        return 'addBookChoice'
    if isGet:
        return 'getBookChoice'

def addBookChoice():
    worldStateManager.setBehavior('addBookChoice')
    global worldState
    return 'getName'

def getBookChoice():
    worldStateManager.setBehavior('getBookChoice')
    global worldState
    return 'getBookFromBasket'

def getBookFromBasket():
    worldStateManager.setBehavior('getBookFromBasket')
    global worldState
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    book = getFromPosition(basket, 0)
    removeFromPosition(basket, 0)
    worldStateManager.add('book', book, 'BOOK', 'BOOK_W_NAME', False)
    return 'getBookName'

def getBookName():
    worldStateManager.setBehavior('getBookName')
    global worldState
    book = worldStateManager.getValue('book', 'BOOK', 'BOOK_W_NAME')
    name = book['name']
    worldStateManager.add('name', name, 'NAME', 'BOOK_NAME', False)
    return 'getFirstLetterOfBookName'

def getFirstLetterOfBookName():
    worldStateManager.setBehavior('getFirstLetterOfBookName')
    global worldState
    name = worldStateManager.getValue('name', 'NAME', 'BOOK_NAME')
    firstLetter = getFromPosition(name, 0)
    print(f'Got book named {name} and it has first letter {firstLetter}')
    worldStateManager.remove('book')
    return 'getChoice'

def getName():
    worldStateManager.setBehavior('getName')
    global worldState
    if True:
        print(f'Invariant for transformation _getFromPosition in behavior getFirstLetterOfBookName')
    name = input('\nPlease enter book name: ')
    worldStateManager.create('name', name, 'NAME', 'BOOK_NAME', True)
    return 'createBook'

def createBook():
    worldStateManager.setBehavior('createBook')
    global worldState
    if True:
        print(f'Invariant for transformation _insertIntoList in behavior addBookToBasket')
    name = worldStateManager.getValue('name', 'NAME', 'BOOK_W_NAME')
    book = {}
    book['name'] = name
    worldStateManager.create('book', book, 'BOOK', 'BOOK_W_NAME', False)
    worldStateManager.remove('name')
    return 'addBookToBasket'

def addBookToBasket():
    worldStateManager.setBehavior('addBookToBasket')
    global worldState
    book = worldStateManager.get('book', 'BOOK', 'BOOK_W_NAME')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    basket = insertIntoList(basket, book, 0)
    worldStateManager.update('basket', basket, 'BASKET', 'BOOK_BASKET')
    worldStateManager.remove('book')
    return 'showBasket'

def showBasket():
    worldStateManager.setBehavior('showBasket')
    global worldState
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