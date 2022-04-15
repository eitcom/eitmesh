# Mesh Models From The FMMU EIT Group

  - [x] `DLS2.mes` human head annotated mesh
  - [x] `I0007.mes` small scaled down human head mesh
  - [x] `IM470.mes` regenerated head mesh (yang bin)
  - [x] `lung.mes` human throax annotated mesh

```python
import pkg_resources
mstr = pkg_resources.resource_filename('eitmesh', 'data/I0007.mes')
```
where `mstr` is the path to the mesh model.

The mesh structure was developed by the **FMMU EIT group** (XiuZhen Dong, et al.)
Please Cite the following paper if you are using .mes in your research:

```
Yang, Bin, et al. "Comparison of electrical impedance tomography and
intracranial pressure during dehydration treatment of cerebral edema."
NeuroImage: Clinical 23 (2019): 101909.
```

# Models created by Benyuan

These models are simple, dedicated meshes.

  - [x] `hsymm22.mat` symmetric, refined head mesh generated using distmesh

These `.mat` meshes should be used as,
```python
mat = loadmat("hsymm22.mat", simplify_cells=True)
mesh_obj, el_pos = mat["mesh_obj"], mat["el_pos"]
```

If you find these mesh usefull, please cite our works.
```bibtex
@article{liu2018pyeit,
  title={pyEIT: A python based framework for Electrical Impedance Tomography},
  author={Liu, Benyuan and Yang, Bin and Xu, Canhua and Xia, Junying and Dai, Meng and Ji, Zhenyu and You, Fusheng and Dong, Xiuzhen and Shi, Xuetao and Fu, Feng},
  journal={SoftwareX},
  volume={7},
  pages={304--308},
  year={2018},
  publisher={Elsevier}
}
```
