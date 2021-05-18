import random
# get a random pattern for correct awnsers
def randGamePattern(size):
    pattern = [0] * size
    for i in range(size):
    # get a random pattern and return it
        pattern[i] += random.randrange(0,15)
    return  pattern
