# EPAI Session 13 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Sequence Types - 1 ". Sequences are iterables with indexing capability. For example List and Tuple are sequence type and iterables are the ones which can be passed element by element by without any index. Sets and Dictionary are Iterables.

Solution:-

**Class is implemented in Module regular_poly.py**

https://github.com/SachinDangayach/session13-SachinDangayach/blob/master/regular_poly.py

**Class is implemented in Module regular_poly.py**

https://github.com/SachinDangayach/session13-SachinDangayach/blob/master/regular_poly_seq.py

**Ipynb file to test the above mentioned Modules**

https://github.com/SachinDangayach/session13-SachinDangayach/blob/master/session13.ipynb


1. We have implemented a Regular Polygon class which takes number or vertices and circumradius and gives a polygon class object with following properties-
- Create a Polygon Class:
    - 1. where initializer takes in:
        - 1. number of edges/vertices
        - 2. circumradius
    - 2. it provide following properties:
        - 1. number of edges
        - 2. number of  vertices
        - 3. interior angle
        - 4. edge length
        - 5. apothem
        - 6. area
        - 7. perimeter
    - 3. that has these functionalities:
        - 1. a proper \_\_repr__ function
        - 2. implements equality (==) based on # vertices and circumradius (\_\_eq__)
        - 3. implements > based on number of vertices only (\_\_gt__)


2. Implement a Custom Polygon sequence type:
  - 1. where initializer takes in:
      - 1. number of vertices for largest polygon in the sequence
      - 2. common circumradius for all polygons
  - 2. that can provide these properties:
      - 1. max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
  - 3. that has these functionalities:
      - 1. functions as a sequence type (\_\_getitem__)
      - 2. supports the len() function (\_\_len__)
      - 3. has a proper representation (\_\_repr__)

### Implementing \_\_getitem__ method makes the class as a sequence type. We have used Static Method to avoid multiple instances and LRU cache helps in performance improvement
