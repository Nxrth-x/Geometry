# Dependencies
import math


# Calculates the distance between two straight lines using the formula
# distance = sqrt((x2 - x1)² - (y2 - y1)²) ...
def distance(a: list, b: list) -> float:
     if(len(a)==len(b)):
          distance = 0
          for i in range(len(a)):
               distance += (b[i]-a[i])**2
          return math.sqrt(distance)
     else:
          raise Exception("Error!\nBoth arrays should be the same lenght!")


# Calculates the midpoint using the formula:
# midpoint = [(x1+x2)/2, (y1+y2)/2...]
def midpoint(a: list, b: list) -> list:
     if(len(a)==len(b)):
          return [(a[i]+b[i])/2 for i in range(len(a))]
     else:
          raise Exception("Error!\nBoth arrays should be the same lenght!")


# Calculates the scalar product using the formula:
# scalar_product = (x1 . x2) + (y1 + y2) ...
def scalar_product(a: list, b: list) -> float:
     if(len(a)==len(b)):
          scalar_product = 0
          for i in range(len(a)):
               scalar_product += a[i]*b[i]
          return scalar_product
     else:
          raise Exception("Error!\nBoth arrays should be the same lenght!")


# Calculates the modulus of the vector using the formula
# modulus = sqrt( x² + y² ...) 
def modulus(vector: list) -> float:
     modulus = 0
     for i in range(len(vector)):
          modulus += vector[i]**2
     return math.sqrt(modulus)


# Calculates the angle between two vectors using the formula
# cosine = (u . v) / (|u|.|v|)
def angle(a: list, b: list) -> float:
     ab = scalar_product(a, b)
     mod_a = modulus(a)
     mod_b = modulus(b)
     cosine = ab/(mod_a*mod_b)
     return math.degrees(math.acos(cosine))


# Calculates the orthogonal_projection using the formula:
# orthogonal_projection = ((u * v) / v²) * v
def orthogonal_projection(a: list, b: list) -> list:
     ab = scalar_product(a, b)
     bb = scalar_product(b, b)
     return multiply_vector(b, ab/bb)


def multiply_vector(a: list, b: float) -> list:
     vector = []
     for i in range(len(a)):
          vector.append(a[i] * b)
     return vector


def triangle_area(a: list, b: list) -> float:     
     return modulus(cross_product(a, b)) / 2


def parallelogram_area(a: list, b: list) -> float:
     return modulus(cross_product(a, b))


def cross_product(a: list, b: list) -> list:
     #Two dimensional array
     if(len(a)==2 and len(a)==len(b)):
          i: float = a[0] * b[1]
          j: float  = -(a[1] * b[0])
          return [i, j]
          
     #Three dimensional array
     elif(len(a)==3 and len(a)==len(b)):
          i: float = (a[1] * b[2]) - (a[2] * b[1])
          j: float = (a[2] * b[0]) - (a[0] * b[2])
          k: float = (a[0] * b[1]) - (a[1] * b[0])
          return [i, j, k]

     #Program doesn't support 4+ dimensional array
     else:
          raise Exception("Error!\nBoth arrays should be the same length and 2 or 3 dimensions.")
