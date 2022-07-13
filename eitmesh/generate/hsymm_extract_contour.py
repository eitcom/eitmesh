# convert head mesh to exterior contours
import numpy as np
import matplotlib.pyplot as plt
from pkg_resources import resource_filename

# image processing
import cv2
import imutils
from scipy.ndimage import gaussian_filter
from scipy import interpolate
import scipy.signal as ss
from pyeit.mesh.utils import to_polar, to_xy

# %% load mesh image and find contours
mstr = resource_filename("eitmesh", "data/DLS2.mes")
imstr = mstr.replace(".mes", ".bmp")
# Read in the image as grayscale - Note the 0 flag
im0 = cv2.imread(imstr, 0)
im = imutils.rotate(im0, -3.1)
im = gaussian_filter(im, sigma=2.0, mode="nearest")

# Run findContours - Note the RETR_EXTERNAL flag
# Also, we want to find the best contour possible with CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(
    im.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
)

# extract ploy points
cnt = contours[0]
approx = cv2.approxPolyDP(cnt, 0.00075 * cv2.arcLength(cnt, True), True)
xy = approx.squeeze(1)
print(xy.shape)

# Create an output of all zeroes that has the same shape as the input image
out = np.zeros_like(im)

# On this output, draw all of the contours that we have detected
# in white, and set the thickness to be 3 pixels
cv2.drawContours(out, contours, -1, 255, 3)

# Spawn new windows that shows us the donut
# (in grayscale) and the detected contour
cv2.imshow("Donut", im)
cv2.imshow("Output Contour", out)

# Wait indefinitely until you push a key.
cv2.waitKey(0)
cv2.destroyAllWindows()

# %% smooth poly points and resample
dist, deg = to_polar(xy)
dist1 = ss.medfilt(dist, 5)

# interpolate
curve_fit = interpolate.interp1d(deg, dist1, kind="cubic", fill_value="extrapolate")
deg_p1 = np.linspace(0, 180, 14, endpoint=False)
deg_p2 = np.linspace(180, 360, 18, endpoint=False)
deg2 = np.hstack([deg_p1, deg_p2])
dist2 = curve_fit(deg2)
xx, yy = to_xy(dist2, deg2)
print(xx.shape)

# plot
fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(xx, yy, "-bo")
ax.axis("equal")
ax.grid(True)

# keep only half
yhalf = yy[xx <= 2]
xhalf = xx[xx <= 2]
xhalf[np.abs(xhalf) < 2] = 0
yn = np.hstack([yhalf, yhalf[xhalf < -1]])
xn = np.hstack([xhalf, -xhalf[xhalf < -1]])
print(xn.shape)

# reorder xy -> polar -> xy
xynew = np.vstack([xn, yn]).T
dist3, deg3 = to_polar(xynew, shift=False)
xx, yy = to_xy(dist3, deg3)
xynew = np.vstack([xx, yy]).astype(np.int32).T
print(np.max(np.abs(xynew)))

# plot
fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(xynew[:, 0], xynew[:, 1], "-ro")
ax.axis("equal")
ax.grid(True)
