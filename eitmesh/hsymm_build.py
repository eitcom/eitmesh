"""head phantom (symmetric)"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat, savemat

from pyeit.io.mes import mesh_plot
from pyeit.mesh import shape
from pyeit.mesh import distmesh
import pyeit.mesh.utils as utils

save_mesh = False
el_pos = np.arange(16)
# build triangles
p, t = distmesh.build(
    fd=shape.head_symm, fh=shape.area_uniform, pfix=shape.head_symm_pfix, h0=0.1
)

# modify perm
ebar = utils.edge_list(t)
ep = p[np.sort(np.unique(ebar.reshape(-1)))]
mesh_center = np.mean(p[t], axis=1)
c = mesh_center[:, np.newaxis, :] - ep[np.newaxis, :, :]
cd = np.linalg.norm(c, axis=-1)
cd_min = np.min(cd, axis=-1)
perm = np.ones(t.shape[0])
perm[cd_min < 0.1] = 0.8

# %% plot
mesh_obj = {"node": p, "element": t, "perm": perm}
fig, ax = plt.subplots(figsize=(9, 6))
mesh_plot(ax, mesh_obj, el_pos)

if save_mesh:
    # save figure
    fig.savefig("../doc/images/hsymm22.png", dpi=100)

    # save mesh
    mesh = {"mesh_obj": mesh_obj, "el_pos": el_pos}
    savemat("./data/hsymm22.mat", mesh)

    # load and verify mesh
    mat = loadmat("hsymm22.mat", simplify_cells=True)
    mesh_obj, el_pos = mat["mesh_obj"], mat["el_pos"]
