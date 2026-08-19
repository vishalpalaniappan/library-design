from computable_units import *
from registered import *
from WorldState import worldStateManager
from LoggingHelper import semanticLogger

def createBook():
    worldStateManager.setBehavior('createBook')
    name = worldStateManager.getValue('name', 'NAME', 'BOOK_W_NAME')
    book = setNestedValue({}, ['name'], name)
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

def createAndAddBook():
    nextBehavior = 'createBook'
    worldState = {}
    while nextBehavior:
        try:
            nextBehavior = globals()[nextBehavior]()
        except Exception as e:
            worldStateManager.setFailure()
            raise e