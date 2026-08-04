from WorldState import WorldState
from registered import *
from LoggingHelper import semanticLogger

def b_getName():
    worldStateManager.setBehavior('b_getName')
    global worldState
    name = getTerminalInput('Enter your name: ')
    worldState['name'] = name
    return 'b_sayHi'

def b_sayHi():
    worldStateManager.setBehavior('b_sayHi')
    global worldState
    name = worldState['name']
    print(f'Hello {name}')
    return 'test'

def test():
    worldStateManager.setBehavior('test')
    global worldState
    return 'b_getName'
if __name__ == '__main__':
    worldStateManager = WorldState('minimal')
    nextBehavior = 'b_getName'
    worldState = {}
    while nextBehavior:
        try:
            nextBehavior = globals()[nextBehavior]()
        except Exception as e:
            worldStateManager.setFailure()
            raise e