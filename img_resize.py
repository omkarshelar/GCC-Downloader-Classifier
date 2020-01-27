import os
from PIL import Image

size = 64 , 64
cwd = os.getcwd()
directory = os.path.join(cwd,"imgs_new")
for filename in os.listdir(directory):
	img_file = os.path.join(directory, filename)
	im = Image.open(img_file)
	im_resized = im.resize(size,Image.ANTIALIAS)
	im_resized.save(img_file, ppi=(64,64))