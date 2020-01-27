import os
from imageai.Detection import ObjectDetection

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()

cwd = os.getcwd()  # Get the current working directory (cwd)
input_image_path = os.path.join(cwd,"imgs","1.jpg")

detections = detector.detectObjectsFromImage(input_image=input_image_path, output_image_path="test.png", minimum_percentage_probability=10)
print(detections)