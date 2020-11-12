# Mesh Models

  - [x] `DLS2.mes` human head annotated mesh
  - [x] `I0007.mes` small scaled down human head mesh
  - [x] `lung.mes` human throax annotated mesh

```python
import pkg_resources
mstr = pkg_resources.resource_filename('pyeit-models', 'model/I0007.mes')
```
where `mstr` is the path to the mesh model.

The mesh structure was developed by the **FMMU EIT group** (Bin Yang, et al.)
Please Cite the following paper if you are using .mes in your research:

```
Yang, Bin, et al. "Comparison of electrical impedance tomography and
intracranial pressure during dehydration treatment of cerebral edema."
NeuroImage: Clinical 23 (2019): 101909.
```

