import os
import cv2
import numpy as np

path = 'PNGImages'
ims = os.listdir(path)

r, g, b = 0, 0, 0
for i in ims:
	im = cv2.imread(os.path.join(path, i))
	im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
	r += np.std(im[:, :, 0]) / 255
	g += np.std(im[:, :, 1]) / 255
	b += np.std(im[:, :, 2]) / 255
	
r /= len(ims)
g /= len(ims)
b /= len(ims)
print(r,g,b)
