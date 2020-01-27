from imageai.Detection import ObjectDetection
import os
from PIL import Image
from shutil import copyfile
import timeit
import imghdr

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()
print("Model Loaded")

input_list = list()


def calc_area_percentage(x1, y1, x2, y2, image_path):
	im = Image.open(image_path)
	width, height = im.size
	area = abs(x1-x2)*abs(y1-y2)
	area_image = width*height
	return area/area_image

count = 1
cwd = os.getcwd()  # Get the current working directory (cwd)
new_images_path = os.path.join(cwd,'imgs_new/')

def object_detector(data):
	# print(data['filename'])
	image_path = os.path.join(cwd,"imgs",data['filename'])
	print(imghdr.what(image_path))
	if imghdr.what(image_path) != 'jpeg':
		print(data['filename']+"--->Not JPEG")
		return
	#print(image_path)
	detections = detector.detectObjectsFromImage(input_image=image_path, minimum_percentage_probability=80)
	#print(detections)
	for detection in detections:
		#print(detection['name'] == data['object'])
		if (detection['name'] == data['object']) and (calc_area_percentage(detection['box_points'][0],detection['box_points'][1],detection['box_points'][2],detection['box_points'][3],image_path)>0.6):
			# print(detections)
			final_captions_file = open("captions-preprocessed.txt","a+")
			global count
			final_captions_file.write(data['caption'])
			final_captions_file.close()
			copyfile(image_path, new_images_path+str(count)+".jpg")
			count += 1
			print(data['filename']+"--->Approved")
			continue
		else:
			pass
			#print(data['filename']+"--->Rejected")


def detection_handler(object):
	with open('captions-labelled.txt') as f:
		for line in f:
			line_list = line.split(',',1)
			d = dict()
			d['filename'] = line_list[0]+".jpg"
			d['caption'] = line_list[1]
			d['object'] = object
			input_list.append(d)

	'''print("Number of images to detect: ",len(input_list))
	print("---------------------------------------------------------------")
	print(input_list[:5])
	print("---------------------------------------------------------------")'''

	cnt = 0
	for inputs in input_list:
		start = timeit.default_timer()
		object_detector(inputs)
		stop = timeit.default_timer()
		print('\t\t\tTime: ', stop - start)  
		
detection_handler('dog')
