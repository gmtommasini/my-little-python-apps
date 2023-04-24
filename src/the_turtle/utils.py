
import colorgram
import random


def random_color():
  # return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
  return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))


# HIRST
def extract_colors(path="hirst.jpg", number_of_colors=20):
  '''Receives the path of a picture and extract the number_of colors required.
  It ignores the backgroud color (usually white), meaning that it will ignore any colors that covers more than 50% of the picture'''
  colors = colorgram.extract(path, number_of_colors)
  rgb = [tuple(color.rgb) for color in colors if (color.proportion < 0.5 and color.proportion > 0.005)]
  # Today I learned that I can't use map() here, because it will forcelly map None to the non wanted values
  return rgb
