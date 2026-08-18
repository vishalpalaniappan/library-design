from createAndAddBook import *
from computable_units import *
from registered import *
from WorldState import worldStateManager
from LoggingHelper import semanticLogger

def initWorldState():
    worldStateManager.setBehavior('initWorldState')
    worldStateManager.create('basket', [], 'BASKET', 'BOOK_BASKET', False)
    worldStateManager.create('choice_prompt', '\nGet user choice (a for add book, g for get book, d for display, else exit): ', 'STRING', 'CHOICE_PROMPT', False)
    worldStateManager.create('book_name_prompt', '\nPlease enter book name: ', 'STRING', 'BOOK_NAME_PROMPT', False)
    worldStateManager.create('basket_position_prompt', '\nPlease enter position to get from basket: ', 'STRING', 'BASKET_POSITION_PROMPT', False)
    return 'acceptChoice'

def acceptChoice():
    worldStateManager.setBehavior('acceptChoice')
    choice_prompt = worldStateManager.getValue('choice_prompt', 'STRING', 'CHOICE_PROMPT')
    choice = getInput(choice_prompt)
    worldStateManager.create('choice', choice, 'CHOICE', 'USER_CHOICE', True)
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
    printFormattedString(f"Got book named {name} and it has first letter {firstLetter}")
    worldStateManager.remove('book')
    return 'acceptChoice'

def getName():
    worldStateManager.setBehavior('getName')
    name = getInput('\nPlease enter book name: ')
    worldStateManager.create('name', name, 'NAME', 'BOOK_NAME', True)
    return 'addBook'

def addBook():
    worldStateManager.setBehavior('addBook')
    createAndAddBook()
    return 'acceptChoice'

def showBasket():
    worldStateManager.setBehavior('showBasket')
    basket = worldStateManager.getValue('basket', 'BASKET', 'BOOK_BASKET')
    printFormattedString(f"Basket Contents: {basket}")
    return 'acceptChoice'
if __name__ == '__main__':
    nextBehavior = 'initWorldState'
    worldState = {}
    while nextBehavior:
        try:
            nextBehavior = globals()[nextBehavior]()
        except Exception as e:
            worldStateManager.setFailure()
            raise e