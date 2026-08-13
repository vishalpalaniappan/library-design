from computable_units import *
from registered import *
from WorldState import WorldState
from LoggingHelper import semanticLogger

def createBasket():
    worldStateManager.setBehavior('createBasket')
    worldStateManager.create('basket', [], 'BASKET', 'BOOK_BASKET', False)
    return 'acceptChoice'

def acceptChoice():
    worldStateManager.setBehavior('acceptChoice')
    choice = input('\nGet user choice (a for add book, g for get book, d for display, else exit): ')
    worldStateManager.create('choice', choice, 'CHOICE', 'USER_CHOICE', True)
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
    position_str = input('\nPlease enter position to get from basket: ')
    worldStateManager.create('position_str', position_str, 'POSITION', 'BASKET_POSITION_STR', True)
    return 'convertToNumber'

def convertToNumber():
    worldStateManager.setBehavior('convertToNumber')
    position_str = worldStateManager.getValue('position_str', 'POSITION', 'BASKET_POSITION_STR')
    position = convertStrToNumber(position_str)
    worldStateManager.create('position', position, 'POSITION', 'BASKET_POSITION', False)
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
    return 'createBook'

def createBook():
    worldStateManager.setBehavior('createBook')
    name = worldStateManager.getValue('name', 'NAME', 'BOOK_W_NAME')
    book = {}
    book['name'] = name
    worldStateManager.create('book', book, 'BOOK', 'BOOK_W_NAME', False)
    worldStateManager.remove('name')
    return 'addBookToBasket'

def addBookToBasket():
    worldStateManager.setBehavior('addBookToBasket')
    book = worldStateManager.get('book', 'BOOK', 'BOOK_W_NAME')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    basket = insertIntoList(basket, 0, book)
    worldStateManager.update('basket', basket, 'BASKET', 'BOOK_BASKET')
    worldStateManager.remove('book')
    return 'acceptChoice'

def showBasket():
    worldStateManager.setBehavior('showBasket')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    print(f'Basket Contents: {basket}')
    return 'acceptChoice'
if __name__ == '__main__':
    worldStateManager = WorldState('minimal')
    nextBehavior = 'createBasket'
    worldState = {}
    while nextBehavior:
        try:
            nextBehavior = globals()[nextBehavior]()
        except Exception as e:
            worldStateManager.setFailure()
            raise e