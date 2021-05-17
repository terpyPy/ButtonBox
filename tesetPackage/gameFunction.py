import random
# get a random pattern for correct awnsers
def getRandomPatt():
    # get a random pattern and return it
    pattern = [random.randrange(0,15), random.randrange(0,15), random.randrange(0,15), random.randrange(0,15)]
    return  pattern
