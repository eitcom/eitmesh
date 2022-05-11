from pkg_resources import resource_filename
import numpy as np
import matplotlib.pyplot as plt
from pyeit.io import mes

# load mesh (PyEITMesh dataset)
file_name = "I0007"
mesh_file = resource_filename("eitmesh", "data/{}.mes".format(file_name))
mesh = mes.load(mesh_file)
x, y = mesh.node[:, 0], mesh.node[:, 1]
# load mesh background image
mesh_img = mesh_file.replace(".mes", ".bmp")
mesh_bk = plt.imread(mesh_img)
print(mesh.elem_centers.shape)
xy_center = np.array(
    [np.mean(x[mesh.el_pos[[4, 13]]]), np.mean(y[mesh.el_pos[[0, 8]]])]
)

fig, ax = plt.subplots()
mesh_im = ax.imshow(mesh_bk, origin="upper")
ax.triplot(x, y, mesh.element, lw=1.0)
for i, e in enumerate(mesh.el_pos):
    ax.plot(x[e], y[e], "ro")
    ele_cord = np.array([x[e], y[e]])
    text_offset = (ele_cord - xy_center) * 0.06 * [1, -1]
    ax.annotate(
        str(i + 1),
        xy=ele_cord,
        xytext=text_offset,
        textcoords="offset points",
        color="white",
        fontsize=12,
        ha="center",
        va="center",
    )
ax.set_title(mesh_file.split("/")[-1])
ax.set_xlabel("X")
ax.set_ylabel("Y")
# fig.savefig("../doc/images/{}.png".format(file_name), dpi=96)
