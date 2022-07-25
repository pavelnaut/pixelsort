import pixelsort.util as util


def lightness(pixel):
    return util.lightness(pixel)


def intensity(pixel):
    return pixel[0] + pixel[1] + pixel[2]

def red(pixel):
    return pixel[0]

def green(pixel):
    return pixel[1]

def blue(pixel):
    return pixel[2]

def hue(pixel):
    return util.hue(pixel)


def saturation(pixel):
    return util.saturation(pixel)


def minimum(pixel):
    return min(pixel[0], pixel[1], pixel[2])


def average(interval, function):
    interval_pixels = [function.__call__(pixel) for pixel in interval]
    return interval[interval_pixels.index(max(interval_pixels, key=interval_pixels.count))]

choices = {
    "lightness": lightness,
    "hue": hue,
    "intensity": intensity,
    "minimum": minimum,
    "saturation": saturation,
    "red": red,
    "green": green,
    "blue": blue,
    "average": average,
}
