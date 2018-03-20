# Snail-run-3D
A snail was set free, his world was 3D, he was an escapee and he jumps with the space key

#Plan
Rendering engine

Class Objects:
- Line
- Vector
- Plane
- Point

Cube.py has two classes: Cube and Cuboid.
Cube has a size attribute, which is the distance from the centre of the cube to the centre of its faces (half the length of a edge).
Cuboid has three attributes for size: length, breadth and height, which specify the corresponding values of the cuboid.

The vertices on both the cube and cuboid are defined like this:
  3 ---------- 7
 /|           /|
1 --------- 5  |
| |         |  |
| 2---------|--6
|/          | /
0---------- 4

The co-ordinates of each vertice are stored in a list with the number of the vertices being the its index in the list.
