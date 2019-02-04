from imageai.Detection import ObjectDetection

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="110.jpg", output_image_path="imagenew1.png", minimum_percentage_probability=10)
