# Analytic Geometry

This is a library done in collaboration with [Élida Castro](https://github.com/elidacastro) and [Victória Sampaio](https://github.com/suzuyay). To sum it up, it is a collection of functions for solving Analytic Geometry problems using Python. With this library you can do stuff like:

 - Calculate the distance between two vectors
 - Calculate the area of a triangle
 - Calculate the orthogonal projection using two vectors
 
## Dependencies

You don't need any third party librarires to use this, but we strongly recommend having [NumPy](https://github.com/numpy/numpy) installed in your computer. The following command will do it for you.

```
$ pip3 install numpy
```

To use this library, simple add the `geometry.py` file to your project folder and add the following lines to your project file:

```
import geometry as geo
```

> Done, you are ready to use it!

## Methods

- `mid_point` recieves two vectors and returns the mid point between them.
- `scalar_product` recieves two vectors as parameters and returns the scalar product.
- `modulus` recieves a vector and returns it's modulus.
- `angle` recieves two vectors and returns the angle (measured in degrees) between them.
- `orthogonal_projection` recieves two vectors and returns the orthogonal projection.
- `triangle_area` and `parallelogram_area` recieves two vectors as parameters and returns the area.
- `cross_product` recieves two arrays of `2` or `3` dimensions and returns their cross product.

## Examples

#### Midpoint method
This method calculates the mid point between two vectors

```
geo.midpoint([5, 1], [-2, -9])
```

Returns `[1.5, -4]` as the result.

#### Distance method
Calculates the distance between two vectors

```
geo.distance([-3, 11], [2, 1])
```

Which will result in `13`.

#### Scalar product method
This method calculates the scalar product between two vectors

```
geo.scalar_product([-5, 6], [4, 3])
```

This results in `-38`.

#### Modulus method
The modulus method returns the modulus of a given vector, example:

```
geo.modulus([-23, 24])
```

Which will result in `33.24`.

#### Angle method
This method recieves two arrays as parameters and returns the angle formed between them.

```
geo.angle([-5, 6], [4, -3])
```

This example results in `166.68` degrees.


#### Orthogonal projection method
This method recieves two arrays as parameters and returns the orthogonal projection.

```
geo.orthogonal_projection([5, 0, -3], [2, -1, 1])
```

Which returns `[2.3, -1.1, 1.1]`.

#### Triangle and Parallelogram area methods

Both methods recieve two arrays as parameters and returns the area of either the triangle or parallelogram, example:

```
geo.parallelogram_area([5, 0, -3], [2, -1, 1])
```

Will return `12.44` as the result.

#### Cross product method

This method recieves two arrays of either `2` or `3` dimensions and returns their cross product

```
geo.cross_product([5, -6], [4, -3])
```

Returns `[15, -24]` as the result.

## Author
- Eder Lima - [GitHub](https://github.com/Nxrth-x) - [LinkedIn](https://linkedin.com/in/lima-eder)

## Aknowledgments

Special thanks to [Élida Castro](https://github.com/elidacastro) for the massive help in developing this project, and also massive thanks to [Victória Sampaio](https://github.com/suzuyay) helping us in writting tests for the library.

This ReadMe file was made using [Dillinger](https://dillinger.io).
