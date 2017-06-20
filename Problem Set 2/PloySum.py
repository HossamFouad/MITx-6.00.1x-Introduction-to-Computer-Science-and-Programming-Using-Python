from math import tan , pi
def polysum(n,s):
      """
      input : n number of sides. Each side has length s
      output: sum the area and square of the perimeter of the regular polygon ,rounded to 4 decimal places
      """
      area = (0.25*n*(s**2))/tan(pi/n)
      perimeter=n*s
      return round(area+perimeter**2,4)
