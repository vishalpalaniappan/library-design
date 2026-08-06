from computable_units import *
from WorldState import WorldState
from LoggingHelper import semanticLogger

def createBasket():
    worldStateManager.setBehavior('createBasket')
    global worldState
    basket = []
    worldStateManager.add('basket', basket, False)
    return 'getChoice'

def getChoice():
    worldStateManager.setBehavior('getChoice')
    global worldState
    choice = input('\nGet user choice (a for add book, g for get book, else exit): ')
    worldStateManager.add('choice', choice, True)
    return 'evaluateChoice'

def evaluateChoice():
    worldStateManager.setBehavior('evaluateChoice')
    global worldState
    choice = worldStateManager.getValue('choice')
    isAdd = choice == 'a'
    isGet = choice == 'g'
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
    basket = worldStateManager.getValue('basket')
    book = getFromPosition(basket, 0)
    removeFromPosition(basket, 0)
    worldStateManager.add('book', book, False)
    return 'getFirstLetterOfBookName'

def getFirstLetterOfBookName():
    worldStateManager.setBehavior('getFirstLetterOfBookName')
    global worldState
    book = worldStateManager.getValue('book')
    name = book['name']
    firstLetter = name[0]
    print(f'Got book named {name} and it has first letter {firstLetter}')
    worldStateManager.add('firstLetter', firstLetter, False)
    worldStateManager.remove('firstLetter')
    worldStateManager.remove('book')
    return 'getChoice'

def displayChoice():
    worldStateManager.setBehavior('displayChoice')
    global worldState
    choice = worldStateManager.getValue('choice')
    print(f'User Choice: {choice}')
    return 'getChoice'

def getName():
    worldStateManager.setBehavior('getName')
    global worldState
    name = input('\nPlease enter book name: ')
    worldStateManager.add('name', name, True)
    return 'createBook'

def createBook():
    worldStateManager.setBehavior('createBook')
    global worldState
    name = worldStateManager.getValue('name')
    book = {}
    book['name'] = name
    worldStateManager.add('book', book, False)
    worldStateManager.remove('name')
    return 'addBookToBasket'

def addBookToBasket():
    worldStateManager.setBehavior('addBookToBasket')
    global worldState
    book = worldStateManager.get('book')
    basket = worldStateManager.getValue('basket')
    basket.insert(0, book)
    worldStateManager.update('basket', basket)
    worldStateManager.remove('book')
    return 'showBasket'

def showBasket():
    worldStateManager.setBehavior('showBasket')
    global worldState
    basket = worldStateManager.getValue('basket')
    print(f'Basket Contents: {basket}')
    return 'getChoice'
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