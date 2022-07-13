"""
a wrapper for fast loading pre-built meshes and make it
easy to use for pyeit package

Copyright (c) Benyuan Liu. All Rights Reserved.
Distributed under the (new) BSD License. See LICENSE.txt for more info.
"""
from pkg_resources import resource_filename
from scipy.io import loadmat
import pyeit.mesh as mesh
import pyeit.io.mes as mes

# visualization
import matplotlib.pyplot as plt


def load(model="hsymm"):
    """load a pre-built mesh, returns PyEITMesh"""
    if model == "hsymm":
        return _load_hsymm()
    elif model in ["I0007", "DLS2", "IM470", "lung"]:
        return _load_mes(model)
    else:
        raise NotImplementedError("{} not supported".format(model))


def _load_hsymm(rev=22):
    """load symmetric head"""
    mesh_file = resource_filename("eitmesh", "data/hsymm{}.mat".format(rev))
    mat = loadmat(mesh_file, simplify_cells=True)["mesh_dataset"]
    mesh_obj = mesh.PyEITMesh(
        node=mat["node"],
        element=mat["element"],
        perm=mat["perm"],
        el_pos=mat["el_pos"],
        ref_node=mat["ref_node"],
    )

    return mesh_obj


def _load_mes(mes_name):
    """load .mes mesh"""
    mstr = resource_filename("eitmesh", "data/{}.mes".format(mes_name))
    # imstr = mstr.replace(".mes", ".bmp")
    mesh_obj = mes.load(fstr=mstr)

    return mesh_obj


if __name__ == "__main__":
    mes_name = "hsymm"
    mesh_obj = load(mes_name)

    # print the size
    e, pts, perm = mesh_obj.element, mesh_obj.node, mesh_obj.perm
    print("tri size = (%d, %d)" % e.shape)
    print("pts size = (%d, %d)" % pts.shape)
    print("perm size = (%d,)" % perm.shape)

    # compare two mesh
    meshes = ["hsymm", "IM470", "DLS2"]
    mesh_array = [[load(mes_name), mes_name] for mes_name in meshes]

    fig, axs = plt.subplots(1, len(meshes), figsize=(15, 6))
    for i, ax in enumerate(axs):
        mesh_obj, title = mesh_array[i]
        mes.mesh_plot(ax, mesh_obj, title=title)
