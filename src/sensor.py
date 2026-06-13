import random

BIN_HEIGHT = 30

def get_distance():
    return random.randint(2, 30)

def get_fill_percentage(distance):
    fill = ((BIN_HEIGHT - distance) / BIN_HEIGHT) * 100

    if fill < 0:
        fill = 0

    return round(fill, 2)