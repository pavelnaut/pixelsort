import random
from .sorting import average

def sort_image(
        size,
        image_data,
        mask_data,
        intervals,
        randomness,
        sorting_function):
    sorted_pixels = []

    for y in range(size[1]):
        row = []
        x_min = 0
        for x_max in intervals[y] + [size[0]]:
            interval = []
            for x in range(x_min, x_max):
                if mask_data[x, y]:
                    interval.append(image_data[x, y])
            if random.random() < randomness / 100:
                row += interval
            else:
                row += sort_interval(interval, sorting_function)
            x_min = x_max
        sorted_pixels.append(row)
    return sorted_pixels

def average_image(
        size,
        image_data,
        mask_data,
        intervals,
        randomness,
        sorting_function):
    sorted_pixels = []

    for y in range(size[1]):
        row = []
        x_min = 0
        for x_max in intervals[y] + [size[0]]:
            interval = []
            for x in range(x_min, x_max):
                if mask_data[x, y]:
                    interval.append(image_data[x, y])
            if random.random() < randomness / 100:
                row += interval
            else:
                row += average_interval(interval, sorting_function)
            x_min = x_max
        sorted_pixels.append(row)
    return sorted_pixels


def sort_interval(interval, sorting_function):
    return [] if interval == [] else sorted(interval, key=sorting_function)


def average_interval(interval, sorting_function):
    if interval == []:
        return []
    average_pixel = average(interval, sorting_function)
    return [] if interval == [] else [average_pixel for _ in interval]
