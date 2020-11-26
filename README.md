# pyeit-models

*status: experimental*

Models and Meshes for [pyEIT](https://github.com/liubenyuan/pyEIT)

## 1. Introduction

Build 2D (triangles) and 3D (tetrahedrons) mesh models using third party libraries.
These meshes are for the forward and inverse simulations in EIT settings.
So we will add an easy to use electrodes interface.

Some mesh-generating or mesh-converting libraries (under consideration).
  
  - [meshio](https://github.com/nschloe/meshio) Mesh input and output conversion (by nschloe).
  - [pygmsh](https://github.com/nschloe/pygmsh) Gmsh for Python (by nschloe).
  - [meshplex](https://github.com/nschloe/meshplex) Compute interesting points, areas, and volumes in triangular and tetrahedral meshes.

  - [meshpy](https://github.com/inducer/meshpy) 2D/3D simplicial mesh generator interface for Python (Triangle, TetGen, gmsh)
  - [tetwild](https://github.com/Yixin-Hu/TetWild) Robust Tetrahedral Meshing in the Wild.
  - [triwild](https://github.com/wildmeshing/TriWild) TriWild: Robust Triangulation with Curve Constraints.
  - [PyMesh](https://github.com/PyMesh/PyMesh) Geometry Processing Library for Python. An interface, the mesh generation part are using CGAL, Triangle, TetGen and Quartet.

  - [iso2mesh](https://github.com/fangq/iso2mesh) A 3D surface and volumetric mesh generator for MATLAB/Octave.

Visualization of 3D tetrahedron meshes.

Some thoughts on FEM simulation
  
  - [ceviche](https://github.com/fancompute/ceviche) Electromagnetic Simulation and Automatic Differentiation

## 2. Dependences

## 3. Applications

Some sample applications. FEM/EIT simulations using [pyEIT](https://github.com/liubenyuan/pyEIT)

