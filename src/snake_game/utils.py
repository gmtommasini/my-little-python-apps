import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, SIZE


def random_position():
    """Return a tuple (X,Y)"""
    # This weird thing is done so the food will be placed in a "square" place,
    #  and not in some completely random position
    x = int( (SCREEN_WIDTH - SIZE )/(2 *SIZE) )
    y = int( (SCREEN_HEIGHT - SIZE )/(2*SIZE))
    print(x, y)
    return (random.randint(-x, x) * SIZE, random.randint(-y, y) * SIZE)