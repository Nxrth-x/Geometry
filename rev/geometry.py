import math
import matplotlib.pyplot as plt


class Coordinate:

     def __init__(self, *args):
          if(len(args)>=2 and len(args)<=3):
               if(len(args) == 2):
                    self.x = args[0]
                    self.y = args[1]
                    self.dim = 2
               else:
                    self.x = args[0]
                    self.y = args[1]
                    self.z = args[2]
                    self.dim = 3
          else:
               raise Exception("Coordinates must be either 2 or 3 dimensions.")


     def __str__(self):
          if(self.dim == 3):
               return f"<{self.x}, {self.y}, {self.z}>"
          else:
               return f"<{self.x}, {self.y}>"


     def __add__(self, other) -> object:
          if(self.dim == other.dim):
               arr = []
               obj_dict = self.__dict__
               for key, value in obj_dict.items():
                    if(key == 'dim'):
                         return Coordinate(*arr)
                    else:
                         arr.append(self[key] + other[key])
          else:
               raise Exception("Error! Both coordinates must be the same dimension.")


     def __sub__(self, other) -> object:
          if(self.dim == other.dim):
               arr = []
               obj_dict = self.__dict__
               for key, value in obj_dict.items():
                    if(key == 'dim'):
                         return Coordinate(*arr)
                    else:
                         arr.append(self[key] - other[key])
          else:
               raise Exception("Error! Both coordinates must be the same dimension.")


     def __mul__(self, val) -> object:
          arr = []
          obj_dict = self.__dict__
          for key, value in obj_dict.items():
               if(key == 'dim'):
                    return Coordinate(*arr)
               else:
                    arr.append(value * val)


     def __rmul__(self, val) -> object:
          arr = []
          obj_dict = self.__dict__
          for key, value in obj_dict.items():
               if(key == 'dim'):
                    return Coordinate(*arr)
               else:
                    arr.append(value * val)


     def __truediv__(self, val) -> object:
          arr = []
          obj_dict = self.__dict__
          for key, value in obj_dict.items():
               if(key == 'dim'):
                    return Coordinate(*arr)
               else:
                    arr.append(value / val)

     def __getitem__(self, key):
          return getattr(self, key)

     def midpoint(self, other) -> object:
          if(self.dim == other.dim):
               return (self + other)/2
          else:
               raise Exception("Both coordinates must be the same dimension.")


     def distance(self, other) -> object:
          if(self.dim == other.dim):
               acc = 0
               obj_dict = self.__dict__
               for key, value in obj_dict.items():
                    if(key == 'dim'):
                         return math.sqrt(acc)
                    else:
                         acc += (other[key] - self[key]) ** 2
          else:
               raise Exception("Both coordinates must be the same dimension.")


     def scalar_product(self, other):
          if(self.dim == other.dim):
               acc = 0
               obj_dict = self.__dict__
               for key, value in obj_dict.items():
                    if(key == 'dim'):
                         return acc
                    else:
                         acc += self[key] * other[key]
          else:
               raise Exception("Both coordinates must be the same dimension.")


     def modulus(self):
          acc = 0
          obj_dict = self.__dict__
          for key, value in obj_dict.items():
               if(key == 'dim'):
                    return math.sqrt(acc)
               else:
                    acc += value ** 2
          

     def angle(self, other):
          if(self.dim == other.dim):
               ab = self.scalar_product(other)
               mod_a = self.modulus()
               mod_b = other.modulus()
               cos = ab / (mod_a * mod_b)
               return math.degrees(math.acos(cos))
          else:
               raise Exception("Error! Both coordinates must be the same dimension.")


     def orthogonal_projection(self, other):
          if(self.dim == other.dim):
               ab = self.scalar_product(other)
               bb = other.scalar_product(other)
               return (ab / bb) * other
          else:
               raise Exception("Error! Both coordinates must be the same dimension.")


     def cross_product(self, other):
          if(self.dim == other.dim):
               if(self.dim == 2):
                    i = self['x'] * other['y']
                    j = -(self['y'] * other['x'])
                    return Coordinate(i, j)
               else:
                    i = (self['y'] * other['z']) - (self['z'] * other['y'])
                    j = (self['z'] * other['x']) - (self['x'] * other['z'])
                    k = (self['x'] * other['y']) - (self['y'] * other['x'])
                    return Coordinate(i, j, k)
     

     def triangle(self, other):
          if(self.dim == other.dim and self.dim == 2):
               origin = [0, 0]
               arr1 = [self['x'], self['y']]
               arr2 = [other['x'], other['y']]
               plt.axes()
               triangle = plt.Polygon([origin, arr1, arr2], fc='b')
               plt.gca().add_patch(triangle)
               plt.axis('scaled')
               plt.show()
          else:
               raise Exception("Error! This method suports only two dimensional coordinates.")
     

     def triangle_area(self, other):
          cross = self.cross_product(other)
          return cross.modulus() / 2


     def parallelogram_area(self, other):
          cross = self.cross_product(other)
          return cross.modulus()

