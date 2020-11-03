# EPAI Session 13 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Sequence Types - 1 ". Sequences are iterables with indexing capability. For example List and Tuple are sequence type and iterables are the ones which can be passed element by element by without any index. Sets and Dictionary are Iterables.

Solution:-
**Class is implemented in Module regular_poly.py**

**Class is implemented in Module regular_poly.py**

**Ipynb file to test the above mentioned Modules**


1. We have implemented a Regular Polygon class which takes number or vertices and circumradius and gives a polygon class object with following properties-
- Create a Polygon Class:
    - where initializer takes in:
        - number of edges/vertices
        - circumradius
    - it provide following properties:
        - # edges
        - # vertices
        - interior angle
        - edge length
        - apothem
        - area
        - perimeter
    - that has these functionalities:
        - a proper \_\_repr__ function
        - implements equality (==) based on # vertices and circumradius (\_\_eq__)
        - implements > based on number of vertices only (\_\_gt__)


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

Implementing \_\_getitem__ method makes the class as a sequence type. We have used Static Method to avoid multiple instances and LRU cache helps in performance improvement
