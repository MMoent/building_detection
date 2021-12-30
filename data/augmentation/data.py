import os
import cv2
import numpy as np
import random


img_path = 'train_img'
label_path = 'train_label'
f = os.listdir(img_path)

cnt = 500
for i in f:
	im = cv2.imread(os.path.join(img_path, i))
	label = cv2.imread(os.path.join(label_path, i))

	flip = random.randint(0, 1)
	flipped_im = cv2.flip(im, flip)
	flipped_label = cv2.flip(label, flip)

	rotate = random.randint(1, 3)
	rotated_im = np.rot90(im, rotate)
	rotated_label = np.rot90(label, rotate)

	flipped_im_name = str(cnt) + '.png'
	cv2.imwrite(os.path.join(img_path, flipped_im_name), flipped_im)
	cv2.imwrite(os.path.join(label_path, flipped_im_name), flipped_label)

	cnt += 1
	rotated_im_name = str(cnt) + '.png'
	cv2.imwrite(os.path.join(img_path, rotated_im_name), rotated_im)
	cv2.imwrite(os.path.join(label_path, rotated_im_name), rotated_label)

	cnt += 1
