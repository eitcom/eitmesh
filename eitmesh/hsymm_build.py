"""head phantom (symmetric)"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat, savemat

from pyeit.io.mes import mesh_plot
from pyeit.mesh import PyEITMesh, shape, distmesh
import pyeit.mesh.utils as utils

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
mesh_dataset = PyEITMesh(node=p, element=t, perm=perm, el_pos=el_pos, ref_node=0)
fig, ax = plt.subplots(figsize=(9, 6))
mesh_plot(ax, mesh_dataset)

save_mesh = False
if save_mesh:
    # save figure
    # fig.savefig("../doc/images/hsymm22.png", dpi=100)

    # save mesh
    savemat("./data/hsymm22.mat", {"mesh_dataset": mesh_dataset})

    # load and verify mesh
    mat = loadmat("./data/hsymm22.mat", simplify_cells=True)["mesh_dataset"]
    mesh_obj = PyEITMesh(
        node=mat["node"],
        element=mat["element"],
        perm=mat["perm"],
        el_pos=mat["el_pos"],
        ref_node=mat["ref_node"],
    )
